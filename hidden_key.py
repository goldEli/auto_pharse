import requests
import json
import time
import random
import pandas as pd
from libs.phrase_api import get_all_projects, get_all_projects_strings

with open('config.json', 'r') as f:
    config = json.load(f)

access_token = config['phrase_token']

phrase_headers = {
    'Authorization': f'token {access_token}',
    'User-Agent': 'My Python App (contact@example.com)',  # Required header
    'Content-Type': 'application/json'
}

base_url="https://api.phrase.com/v2"
 
source_id_list = [
    "2c5df130502468bb56c0af6b13ae2a7c",
    "4380db9ef5d33c2041423553568ff4a2",
    "dc2160578ccc3752fbeb1668c4fb7293",
    "fc7cb42f867778a29962b4599a0f2d2a",
    "2692f7fe7a92210c34bb262cd429d594",
    "93bbad51303d8ef448074e323b5f76f9",
    "4f6963203a57bd85f9c655f6933585ba",
    "da86a54caa08526b7057961a33967731",
    "f0359452f94b49b4ed35519d1f270e95",
    "0d3a6dfc57d2fbdeb84b41e56e0423c9",
    "c89c1e440d45a16d5cd4a6c2fb59d4b9",
    "d3d8924ff42c485376fc60f4d4586d93",
    "e0e1348470cf82929438fe4a4c7cc9af",
    "e12f4039d961b8f4df1ee40ceaa82863",
    "c469ed5b091c1de2e38c7d1de2500067",
]

def read_excel_first_column(file_path):
    """
    读取Excel文件的第一列数据
    
    Args:
        file_path (str): Excel文件路径
    
    Returns:
        list: 第一列的数据列表
    """
    try:
        # 读取Excel文件
        df = pd.read_excel(file_path)
        
        # 获取第一列数据
        first_column = df.iloc[:, 0].tolist()
        
        # 过滤掉空值和NaN
        first_column = [str(item).strip() for item in first_column if pd.notna(item) and str(item).strip()]
        
        print(f"成功读取Excel文件: {file_path}")
        print(f"第一列数据数量: {len(first_column)}")
        
        return first_column
        
    except Exception as e:
        print(f"读取Excel文件时出错: {e}")
        return []



# 读取Excel文件的第一列数据
excel_file_path = "./data/Hidden keys on Crowdin (Web).xlsx"
print("开始读取Excel文件...")
first_column_data = read_excel_first_column(excel_file_path)

keys_list = []

if first_column_data:
    print("\n第一列数据:")
    for i, item in enumerate(first_column_data, 1):
        # print(f"{i}. {item}")
        keys_list.append(item)
    
    print(f"\n总共读取到 {len(first_column_data)} 条数据")
else:
    print("没有读取到任何数据")

print(keys_list)

def update_project_key_exclude(project, key, target_locale_id):
    project_id = project['id']
    url = f"{base_url}/projects/{project_id}/keys/exclude"

    payload = {
        "q": f"{key}* translated:true",
        "target_locale_id": target_locale_id,
    }
    headers = phrase_headers

    response = requests.request("PATCH", url, json=payload, headers=headers)

    print(f"{key}:{target_locale_id}:{response.text}")


def update_project_keys_exclude(project):
    for key in keys_list:
        print("--------------------------------")
        print(f"{project['name']}: {key}")
        for target_locale_id in source_id_list:
            update_project_key_exclude(project, key, target_locale_id)


# Usage
projects = get_all_projects_strings(access_token, base_url)
print(f"Found {len(projects)} projects")

for project in projects:
    project_name = project['name']
    project_id = project['id']

    # print(f"Project: {project_name} (ID: {project_id})")
    if project_name == "web-language":
        
        update_project_keys_exclude(project)
