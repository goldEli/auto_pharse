import requests
import json
import time
import random

with open('config.json', 'r') as f:
    config = json.load(f)

access_token = config['phrase_token']


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


def get_project_info(project_id):
    """
    Get detailed information about a specific project from Phrase Strings API
    
    Args:
        project_id (str): The ID of the project to retrieve
        access_token (str): Your Phrase access token
        base_url (str): API base URL (default: EU data center)
    
    Returns:
        dict: Project information or None if error
    """
    headers = {
        'Authorization': f'token {access_token}',
        'User-Agent': 'My Python App (contact@example.com)',  # Required header
        'Content-Type': 'application/json'
    }
    
    
    url = f"{base_url}/projects/{project_id}"
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"Project with ID '{project_id}' not found")
            return None
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


def is_english_locale(name):
    name = name.lower()
    return name in ['en', 'en-us', 'en_us', 'enus']

def is_chinese_locale(name):
    name = name.lower()
    return name in ['zh', 'zh-cn', 'zh_cn', 'zhcn']

def get_all_locales(project_id):
    
    headers = phrase_headers


    # API endpoint
    url = f'{base_url}/projects/{project_id}/locales'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        locales = response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
    return locales

def get_payload_by_locale_name(name, en_locale_id):
    # name 转小写
    name = name.lower()
    # zh
    if name in ['zh', 'zh-cn', 'zh_cn', 'zhcn']:
        return {
            "code": "zh-CN",
            "default": True,
            "main": True,
        }
    # en
    if name in ['en', 'en-us', 'en_us', 'enus']:
        return {
            "code": "en-US",
            "default": False,
            "main": True,
        }
    # zh-TW
    if name in ['zh-tw', 'zh_tw', 'zhtw']:
        return {
            "code": "zh-TW",
            "default": False,
            "main": False,
        }
    # vi-VN
    if name in ['vi', 'vi-vn', 'vi_vn', 'vivn']:
        return {
            "code": "vi",
            "default": False,
            "main": False,
            "source_locale_id": en_locale_id,
            "fallback_locale_id": en_locale_id,
        }
    # ar-SA
    if name in ['ar', 'ar-sa', 'ar_sa', 'arsa']:
        return {
            "code": "ar",
            "default": False,
            "main": False,
            "source_locale_id": en_locale_id,
            "fallback_locale_id": en_locale_id,
        }
    # de-DE
    if name in ['de', 'de-de', 'de_de', 'dede']:
        return {
            "code": "de",
            "default": False,
            "main": False,
            "source_locale_id": en_locale_id,
            "fallback_locale_id": en_locale_id,
        }
    # es-419
    if name in ['es', 'es-419', 'es_419', 'es419']:
        return {
            "code": "es-419",
            "default": False,
            "main": False,
            "source_locale_id": en_locale_id,
            "fallback_locale_id": en_locale_id,
        }
    # es-ES
    if name in ['es-es', 'es_es', 'eses']:
        return {
            "code": "es-ES",
            "default": False,
            "main": False,
            "source_locale_id": en_locale_id,
            "fallback_locale_id": en_locale_id,
        }

    # fa-IR
    if name in ['fa', 'fa-ir', 'fa_ir', 'fari']:
        return {
            "code": "fa-IR",
            "default": False,
            "main": False,
            "source_locale_id": en_locale_id,
            "fallback_locale_id": en_locale_id,
        }
    # fr-FR
    if name in ['fr', 'fr-fr', 'fr_fr', 'frfr']:
        return {
            "code": "fr",
            "default": False,
            "main": False,
            "source_locale_id": en_locale_id,
            "fallback_locale_id": en_locale_id,
        }
    # it-IT
    if name in ['it', 'it-it', 'it_it', 'itit']:
        return {
            "code": "it",
            "default": False,
            "main": False,
            "source_locale_id": en_locale_id,
            "fallback_locale_id": en_locale_id,
        }
    # ja-JP
    if name in ['ja', 'ja-jp', 'ja_jp', 'jap']:
        return {
            "code": "ja",
            "default": False,
            "main": False,
            "source_locale_id": en_locale_id,
            "fallback_locale_id": en_locale_id,
        }
    # ko-KR
    if name in ['ko', 'ko-kr', 'ko_kr', 'koko']:
        return {
            "code": "ko",
            "default": False,
            "main": False,
            "source_locale_id": en_locale_id,
            "fallback_locale_id": en_locale_id,
        }
    # pl-PL
    if name in ['pl', 'pl-pl', 'pl_pl', 'plpl']:
        return {
            "code": "pl",
            "default": False,
            "main": False,
            "source_locale_id": en_locale_id,
            "fallback_locale_id": en_locale_id,
        }
    # pt-BR
    if name in ['pt', 'pt-br', 'pt_br', 'ptbr']:
        return {
            "code": "pt-BR",
            "default": False,
            "main": False,
            "source_locale_id": en_locale_id,
            "fallback_locale_id": en_locale_id,
        }
    # ru-RU
    if name in ['ru', 'ru-ru', 'ru_ru', 'ruru']:
        return {
            "code": "ru",
            "default": False,
            "main": False,
            "source_locale_id": en_locale_id,
            "fallback_locale_id": en_locale_id,
        }
    # tr-TR
    if name in ['tr', 'tr-tr', 'tr_tr', 'trtr']:
        return {
            "code": "tr",
            "default": False,
            "main": False,
            "source_locale_id": en_locale_id,
            "fallback_locale_id": en_locale_id,
        }
    # uk-UA
    if name in ['uk', 'uk-ua', 'uk_ua', 'ukua', 'uk-uk', 'uk_uk', 'ukuk']:
        return {
            "code": "uk",
            "default": False,
            "main": False,
            "source_locale_id": en_locale_id,
            "fallback_locale_id": en_locale_id,
        }

    # en_TR
    if name in ['en_tr', 'en-tr', 'entr']:
        return {
            "code": "en-TR",
            "default": False,
            "main": False,
            "source_locale_id": en_locale_id,
            "fallback_locale_id": en_locale_id,
        }


    # 如果没找到，报错终端程序
    raise Exception(f"Locale {name} not found")

# update a locale
def update_locale(project_id, locale_id, name, en_locale_id):
    headers = phrase_headers

    url = f'{base_url}/projects/{project_id}/locales/{locale_id}'

    payload = get_payload_by_locale_name(name, en_locale_id)

    response = requests.request("PATCH", url, json=payload, headers=headers)

    if response.status_code != 200:
        print(payload)
        # 打印错误终端程序
        print(f"Error: {response.status_code} - {response.text}")
        exit()
        return False
    # print payload string
    print(json.dumps(payload, indent=4))
    print(f"update locale: {name} success")
    return True



def get_english_locale_id(locales):
    for locale in locales:
        if is_english_locale(locale['name']):
            return locale['id']
    return None

def get_chinese_locale(locales):
    for locale in locales:
        if is_chinese_locale(locale['name']):
            return locale
    return None

def get_english_locale(locales):
    for locale in locales:
        if is_english_locale(locale['name']):
            return locale
    return None

def update_project(project):

    # 获取项目信息
    project_id = project['id']

    # 获取项目中的所有语言
    locales = get_all_locales(project_id)

    english_locale_id = get_english_locale_id(locales)

    # print(f"english_locale_id: {english_locale_id}")
    # print(locales)

    # print(f"locales: {locales}")
    print("locales length: ", len(locales))
    # print("all locales name: ", [locale['name'] for locale in locales])
    # update chinese locale first 
    chinese_locale = get_chinese_locale(locales)
    if chinese_locale:
        update_locale(project_id, chinese_locale['id'], chinese_locale['name'], english_locale_id)
    else:
        print("chinese locale not found")
        exit()

    # update english locale
    english_locale = get_english_locale(locales)
    if english_locale:
        update_locale(project_id, english_locale['id'], english_locale['name'], english_locale_id)
    else:
        print("english locale not found")
        exit()

    # 更新项目中的语言
    for locale in locales:
        if locale['id'] == chinese_locale['id'] or locale['id'] == english_locale['id']:
            continue
        update_locale(project_id, locale['id'], locale['name'], english_locale_id)

# Usage
projects = get_all_projects_strings()
print(f"Found {len(projects)} projects")

for project in projects:
    print(f"Project: {project['name']} (ID: {project['id']})")
    project_name = project['name']
    project_id = project['id']

    # ignore project name 'test'
    if project_name == 'test':
        continue

    print("="*100)
    print(f"start update project: {project_name}")
    update_project(project)
    print("="*100)
    # wait random time
    random_time = random.randint(1, 3)
    time.sleep(random_time)
    print(f"wait {random_time} seconds")


