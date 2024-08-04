import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import umap.umap_ as umap

# 加載相似度矩陣和特徵數據
def load_similarity_and_features(similarity_file='similarity_matrix.npy', features_file='features.json'):
    # 加載相似度矩陣
    similarity_matrix = np.load(similarity_file)

    # 加載特徵數據
    with open(features_file, 'r', encoding='utf-8') as file:
        features = json.load(file)
    
    return similarity_matrix, features

# 視覺化相似度
def visualize_similarity_umap_with_clusters(similarity_matrix, features, n_clusters=6, highlight_samples=None):
    # 標準化數據
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(similarity_matrix)

    # 使用 UMAP 進行降維
    reducer = umap.UMAP(random_state=42)
    umap_results = reducer.fit_transform(scaled_data)

    # 使用 KMeans 進行聚類
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(scaled_data)

    # 創建 DataFrame 存儲結果
    df_umap = pd.DataFrame(umap_results, columns=['umap1', 'umap2'])
    df_umap['cluster'] = clusters

    # 添加 type 信息
    df_umap['type'] = [features[sample_id]['type'] for sample_id in features.keys()]

    # 繪製 UMAP 結果
    plt.figure(figsize=(10, 10))
    scatter_plot = sns.scatterplot(x='umap1', y='umap2', data=df_umap, hue='cluster', style='type', palette='tab10', s=50, alpha=0.7)
    
    # 標注特定樣本
    if highlight_samples:
        for sample_id in highlight_samples:
            if sample_id in features:
                sample_index = list(features.keys()).index(sample_id)
                plt.scatter(df_umap.iloc[sample_index]['umap1'], df_umap.iloc[sample_index]['umap2'], color='red', marker='*', s=200)
                plt.text(df_umap.iloc[sample_index]['umap1'], df_umap.iloc[sample_index]['umap2'], sample_id, fontsize=9, weight='bold')

    plt.title(f'UMAP Visualization of Sample Similarity with KMeans Clusters (n_clusters={n_clusters})')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

# 加載數據
similarity_matrix, features = load_similarity_and_features()

# 需要標注的樣本ID列表
highlight_samples = ['unknow', 'main']

# 使用 UMAP 進行視覺化
visualize_similarity_umap_with_clusters(similarity_matrix, features, n_clusters=3, highlight_samples=highlight_samples)
