# simulate open browser https://app.phrase.com/accounts/weex-global/projects/activity-backend-language/locales using selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

def process_locale_page(driver, page_url, page_name, source="en-US"):
    """
    处理单个locale页面的操作
    
    Args:
        driver: WebDriver实例
        page_url: 页面URL
        page_name: 页面名称（用于日志）
        source: 源语言（默认en-US）
    """
    print(f"\n开始处理{page_name}页面...")
    driver.get(page_url)
    time.sleep(3)

    # 等待页面加载
    wait = WebDriverWait(driver, 10)

    try:
        # 1. 获取 class 为 syn_dropdown__content syn_dropdown-menu__dropdown hidden 的元素
        elements = driver.find_elements(By.CSS_SELECTOR, ".pa-list-items .syn_dropdown__content.syn_dropdown-menu__dropdown.hidden")
        
        print(f"{page_name}页面找到 {len(elements)} 个符合条件的元素")
        
        # 2. 循环元素
        for i in range(len(elements)):
            try:
                print(f"处理{page_name}页面第 {i+1} 个元素")
                if i < 2:
                    continue
                
                textElements = driver.find_elements(By.CSS_SELECTOR, ".index-translations-link")
                print(f"找到 {len(textElements)} 个符合条件的元素")
                second_element_text = textElements[i].text.strip()
                target_values = ['zh-cn', 'zh-CN', 'en-US', 'en-us', 'en', 'zh-TW', 'zh-tw']
            
                isEmpty = second_element_text in target_values
                
                # 重新查找当前索引的元素，避免stale element reference
                current_elements = driver.find_elements(By.CSS_SELECTOR, ".pa-list-items .syn_dropdown__content.syn_dropdown-menu__dropdown.hidden")
                if i < len(current_elements):
                    current_element = current_elements[i]
                    print(current_element)
                    
                    # 3. 模拟鼠标mouseenter事件
                    driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('mouseenter', {bubbles: true}));", current_element)
                    print(f"已对{page_name}页面第 {i+1} 个元素执行mouseenter事件")
                    
                    # 等待一下让DOM更新
                    time.sleep(0.5)
                    
                    # 在element下点击class为'syn_dropdown-menu__dropdown-list'的ul元素中的第三个a标签
                    dropdown_list = current_element.find_element(By.CSS_SELECTOR, "ul.syn_dropdown-menu__dropdown-list")
                    third_link = dropdown_list.find_elements(By.TAG_NAME, "a")[2]  # 获取第三个a标签（索引为2）
                    third_link.click()
                    print(f"已点击{page_name}页面第 {i+1} 个元素的第三个a标签")

                    time.sleep(3)

                    # click a markup with href="#advanced"
                    advanced_element = driver.find_element(By.CSS_SELECTOR, "a[href='#advanced']")
                    advanced_element.click()
                    print(f"已点击{page_name}页面第 {i+1} 个元素的 advanced_element")

                    time.sleep(1)

                    # 查找两组 selectize-input 元素
                    selectize_inputs = driver.find_elements(By.CSS_SELECTOR, "div.selectize-input.items.has-options")
                    print(f"找到 {len(selectize_inputs)} 个 selectize-input 元素")

                    # 处理两组 selectize-input 元素
                    for j in range(len(selectize_inputs)):
                        try:
                            print(f"处理{page_name}页面第 {j+1} 个 selectize-input 元素")
                            
                            # 重新查找元素，避免stale element reference
                            current_selectize_inputs = driver.find_elements(By.CSS_SELECTOR, "div.selectize-input.items.has-options")

                            if j < len(current_selectize_inputs):
                                selectize_input = current_selectize_inputs[j]
                                
                                # 点击 selectize-input div
                                selectize_input.click()
                                print(f"已点击{page_name}页面第 {j+1} 个 selectize-input")
                                
                                time.sleep(0.5)

                                txt = "en-US"
                                if isEmpty:
                                    txt = ""
                                
                                # 找到儿子 input 元素并输入 en-US
                                input_element = selectize_input.find_element(By.TAG_NAME, "input")
                                input_element.clear()
                                input_element.send_keys(txt)
                                input_element.send_keys(Keys.RETURN)
                                print(f"已在{page_name}页面第 {j+1} 个 input 中输入 {txt} 并回车")
                                
                                time.sleep(2)
                            else:
                                print(f"{page_name}页面第 {j+1} 个 selectize-input 元素不存在")
                                
                        except Exception as e:
                            print(f"处理{page_name}页面第 {j+1} 个 selectize-input 时出错: {e}")
                            continue

                    # 点击 value 为 'save' 的 input 元素
                    try:
                        # 使用显式等待确保元素可用
                        save_button = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Save']"))
                        )
                        save_button.click()
                        print(f"已点击{page_name}页面 save 按钮")
                        time.sleep(1)
                    except Exception as e:
                        print(f"点击{page_name}页面 save 按钮时出错: {e}")

                    # click a markup with href="#advanced"

                    # click a markup with href="#advanced"
                    
                    # 等待一下再进行下一个操作
                    print(f"等待3秒 等待{page_name}页面下一个元素")
                    time.sleep(3)
                else:
                    print(f"{page_name}页面第 {i+1} 个元素不存在，跳过")
                    continue

            except Exception as e:
                print(f"处理{page_name}页面第 {i+1} 个元素时出错: {e}")
                continue

    except Exception as e:
        print(f"{page_name}页面执行过程中出错: {e}")

    print(f"{page_name}页面操作完成")

# 主程序
options = Options()
# 设置用户数据目录路径，使用已有的浏览器配置（如已登录）
options.add_argument("user-data-dir=/Users/eli/Documents/selenium")

# 尝试连接到已存在的Chrome实例，如果不存在则创建新的
try:
    # 尝试连接到已存在的Chrome实例
    driver = webdriver.Chrome(options=options)
    # 如果成功连接，新开一个tab
    driver.execute_script("window.open('');")
    # 切换到新开的tab
    driver.switch_to.window(driver.window_handles[-1])
    print("已连接到现有浏览器并新开tab")
except Exception as e:
    # 如果连接失败，创建新的浏览器实例
    driver = webdriver.Chrome(options=options)
    print("创建了新的浏览器实例")

# 定义要处理的页面列表
pages_to_process = [
    # {
    #     "url": "https://app.phrase.com/accounts/weex-global/projects/activity-backend-language/locales",
    #     "name": "activity-backend-language",
    #     "source": "en-US"
    # },
    # {
    #     "url": "https://app.phrase.com/accounts/weex-global/projects/test/locales",
    #     "name": "test"
    # },
    {
        "url": "https://app.phrase.com/accounts/weex-global/projects/activity-language/locales",
        "name": "activity-language",
    }
    # 可以继续添加更多页面
]

# 处理所有页面
for page in pages_to_process:
    process_locale_page(driver, page["url"], page["name"], page["source"])

print("所有页面操作完成，浏览器保持打开状态")
# 如果需要自动关闭浏览器，取消下面这行的注释
# driver.quit()

