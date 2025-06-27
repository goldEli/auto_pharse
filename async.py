from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
    driver.get("https://app.phrase.com/accounts/weex-global/repo_syncs")
    time.sleep(3)

    # 等待页面加载并点击"Add sync"按钮
    try:
        wait = WebDriverWait(driver, 10)
        add_sync_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add sync')]"))
        )
        add_sync_button.click()
        print("已点击 'Add sync' 按钮")
        time.sleep(2)
    except Exception as e:
        print(f"点击 'Add sync' 按钮时出错: {e}")

    # 新开第二个tab
    print("新开第二个tab...")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])

    # 第二个tab打开 TransHub 页面
    # print("在第二个tab中打开 TransHub 页面...")
    # # driver.get(f"https://transhub-private.weex.tech/wwfrontend/{project_name}")
    # driver.get(f"https://transhub-private.weex.tech/wwfrontend/{project_name}/hooks")
    # time.sleep(2)

    # print("两个页面都已打开完成")
    # print("Tab 1: Phrase repo_syncs")
    # print("Tab 2: TransHub affiliate-language")
    
    # # 保持浏览器打开
    # print("浏览器保持打开状态，可以手动切换tab查看不同页面")
    
    return driver

if __name__ == "__main__":
    driver = open_pages_in_tabs("activity-language")
    # 如果需要自动关闭浏览器，取消下面这行的注释
    # driver.quit()
