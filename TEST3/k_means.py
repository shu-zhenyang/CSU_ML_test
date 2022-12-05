import numpy as np
# 导入sklearn聚类算法中的KMeans算法
from sklearn.cluster import KMeans
# plt用于绘图
import matplotlib.pyplot as plt
# pandas是一个结构化数据处理工具集
import pandas as pd
# 用于从config模块获取项目配置
import config

# 获取数据
data_df = pd.read_csv('spring-framework_data.csv')
# 保留需要的key数据
num_data_df = data_df[['commit', 'issue', 'pullrequest', 'issuecomment', 'commitcomment', 'contri']]


"""k_means算法，K为簇的数量，means为平均的意思"""
# 更新簇中心(和直接调用效果一致)
# def update_cluster_center(cluster_center_arr1, cluster_ele_dict):
#     cluster_center_arr = cluster_center_arr1.copy()
#     cluster_center_err = 0
#     for ix, value in enumerate(cluster_center_arr):  # enumerate()将数据对象（如列表、元组或字符串）组合为一个索引序列
#         cluster_center_err += np.power((np.array(cluster_ele_dict[ix]) - value.reshape(1, -1)), 2).sum()
#         cluster_center_arr[ix] = np.r_[np.array(cluster_ele_dict[ix]), value.reshape(1, -1)].mean(axis=0)
#     return cluster_center_arr, cluster_center_err
# # 转变参数为float型
# numb_data_arr = num_data_df.values.astype('float')
# # k的数量
# cluster_num = 3
# # 定义初始中心
# cluster_center_arr = numb_data_arr[:cluster_num - 1]
# # 迭代次数与误差
# iter_num = 20
# epsilon = 1e-12
# # 进行迭代更新中心点
# while iter_num >= 0:
#     # 确定当前每个点所属的分类
#     cluster_ele_dict = {i: [] for i in range(cluster_num)}
#     for num, value in enumerate(numb_data_arr):
#         min_val_index = np.argmin(pow(value - cluster_center_arr, 2).sum(axis=1))
#         cluster_ele_dict[min_val_index].append(list(value))
#     # 更新中心点
#     new_cluster_center, rss_value = update_cluster_center(cluster_center_arr, cluster_ele_dict)
#     # 如果误差满足条件，则终止
#     if np.max(new_cluster_center - cluster_center_arr) <= epsilon:
#         break
#     else:
#         cluster_center_arr = new_cluster_center
#     iter_num -= 1


"""使用sklearn模块进行聚类分析"""
def do_cluster(data_df):
    num_data_arr = data_df.values.astype('float')
    y_pred = KMeans(max_iter=20, n_clusters=3, init='k-means++', tol=1e-12).fit_predict(num_data_arr)
    return y_pred

# 不同的cluter有不同的颜色
y_pred = do_cluster(num_data_df)
# 对聚类进行可视化处理
num = num_data_df
numb_data_arr = num_data_df.values.astype('float')
plt.scatter(numb_data_arr[:, 1], numb_data_arr[:, 3], c= y_pred)  # [:, 1] 输出第1列的数据 ； color
plt.savefig('spring-framework_cluster.png')
plt.show()



# 保存结果
def get_data_clustered(data_dict, y_pred):
    temp = {}
    for i in range(len(y_pred)):
        temp[i] = y_pred[i]
    data_dict['y'] = temp
    return pd.DataFrame(data_dict)

# print(data_clustered_df)
# print('---------------')
# print(data_clustered_df.to_dict()) 转成字典型
data_clustered_df = get_data_clustered(data_df.to_dict(), y_pred)
data_clustered_df.to_csv('spring-framework_cluster.csv')



