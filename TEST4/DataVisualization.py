"""数据可视化"""

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.decomposition import PCA
from TEST3.k_means import y_pred


# 热力图
def draw_heatmap(df):
    corr = df.drop(["Unnamed: 0"], axis=1).corr()  # [-1,1]
    plt.figure(figsize=(12, 12))
    plt.title('spring-framework_heatmap')
    # 调用sns库的heatmap函数，绘制热力图
    sns.heatmap(corr)
    # 保存与展示
    plt.savefig('spring-framework_heatmap.png')
    plt.show()


# k-means聚类结果在PCA(主成分分析)降维后的分布可视化
def do_PCA(data_df):
    return PCA(n_components=2).fit_transform(data_df)

# 绘制PCA图
def draw_PCA(data_df):
    # 导入数据，转成float型
    num_data_df = data_df[['commit', 'issue', 'pullrequest', 'issuecomment', 'commitcomment', 'contri']]
    numb_data_arr = num_data_df.values.astype('float')
    # 主成分分析
    X_pca = do_PCA(numb_data_arr)
    # 可视化聚类结果（PCA降维数据视图按照聚类结果上色）
    plt.title('spring-framework_cluster')
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_pred, label="PCA")
    plt.savefig('spring-framework_cluster.png')
    plt.show()


data_df = pd.read_csv('spring-framework_data.csv')
draw_heatmap(data_df)
draw_PCA(data_df)
print('ok')







