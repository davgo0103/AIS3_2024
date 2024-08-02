import requests
import os
from time import sleep
import subprocess

def download_file(url, params, file_path, retries=3, sleep_time=5):
    """嘗試多次下載檔案以處理網絡問題。"""
    for attempt in range(retries):
        try:
            with requests.post(url, data=params, stream=True) as response:
                if response.status_code == 200:
                    with open(file_path, "wb") as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    return True
                else:
                    print(f"下載失敗，響應碼 {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"嘗試 {attempt + 1}/{retries} 失敗: {e}")
            sleep(sleep_time)
    return False

def unzip_file(zip_path, extract_to, password='infected'):
    """使用系統的 7-Zip 工具解壓縮檔案。"""
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    seven_zip_path = r'C:\Program Files\7-Zip\7z.exe'  
    try:
        cmd = [seven_zip_path, 'x', zip_path, f'-o{extract_to}', f'-p{password}', '-y']
        subprocess.run(cmd, check=True)
        os.remove(zip_path)
        print(f"{zip_path} 已解壓縮並刪除原檔案。")
    except subprocess.CalledProcessError as e:
        print(f"解壓縮失敗: {e}")

def check_if_sample_exists(extract_to, sample_hash):
    """檢查指定目錄是否已存在以樣本哈希命名的文件，不考慮檔案類型。"""
    for file in os.listdir(extract_to):
        if file.startswith(sample_hash):
            return True
    return False

api_key = '5188182ec7fb344237397805768b339b'
api_url = 'https://mb-api.abuse.ch/api/v1/'
dl_type = 'Emotet' # 指定要下載的惡意軟體類型，注意已存在的資料夾名稱大小寫必須相同
destination_folder = f'./{dl_type}/'

params = {
    'query': 'get_taginfo',
    'tag': dl_type,
    'api_key': api_key,
    'limit': 1000,
}
response = requests.post(api_url, data=params)
samples = response.json().get('data', [])

if samples:
    print(f"找到 {len(samples)} 個樣本，開始下載...")
    for sample in samples:
        sample_hash = sample['sha256_hash']
        file_path = f"{sample_hash}.zip"
        if not check_if_sample_exists(destination_folder, sample_hash):
            download_params = {
                'query': 'get_file',
                'sha256_hash': sample_hash,
                'api_key': api_key
            }
            success = download_file(api_url, download_params, file_path)
            if success:
                print(f"樣本 {sample_hash} 下載成功，已儲存為 {file_path}")
                unzip_file(file_path, destination_folder, 'infected')
            else:
                print(f"樣本 {sample_hash} 下載失敗")
        else:
            print(f"樣本 {sample_hash} 已存在於目錄中，跳過。")
else:
    print("沒有找到樣本")
