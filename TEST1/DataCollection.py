# 引入必要模块
import requests
import json
import pandas as pd

# 定义token、commit_url、start_time、stop_time等参数
# 若不设置token每小时请求上限60次，设置后上限5000次，获取方法可参照#http://mtw.so/6fZAcv

# req_token = 'xxx'
req_token = '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'
commit_url = 'https://api.github.com/repos/spring-projects/spring-framework/commits'
commitcomment_url = 'https://api.github.com/repos/spring-projects/spring-framework/comments'
issue_url = 'https://api.github.com/repos/spring-projects/spring-framework/issues'
issuecomment_url = 'https://api.github.com/repos/spring-projects/spring-framework/issues/comments'
pullrequest_url = 'https://api.github.com/repos/spring-projects/spring-framework/pulls'
start_time = '2022-02-01T00:00:00Z'
stop_time = '2022-02-28T00:00:00Z'


# 定义获取commit数据的函数
def get_commmit_data(req_token, commit_url, start_time, stop_time):
    i = 1
    api_data = []
    # 利用i遍历数据页
    while (True):
        header = {
            'Authorization': req_token
        }
        param = {
            'since': start_time,
            'until': stop_time,
            'per_page': 100,
            'page': i
        }
        # 利用get方法请求数据并将数据转换为json格式
        new_data = json.loads(requests.get(commit_url, params=param, headers=header).text)
        print(new_data)
        # 判断请求到的数据是否为空
        if (len(new_data) < 1):
            break;
        api_data.extend(new_data)
        i += 1
    return api_data


# 定义获取commitcomment数据的函数
def get_commitcomment_data(req_token, commitcomment_url, start_time, stop_time):
    i = 1
    api_data = []
    # 利用i遍历数据页
    while (True):
        header = {
            'Authorization': req_token
        }
        param = {
            'since': start_time,
            'until': stop_time,
            'per_page': 100,
            'page': i
        }
        # 利用get方法请求数据并将数据转换为json格式
        new_data = json.loads(requests.get(commitcomment_url, params=param, headers=header).text)
        print(new_data)
        # 判断请求到的数据是否为空
        if (len(new_data) < 1):
            break;
        api_data.extend(new_data)
        i += 1
    return api_data


# 定义获取issue数据的函数
def get_issue_data(req_token, issue_url, start_time, stop_time):
    i = 1
    api_data = []
    # 利用i遍历数据页
    while (True):
        header = {
            'Authorization': req_token
        }
        param = {
            'since': start_time,
            'until': stop_time,
            'per_page': 100,
            'page': i
        }
        # 利用get方法请求数据并将数据转换为json格式
        new_data = json.loads(requests.get(issue_url, params=param, headers=header).text)
        print(new_data)
        # 判断请求到的数据是否为空
        if (len(new_data) < 1):
            break;
        api_data.extend(new_data)
        i += 1
    return api_data


# 定义获取issuecomment数据的函数
def get_issuecomment_data(req_token, issuecomment_url, start_time, stop_time):
    i = 1
    api_data = []
    # 利用i遍历数据页
    while (True):
        header = {
            'Authorization': req_token
        }
        param = {
            'since': start_time,
            'until': stop_time,
            'per_page': 100,
            'page': i
        }
        # 利用get方法请求数据并将数据转换为json格式
        new_data = json.loads(requests.get(issuecomment_url, params=param, headers=header).text)
        print(new_data)
        # 判断请求到的数据是否为空
        if (len(new_data) < 1):
            break;
        api_data.extend(new_data)
        i += 1
    return api_data


# 定义获取pullrequest数据的函数
def get_pullrequest_data(req_token, pullrequest_url, start_time, stop_time):
    i = 1
    api_data = []
    # 利用i遍历数据页
    while (True):
        header = {
            'Authorization': req_token
        }
        param = {
            'since': start_time,
            'until': stop_time,
            'per_page': 100,
            'page': i
        }
        # 利用get方法请求数据并将数据转换为json格式
        new_data = json.loads(requests.get(pullrequest_url, params=param, headers=header).text)
        print(new_data)
        # 判断请求到的数据是否为空
        if (len(new_data) < 1):
            break;
        api_data.extend(new_data)
        i += 1
    return api_data


# 定义转换commit数据为DataFrame类型的函数
def clean_commit_data(api_data):
    data = []  # list
    for _ in api_data:
        temp_obj = {'sha': _['sha'], 'url': _['url'], 'node_id': _['node_id'], 'commit_message': _['commit']['message'],
                    'comments_url': _['comments_url'], 'comment_count': _['commit']['comment_count'],
                    'commit_date': _['commit']['committer']['date'], 'committer_name': _['commit']['committer']['name'],
                    'committer_login': _['committer']['login'] if _['committer'] else ''}  # 字典类型 key
        # 保留指定字段数据
        # c = a if a>b else b ;if ..else的变式
        data.append(temp_obj)
    return pd.DataFrame(data)


# 定义转换commitcomment数据为DataFrame类型的函数
def clean_commitcomment_data(api_data):
    data = []
    for _ in api_data:
        temp_obj = {'id': _['id'], 'user_login': _['user']['login'], 'user_id': _['user']['id'],
                    'position': _['position'], 'path': _['path'], 'body': _['body']}
        # 保留指定字段数据
        data.append(temp_obj)
    return pd.DataFrame(data)


# 定义转换issue数据为DataFrame类型的函数
def clean_issue_data(api_data):
    data = []
    for _ in api_data:
        print("_['labels'][0]['description'] is ",_['labels'][0]['description'], "type is ",type(_['labels']))
        temp_obj = {'id': _['id'], 'user_login': _['user']['login'], 'user_id': _['user']['id'],
                    'labels_name': _['labels']['name'], 'labels_description': _['labels']['description']}
        # 保留指定字段数据
        data.append(temp_obj)
    return pd.DataFrame(data)


# 定义转换issuecomment数据为DataFrame类型的函数
def clean_issuecomment_data(api_data):
    data = []
    for _ in api_data:
        temp_obj = {'id': _['id'], 'user_login': _['user']['login'], 'user_id': _['user']['id'], 'body': _['body']}
        # 保留指定字段数据
        data.append(temp_obj)
    return pd.DataFrame(data)


# 定义转换pullrequest数据为DataFrame类型的函数
def clean_pullrequest_data(api_data):
    data = []
    for _ in api_data:
        temp_obj = {'id': _['id'], 'title': _['title'], 'user_login': _['user']['login'], 'user_id': _['user']['id'],
                    'body': _['body'], 'labels_name': _['labels']['name'],
                    'labels_description': _['labels']['description']}
        # 保留指定字段数据
        data.append(temp_obj)
    return pd.DataFrame(data)


# 调用定义好的get_commmit_data函数请求commit数据
commmit_data = get_commmit_data(req_token, commit_url, start_time, stop_time)
commitcomment_data = get_commitcomment_data(req_token, commitcomment_url, start_time, stop_time)
issue_data = get_issue_data(req_token, issue_url, start_time, stop_time)
issuecomment_data = get_issuecomment_data(req_token, issuecomment_url, start_time, stop_time)
pullrequest_data = get_pullrequest_data(req_token, pullrequest_url, start_time, stop_time)

# 调用定义好的clean_commit_data函数处理commit数据
commmit_data_df = clean_commit_data(commmit_data)
commitcomment_data_df = clean_commitcomment_data(commitcomment_data)
issue_data_df = clean_issue_data(issue_data)
issuecomment_data_df = clean_issuecomment_data(issuecomment_data)
pullrequest_data_df = clean_pullrequest_data(pullrequest_data)

# 使用pandas方法将数据保存至CSV文件
commmit_data_df.to_csv('spring-framework_commit_data.csv')
print("ok")
commitcomment_data_df.to_csv('spring-framework_commitcomment_data.csv')
print("ok")
issue_data_df.to_csv('spring-framework_issue_data.csv')
print("ok")
issuecomment_data_df.to_csv('spring-framework_issuecomment_data.csv')
print("ok")
pullrequest_data_df.to_csv('spring-framework_pullrequest_data.csv')
print("ok")

