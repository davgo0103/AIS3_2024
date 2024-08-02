import os
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import jaccard_score
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# 解析 CAPA 報告並轉換為 JSON 格式
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

# 過濾檔案大小小於 3KB 的檔案
def filter_files_by_size(folder, min_size_kb):
    """過濾指定文件夾中大小小於指定KB的文件"""
    return [file for file in os.listdir(folder) if os.path.getsize(os.path.join(folder, file)) >= min_size_kb * 1024]

# 設定你的報告目錄和 JSON 輸出目錄
types = ['Emotet', 'wannacry']  # 添加多種類型
report_folders = [f'./report/{type}' for type in types]
json_folders = [f'./json_reports/{type}' for type in types]

# 轉換所有報告文件為 JSON 格式
for report_folder, json_folder in zip(report_folders, json_folders):
    convert_reports_to_json(report_folder, json_folder)

# 提取特徵
def extract_features(json_folders, min_size_kb=3):  # 過濾小於3KB的檔案
    features = {}
    for json_folder in json_folders:
        json_files = filter_files_by_size(json_folder, min_size_kb)
        for json_file in json_files:
            if json_file.endswith('.json'):
                with open(os.path.join(json_folder, json_file), 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    sample_id = json_file.split('.')[0]
                    feature_strings = []
                    for section in data:
                        for key, value in section.items():
                            if isinstance(value, list):
                                feature_strings.extend(value)
                            else:
                                feature_strings.append(value)
                    # 排序特徵以減少順序的影響
                    features[sample_id] = ' '.join(sorted(feature_strings))
    return features

# 提取特徵
features = extract_features(json_folders)
print("提取的特徵:")
for sample_id, feature in features.items():
    print(f"{sample_id}: {feature[:100]}...")  # 只印出前100個字元

# 計算相似度
def calculate_similarity_jaccard(features):
    sample_ids = list(features.keys())
    vectorizer = CountVectorizer(binary=True).fit_transform(features.values())
    vectors = vectorizer.toarray()

    jaccard_matrix = np.zeros((len(sample_ids), len(sample_ids)))
    for i in range(len(sample_ids)):
        for j in range(len(sample_ids)):
            if i != j:
                jaccard_matrix[i][j] = jaccard_score(vectors[i], vectors[j])
            else:
                jaccard_matrix[i][j] = 1.0  # 自身比較設為1

    similarity_dict = {}
    for i, sample_id in enumerate(sample_ids):
        similarity_dict[sample_id] = {}
        for j, other_sample_id in enumerate(sample_ids):
            similarity_dict[sample_id][other_sample_id] = jaccard_matrix[i][j]
    return similarity_dict

# 計算相似度
similarity = calculate_similarity_jaccard(features)

# 視覺化相似度
def visualize_similarity(similarity):
    sample_ids = list(similarity.keys())
    data = pd.DataFrame(similarity).fillna(0)
    sns.heatmap(data, xticklabels=sample_ids, yticklabels=sample_ids, cmap="YlGnBu")
    plt.title('Sample Similarity Heatmap')
    plt.show()

# 視覺化相似度
visualize_similarity(similarity)

# 生成報告
def generate_report(similarity, output_file='report.txt'):
    with open(output_file, 'w', encoding='utf-8') as file:
        for sample_id, similar_samples in similarity.items():
            file.write(f"Sample ID: {sample_id}\n")
            file.write("Similar Samples:\n")
            for other_sample_id, sim_score in sorted(similar_samples.items(), key=lambda item: item[1], reverse=True):  # 降冪排序
                file.write(f"\t{other_sample_id}: {sim_score:.2f}\n")
            file.write("\n")

# 生成報告
generate_report(similarity)
