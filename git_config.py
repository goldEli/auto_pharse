import requests
import json
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open('config.json', 'r') as f:
    config = json.load(f)

access_token = config['phrase_token']
github_token = config['token']
api_endpoint = config['api_endpoint']
phrase_url = config['phrase_url']
gitlab_url = config['gitlab_url']

phrase_headers = {
    'Authorization': f'token {access_token}',
    'User-Agent': 'My Python App (contact@example.com)',  # Required header
    'Content-Type': 'application/json'
}

base_url="https://api.phrase.com/v2"

def get_all_projects_strings():
    """
    Get all projects from Phrase Strings API with pagination
    """
    all_projects = []
    page = 1
    per_page = 100  # Maximum allowed per page
    
    headers = {
        'Authorization': f'token {access_token}',
        'User-Agent': 'My Python App (contact@example.com)'  # Required header
    }
    
    while True:
        # Make request to list projects endpoint
        url = f"{base_url}/projects"
        params = {
            'page': page,
            'per_page': per_page
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            projects = response.json()
            
            # If no projects returned, we've reached the end
            if not projects:
                break
                
            all_projects.extend(projects)
            
            # Check if we got fewer projects than requested (last page)
            if len(projects) < per_page:
                break
                
            page += 1
        else:
            print(f"Error: {response.status_code} - {response.text}")
            break
    
    return all_projects


all_projects = get_all_projects_strings()
all_projects_names = [project['name'] for project in all_projects]
print(all_projects_names)

def open_phrase_yml_page(project_name="app-language"):
    """
    使用Selenium模拟浏览器打开Phrase YML配置页面
    
    Args:
        project_name: 项目名称，默认为app-language
    """
    options = Options()
    
    # 尝试连接到已存在的Chrome实例，如果不存在则创建新的
    try:
        # 首先尝试不使用用户数据目录连接
        driver = webdriver.Chrome(options=options)
        print("已连接到现有浏览器")
    except Exception as e:
        try:
            # 如果失败，尝试使用不同的用户数据目录
            options.add_argument("user-data-dir=/Users/eli/Documents/selenium_new")
            driver = webdriver.Chrome(options=options)
            print("使用新的用户数据目录创建了浏览器实例")
        except Exception as e2:
            # 如果还是失败，尝试使用临时用户数据目录
            import tempfile
            import os
            temp_dir = tempfile.mkdtemp()
            options = Options()
            options.add_argument(f"user-data-dir={temp_dir}")
            driver = webdriver.Chrome(options=options)
            print(f"使用临时用户数据目录创建了浏览器实例: {temp_dir}")

    # 打开Phrase YML配置页面
    url = f"https://transhub-private.weex.tech/wwfrontend/{project_name}/-/edit/main/.phrase.yml"
    print(f"正在打开页面: {url}")
    driver.get(url)
    
    # 等待页面加载
    wait = WebDriverWait(driver, 10)
    time.sleep(3)
    
    print(f"页面已打开完成: {project_name}")
    print("浏览器保持打开状态，可以查看Phrase YML配置")
    
    return driver


options = Options()
# 设置用户数据目录路径，使用已有的浏览器配置（如已登录）
options.add_argument("user-data-dir=/Users/eli/Documents/selenium")

# 尝试连接到已存在的Chrome实例，如果不存在则创建新的
try:
    # 尝试连接到已存在的Chrome实例
    driver = webdriver.Chrome(options=options)
    print("已连接到现有浏览器")
except Exception as e:
    # 如果连接失败，创建新的浏览器实例
    driver = webdriver.Chrome(options=options)
    print("创建了新的浏览器实例")


def open_multiple_phrase_yml_pages(project_list):
    """
    批量打开多个项目的Phrase YML配置页面
    
    Args:
        project_list: 项目名称列表
    """
    
   

    # 为每个项目打开一个新tab
    for i, project_name in enumerate(project_list):
        if i > 0:  # 第一个项目使用当前tab，其他项目使用新tab
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[-1])
        
        # 打开Phrase YML配置页面
        url = f"https://transhub-private.weex.tech/wwfrontend/{project_name}/-/edit/main/.phrase.yml"
        print(f"正在打开页面 {i+1}: {url}")
        driver.get(url)
        
        # 等待页面加载
        time.sleep(3)
        print(f"页面 {i+1} 已打开完成: {project_name}")
    
    print(f"所有 {len(project_list)} 个页面都已打开完成")
    print("浏览器保持打开状态，可以查看所有Phrase YML配置")
    
    return driver

if __name__ == "__main__":
    # 单个项目示例
    # driver = open_phrase_yml_page("app-language")
    
    # 批量打开多个项目示例
    project_list = [
        'activity-backend-language', 
        'activity-language', 
        'affiliate-language', 
        'app-language', 
        'mix-language', 
        'asset-language', 
        'gateway-language', 
        'msg-language', 
        'new-trace-language', 
        'spot-language', 
        'trade-language', 
        'unimargin-language', 
        'user-language', 
        'web-language', 
        'web-pages-language'
    ]
    
    driver = open_multiple_phrase_yml_pages(project_list)
    
    # 如果需要自动关闭浏览器，取消下面这行的注释
    # driver.quit()
