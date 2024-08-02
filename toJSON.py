import os
import json

def parse_section(lines):
    section_data = {}
    current_key = None
    
    for line in lines:
        if line.startswith("┍") or line.startswith("┕"):
            continue
        parts = line.strip().split("│")
        if len(parts) < 3:
            continue
        key = parts[1].strip()
        value = parts[2].strip()
        
        if key:
            current_key = key
            if key not in section_data:
                section_data[key] = []
            section_data[key].append(value)
        elif current_key and value:
            section_data[current_key][-1] += f" {value}"
    
    # 將只有一個元素的列表轉換為單一值
    for key, value in section_data.items():
        if len(value) == 1:
            section_data[key] = value[0]
        else:
            section_data[key] = value
    
    return section_data

def report_to_json(file_path, output_file):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    sections = []
    current_section = []
    
    for line in lines:
        if line.startswith("┍"):
            if current_section:
                sections.append(parse_section(current_section))
                current_section = []
        current_section.append(line)
    if current_section:
        sections.append(parse_section(current_section))
    
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(sections, json_file, indent=4, ensure_ascii=False)

def convert_reports_to_json(report_folder, json_folder):
    if not os.path.exists(json_folder):
        os.makedirs(json_folder)
    
    for report_file in os.listdir(report_folder):
        if report_file.endswith('.txt'):
            report_path = os.path.join(report_folder, report_file)
            json_output_path = os.path.join(json_folder, f"{os.path.splitext(report_file)[0]}.json")
            report_to_json(report_path, json_output_path)
            print(f"已將 {report_file} 轉換為 JSON。")

# 設定你的報告目錄和JSON輸出目錄
report_folder = './report/wannacry'
json_folder = './json_reports/wannacry'

# 轉換所有報告文件為JSON格式
convert_reports_to_json(report_folder, json_folder)
