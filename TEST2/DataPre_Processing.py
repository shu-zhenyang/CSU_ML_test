import pandas as pd


# 初始化一行贡献者数据
def init_data(login):
    return {
        'login': login,
        'commit': 0,
        'issue': 0,
        'pullrequest': 0,
        'issuecomment': 0,
        'commitcomment': 0,
        'contri': 0,
    }


# 定义数据预处理函数，统计每位贡献者的各项数据
def commit_preprocess(data_out, path, login_param):
    # 利用pandas读取CSV文件
    data_in = pd.read_csv(path)
    for index, row_data in data_in.iterrows():   # iterrows()可以返回所有的行索引，以及该行的所有内容
        # 判断该用户名是否为空
        if not pd.isnull(row_data[login_param]):
            login = row_data[login_param]
        else:
            continue
        # 判断该贡献者是否已加入data_out
        if login not in data_out:
            data_out[login] = init_data(login)
        data_out[login]['commit'] = data_out[login]['commit'] + 1  # 数量加1
def commitcomment_preprocess(data_out, path, login_param):
    # 利用pandas读取CSV文件
    data_in = pd.read_csv(path)
    for index, row_data in data_in.iterrows():   # iterrows()可以返回所有的行索引，以及该行的所有内容
        # 判断该用户名是否为空
        if not pd.isnull(row_data[login_param]):
            login = row_data[login_param]
        else:
            continue
        # 判断该贡献者是否已加入data_out
        if login not in data_out:
            data_out[login] = init_data(login)
        data_out[login]['commitcomment'] = data_out[login]['commitcomment'] + 1  # 数量加1
def issue_preprocess(data_out, path, login_param):
    # 利用pandas读取CSV文件
    data_in = pd.read_csv(path)
    for index, row_data in data_in.iterrows():   # iterrows()可以返回所有的行索引，以及该行的所有内容
        # 判断该用户名是否为空
        if not pd.isnull(row_data[login_param]):
            login = row_data[login_param]
        else:
            continue
        # 判断该贡献者是否已加入data_out
        if login not in data_out:
            data_out[login] = init_data(login)
        data_out[login]['issue'] = data_out[login]['issue'] + 1  # 数量加1
def pullrequest_preprocess(data_out, path, login_param):
    # 利用pandas读取CSV文件
    data_in = pd.read_csv(path)
    for index, row_data in data_in.iterrows():   # iterrows()可以返回所有的行索引，以及该行的所有内容
        # 判断该用户名是否为空
        if not pd.isnull(row_data[login_param]):
            login = row_data[login_param]
        else:
            continue
        # 判断该贡献者是否已加入data_out
        if login not in data_out:
            data_out[login] = init_data(login)
        data_out[login]['pullrequest'] = data_out[login]['pullrequest'] + 1  # 数量加1
def issuecomment_preprocess(data_out, path, login_param):
    # 利用pandas读取CSV文件
    data_in = pd.read_csv(path)
    for index, row_data in data_in.iterrows():   # iterrows()可以返回所有的行索引，以及该行的所有内容
        # 判断该用户名是否为空
        if not pd.isnull(row_data[login_param]):
            login = row_data[login_param]
        else:
            continue
        # 判断该贡献者是否已加入data_out
        if login not in data_out:
            data_out[login] = init_data(login)
        data_out[login]['issuecomment'] = data_out[login]['issuecomment'] + 1  # 数量加1


# 定义贡献者contri值计算函数
def preprocess_contri(data_out):
    k_tuple = ('commit', 'issue', 'pullrequest', 'issuecomment', 'commitcomment')
    temp = {}
    sum_all = 0
    # 遍历数据
    for login, v in data_out.items():
        user_sum = 0
        # 遍历每位贡献者的具体数据
        for k in k_tuple:
            user_sum = user_sum + v[k]

        temp[login] = user_sum
        sum_all = sum_all + user_sum
    for login, v in data_out.items():
        v['contri'] = temp[login] / sum_all * 100



data_out = {}
# 预处理原始数据，将有价值的信息集中保存在data_out里
commit_preprocess(data_out, 'spring-framework_commit_data.csv', 9)  # 参数选择第8行的数据
commitcomment_preprocess(data_out, 'spring-framework_commitcomment_data.csv', 2)
issue_preprocess(data_out, 'spring-framework_issue_data.csv', 2)
pullrequest_preprocess(data_out, 'spring-framework_pullrequest_data.csv', 3)
issuecomment_preprocess(data_out, 'spring-framework_issuecomment_data.csv', 2)

# 调用定义好的preprocess_contri函数计算contri值
preprocess_contri(data_out)

# 将数据转换为DataFrame类型
data_df = pd.DataFrame([v for v in data_out.values()])
# 使用pandas方法将数据保存至CSV文件
data_df.to_csv('spring-framework_data.csv')
