import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 加載相似度矩陣和特徵數據
def load_similarity_and_features(similarity_file='similarity_matrix.npy', features_file='features.json'):
    # 加載相似度矩陣
    similarity_matrix = np.load(similarity_file)

    # 加載特徵數據
    with open(features_file, 'r', encoding='utf-8') as file:
        features = json.load(file)
    
    return similarity_matrix, features

# 視覺化相似度
def visualize_similarity_tsne_with_clusters(similarity_matrix, features, n_clusters=5):
    # 標準化數據
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(similarity_matrix)

    # 使用 t-SNE 進行降維，設置合適的 perplexity 值
    n_samples = scaled_data.shape[0]
    perplexity = min(30, n_samples - 1)  # perplexity 必須小於樣本數

    tsne = TSNE(n_components=2, random_state=42, perplexity=perplexity)
    tsne_results = tsne.fit_transform(scaled_data)

    # 使用 KMeans 進行聚類
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(scaled_data)

    # 創建 DataFrame 存儲結果
    df_tsne = pd.DataFrame(tsne_results, columns=['tsne1', 'tsne2'])
    df_tsne['cluster'] = clusters

    # 添加 type 信息
    df_tsne['type'] = [features[sample_id]['type'] for sample_id in features.keys()]

    # 繪製 t-SNE 結果
    plt.figure(figsize=(10, 10))
    sns.scatterplot(x='tsne1', y='tsne2', data=df_tsne, hue='type', style='cluster', palette='tab10', s=100, alpha=0.7)
    plt.title('t-SNE Visualization of Sample Similarity with KMeans Clusters')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

# 加載數據
similarity_matrix, features = load_similarity_and_features()

# 視覺化相似度
visualize_similarity_tsne_with_clusters(similarity_matrix, features, n_clusters=3)
