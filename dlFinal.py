import requests
import os
from time import sleep
import subprocess
import shutil
from multiprocessing import Pool
from rich.console import Console
from rich.progress import Progress

api_key = '5188182ec7fb344237397805768b339b'
api_url = 'https://mb-api.abuse.ch/api/v1/'
dl_type = 'Emotet'
destination_folder = f'./{dl_type}/'
report_folder = f'./report/{dl_type}/'
temp_dir = './temp/'
limit = 100

# 設定要分析的檔案類型
file_extension = '.exe'


console = Console()

def download_file(url, params, file_path, retries=3, sleep_time=5):
    with Progress(console=console) as progress:
        task = progress.add_task("[cyan]正在下載...", total=retries)
        for attempt in range(retries):
            try:
                with requests.post(url, data=params, stream=True) as response:
                    if response.status_code == 200:
                        with open(file_path, "wb") as f:
                            for chunk in response.iter_content(chunk_size=8192):
                                f.write(chunk)
                        progress.update(task, advance=1)
                        return True
                    else:
                        console.log(f"[red]下載失敗，響應碼：{response.status_code}")
            except requests.exceptions.RequestException as e:
                console.log(f"[yellow]第 {attempt + 1} 次嘗試失敗：{e}")
                sleep(sleep_time)
            progress.update(task, advance=1)
    return False

def unzip_file(zip_path, extract_to, password='infected'):
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    seven_zip_path = r'C:\Program Files\7-Zip\7z.exe'
    try:
        cmd = [seven_zip_path, 'x', zip_path, f'-o{extract_to}', f'-p{password}', '-y']
        subprocess.run(cmd, check=True)
        os.remove(zip_path)
        console.log(f"[green]{zip_path} 已解壓縮並刪除原檔案。")
    except subprocess.CalledProcessError as e:
        console.log(f"[red]解壓縮失敗：{e}")

def check_if_sample_exists(extract_to, sample_hash):
    for file in os.listdir(extract_to):
        if file.startswith(sample_hash):
            return True
    return False

def clean_temp_directory(temp_dir):
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

def run_capa(sample_path, report_path):
    capa_path = './capa'
    try:
        os.makedirs(os.path.dirname(report_path), exist_ok=True)
        with open(report_path, 'w') as report_file:
            subprocess.run([capa_path, sample_path], stdout=report_file, stderr=subprocess.STDOUT, check=True)
        console.log(f"[green]{sample_path} 分析完成，報告已保存於 {report_path}")
    except subprocess.CalledProcessError as e:
        console.log(f"[red]CAPA 分析失敗：{e}")

def analyze_sample(file):
    if file.endswith(file_extension):
        sample_hash = file.split('.')[0]
        report_path = os.path.join(report_folder, f"{sample_hash}.txt")
        if not os.path.exists(report_path):
            sample_path = os.path.join(destination_folder, file)
            run_capa(sample_path, report_path)

def analyze_pending_samples():
    files_to_analyze = [file for file in os.listdir(destination_folder) if file.endswith(file_extension) and not os.path.exists(os.path.join(report_folder, f"{file.split('.')[0]}.txt"))]
    with Pool(processes=os.cpu_count()) as pool:
        pool.map(analyze_sample, files_to_analyze)


def download_and_process_sample(sample_hash):
    file_path = os.path.join(temp_dir, f"{sample_hash}.zip")
    if not check_if_sample_exists(destination_folder, sample_hash):
        download_params = {
            'query': 'get_file',
            'sha256_hash': sample_hash,
            'api_key': api_key
        }
        success = download_file(api_url, download_params, file_path)
        if success:
            unzip_file(file_path, temp_dir, 'infected')
            sample_files = os.listdir(temp_dir)
            for file in sample_files:
                if file.startswith(sample_hash):
                    source_path = os.path.join(temp_dir, file)
                    target_path = os.path.join(destination_folder, file)
                    if not check_if_sample_exists(destination_folder, sample_hash):
                        shutil.move(source_path, target_path)
                        report_path = os.path.join(report_folder, f"{sample_hash}.txt")
                        if not os.path.exists(report_path):
                            run_capa(target_path, report_path)
                    else:
                        console.log(f"[yellow]{file} 已存在於 {destination_folder}，跳過。")
                    break
            clean_temp_directory(temp_dir)
        else:
            console.log(f"[red]樣本 {sample_hash} 下載失敗")
    else:
        console.log(f"[yellow]樣本 {sample_hash} 已存在於目錄中，跳過。")

def ensure_directories_exist():
    """確保所有必要的目錄都已經存在，如果不存在則創建它們。"""
    os.makedirs(destination_folder, exist_ok=True)
    os.makedirs(report_folder, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)


def main():
    ensure_directories_exist()  # 確保所有目錄都已創建
    console.log(f"[bold magenta]開始下載和分析 {dl_type} 樣本...")
    params = {
        'query': 'get_taginfo',
        'tag': dl_type,
        'api_key': api_key,
        'limit': limit,
    }

    response = requests.post(api_url, data=params)
    samples = response.json().get('data', [])

    clean_temp_directory(temp_dir)
    
    if samples:
        console.log(f"[bold blue]找到 {len(samples)} 個樣本，開始下載...")
        with Pool(processes=os.cpu_count()) as pool:
            pool.map(download_and_process_sample, [sample['sha256_hash'] for sample in samples])
        analyze_pending_samples()  # 在所有樣本處理完畢後檢查是否有未分析的樣本
    else:
        console.log("[bold red]沒有找到樣本。")

if __name__ == "__main__":
    main()