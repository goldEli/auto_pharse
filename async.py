from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

with open('config.json', 'r') as f:
    config = json.load(f)

github_token = config['token']
api_endpoint = config['api_endpoint']
phrase_url = config['phrase_url']
gitlab_url = config['gitlab_url']




def open_pages_in_tabs(project_name):
    """
    在浏览器中打开两个指定的页面在不同的tab中
    """
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

    # 第一个tab打开 Phrase repo_syncs 页面
    print("在第一个tab中打开 Phrase repo_syncs 页面...")
    driver.get(phrase_url)
    # time.sleep(3)

    # 等待页面加载并点击"Add sync"按钮
    try:
        wait = WebDriverWait(driver, 10)
        add_sync_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="translation_center_menu"]/ul/li[2]/div'))
        )
        add_sync_button.click()
        print("已点击指定XPath的按钮")
        # time.sleep(2)
    except Exception as e:
        print(f"点击指定XPath的按钮时出错: {e}")

    # wait 1s then click the button
    # time.sleep(1)
    add_sync_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="translation_center_menu"]/ul/li[2]/div/div[2]/div/div/ul/div/div/a[2]'))
    )
    add_sync_button.click()
    print("已点击gitlab按钮")

    # click project name
    # print(project_name)
    # project_name = wait.until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="modal"]/form/div/div[2]/div/div[2]/div[1]/div/div/div[1]'))
    # )
    # project_name.click()
    # time.sleep(1)
    # project_name.click()
    
    # click the checkbox
    # //*[@id="api_endpoint"]/div/label
    checkbox_element = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="api_endpoint"]/div/label'))
    )
    checkbox_element.click()
    print("已点击api_endpoint checkbox")

    # input api endpoint
    api_endpoint_input = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="api_endpoint"]/div/div[2]/div[1]/div/input'))
    )
    api_endpoint_input.clear()
    api_endpoint_input.send_keys(api_endpoint)
    print("已输入api endpoint")
    time.sleep(1)

    # click the btn
    button_element = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="token"]/div/div[1]/div'))
    )
    button_element.click()
    print("已点击按钮")
    time.sleep(1)

    # input access token
    try:
        access_token_input = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="token"]/div/div[1]/div/input'))
        )
        access_token_input.clear()
        access_token_input.send_keys(github_token)
    except Exception as e:
        print(f"输入access token时出错: {e}")
    print("已输入access token")
    

    # input project name
    # print("input project name")
    # # syn_input syn_input__has_suffix
    # project_input = wait.until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "input.syn_input.syn_input__has_suffix"))
    # )
    # project_input.clear()
    # project_input.send_keys(project_name)
    # print(f"已输入项目名称: {project_name}")
    

    # 新开第二个tab
    # print("新开第二个tab...")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])

    # 第二个tab打开 TransHub 页面
    print("在第二个tab中打开 TransHub 页面...")
    # driver.get(f"https://transhub-private.weex.tech/wwfrontend/{project_name}")
    driver.get(f"{gitlab_url}/{project_name}/hooks")
    # time.sleep(2)

    # click the add hook button
    hook_button = wait.until( 
        EC.element_to_be_clickable((By.XPATH, '//*[@id="content-body"]/div[3]/section/div/header/div[2]/button'))
    )
    hook_button.click()
    print("已点击添加钩子按钮")

    print("两个页面都已打开完成")
    print("Tab 1: Phrase repo_syncs")
    print("Tab 2: TransHub affiliate-language")
    
    # 保持浏览器打开
    print("浏览器保持打开状态，可以手动切换tab查看不同页面")
    
    return driver

if __name__ == "__main__":
    list = [
        # "activity-backend-language",
        # "activity-language",
        # "affiliate-language",
        "app-language",
        # "asset-language",
        # "gateway-language",
        # "mix-language",
        # "msg-language",
        # "new-trace-language",
        # "phrase-demo",
        # "spot-language",
        # "trade-language",
        # "unimargin-language",
        # "user-language",
        # "web-language",
        # "web-pages-language"
    ]
    for project in list:
        driver = open_pages_in_tabs(project)
    # 如果需要自动关闭浏览器，取消下面这行的注释
    # driver.quit()
