# 引入必要模块
import requests
import json
import pandas as pd

# 定义token、commit_url、start_time、stop_time等参数
# 若不设置token每小时请求上限60次，设置后上限5000次，获取方法可参照#http://mtw.so/6fZAcv

# req_token = 'xxx'
req_token = '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'
issue_url = 'https://api.github.com/repos/spring-projects/spring-framework/issues'
start_time = '2022-02-01T00:00:00Z'
stop_time = '2022-02-28T00:00:00Z'



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
        print(new_data) # 打印数据
        # 判断请求到的数据是否为空
        if (len(new_data) < 1):
            break;
        api_data.extend(new_data)
        i += 1
    return api_data


# 定义转换issue数据为DataFrame类型的函数
def clean_issue_data(api_data):
    data = []
    for _ in api_data:
        temp_obj = {'id': _['id'], 'user_login': _['user']['login'], 'user_id': _['user']['id'],
                    'labels_name': _['labels'][0]['name'], 'labels_description': _['labels'][0]['description']}
        # 保留指定字段数据
        data.append(temp_obj)
    return pd.DataFrame(data)

# 调用定义好的get_commmit_data函数请求commit数据
issue_data = get_issue_data(req_token, issue_url, start_time, stop_time)

# 调用定义好的clean_commit_data函数处理commit数据
issue_data_df = clean_issue_data(issue_data)

# 使用pandas方法将数据保存至CSV文件
issue_data_df.to_csv('spring-framework_issue_data.csv')
print("ok")
