# simulate open browser https://app.phrase.com/accounts/weex-global/projects/activity-backend-language/locales using selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
with open('config.json', 'r') as f:
    config = json.load(f)

phrase_project_url = config['phrase_project_url']


locales_list = [
    # en-US
    {
        "locale": "es-US",
        "names": ["en-us", "en-US", "en_us", "en_US", "en", "esUS"],
    },
    # zh-CN
    {
        "locale": "zh-CN",
        "names": ["zh-cn", "zh-CN", "zh_cn", "zh_CN", "zhCN", "zh"],
    },
    # zh-TW
    {
        "locale": "zh-TW",
        "names": ["zh-tw", "zh-TW", "zh_tw", "zh_TW", "zh_tw", "zhTW"],
    },
    # ko
    {
        "locale": "Korean - ko",
        "names": ["ko", "ko-KR", "ko-kr", "ko_KR", "ko_kr", "koKR"],
    },
    # ja
    {
        "locale": "Japanese - ja",
        "names": ["ja", "ja-JP", "ja-jp", "ja_JP", "ja_jp", "jaJP"],
    },
    # vi
    {
        "locale": "Vietnamese - vi",
        "names": ["vi", "vi-VN", "vi-vn", "vi_VN", "vi_vn", "viVN"],
    },
    # fa-IR
    {
        "locale": "fa-IR",
        "names": ["fa-IR", "fa-ir", "fa_IR", "fa_ir", "faIR", "fa"],
    },
    # ar
    {
        "locale": "Arabic - ar",
        "names": ["ar", "ar-SA", "ar-sa", "ar_SA", "ar_sa", "arSA"],
    },
    # tr
    {
        "locale": "Turkish - tr",
        "names": ["tr", "tr-TR", "tr-tr", "tr_TR", "tr_tr", "trTR"],
    },
    {
        "locale": "English, Turkey - en-TR",
        "names": ["en-tr", "en_tr", "en_TR", "en_tr", "enTR"],
    },
    # de
    {
        "locale": "German - de",
        "names": ["de", "de-DE", "de-de", "de_DE", "de_de", "deDE"],
    },
    # fr
    {
        "locale": "French - fr",
        "names": ["fr", "fr-FR", "fr-fr", "fr_FR", "fr_fr", "frFR"],
    },
    # it
    {
        "locale": "Italian - it",
        "names": ["it", "it-IT", "it-it", "it_IT", "it_it", "itIT"],
    },
    # es-es
    {
        "locale": "es-ES",
        "names": ["es-es", "es-ES", "es-es", "es_es", "es_ES", "esES"],
    },
    # es-419
    {
        "locale": "es-419",
        "names": ["es-419", "es", "es_419", "es_419", "es_419", "es419"],
    },
    # pl
    {
        "locale": "Polish - pl",
        "names": ["pl", "pl-PL", "pl-pl", "pl_PL", "pl_pl", "plPL"],
    },
    # ru
    {
        "locale": "Russian - ru",
        "names": ["ru", "ru-RU", "ru-ru", "ru_RU", "ru_ru", "ruRU"],
    },
    # uk
    {
        "locale": "Ukrainian - uk",
        "names": ["uk", "uk-UA", "uk-ua", "uk_UA", "uk_ua", "ukUA"],
    },
    # pt-BR
    {
        "locale": "pt-BR",
        "names": ["pt-br", "pt-BR", "pt_br", "pt_BR", "ptBR"],
    }
]

def process_locale_page(driver, page_url, page_name, source="en-US"):
    """
    处理单个locale页面的操作
    
    Args:
        driver: WebDriver实例
        page_url: 页面URL
        page_name: 页面名称（用于日志）
        source: 源语言（默认en-US）
    """
    print(f"\n开始处理{page_name}页面...{source}")
    driver.get(page_url)
    time.sleep(3)

    # 等待页面加载
    wait = WebDriverWait(driver, 10)

    try:
        # 1. 获取 class 为 syn_dropdown__content syn_dropdown-menu__dropdown hidden 的元素
        # elements = driver.find_elements(By.CSS_SELECTOR, ".pa-list-items .syn_dropdown__content.syn_dropdown-menu__dropdown.hidden")
        # 等待所有符合条件的元素出现在 DOM 中（不一定可见）
        elements = wait.until(EC.presence_of_all_elements_located((
            By.CSS_SELECTOR,
            ".pa-list-items .syn_dropdown__content.syn_dropdown-menu__dropdown.hidden"
        )))
        
        print(f"{page_name}页面找到 {len(elements)} 个符合条件的元素")
        
        # 2. 循环元素
        for i in range(len(elements)):
            try:
                print(f"处理{page_name}页面第 {i+1} 个元素")
                
                textElements = driver.find_elements(By.CSS_SELECTOR, ".index-translations-link")
                print(f"找到 {len(textElements)} 个符合条件的元素")
                second_element_text = textElements[i].text.strip()
                target_values = ['zh-cn', 'zh-CN', 'en-US', 'en-us', 'en', 'zh-TW', 'zh-tw']
            
                isEmpty = second_element_text in target_values
                
                # 重新查找当前索引的元素，避免stale element reference
                # elements = driver.find_elements(By.CSS_SELECTOR, ".pa-list-items .syn_dropdown__content.syn_dropdown-menu__dropdown.hidden")

                elements = wait.until(EC.presence_of_all_elements_located((
                    By.CSS_SELECTOR,
                    ".pa-list-items .syn_dropdown__content.syn_dropdown-menu__dropdown.hidden"
                )))

                if i < len(elements):
                    current_element = elements[i]
                    print(current_element)
                    
                    # 3. 模拟鼠标mouseenter事件
                    driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('mouseenter', {bubbles: true}));", current_element)
                    print(f"已对{page_name}页面第 {i+1} 个元素执行mouseenter事件")
                    
                    # 等待一下让DOM更新
                    # time.sleep(0.5)
                    
                    # 在element下点击class为'syn_dropdown-menu__dropdown-list'的ul元素中的第三个a标签
                    dropdown_list = current_element.find_element(By.CSS_SELECTOR, "ul.syn_dropdown-menu__dropdown-list")
                    third_link = dropdown_list.find_elements(By.TAG_NAME, "a")[2]  # 获取第三个a标签（索引为2）
                    third_link.click()
                    print(f"已点击{page_name}页面第 {i+1} 个元素的第三个a标签")

                    time.sleep(3)

                    # 获取 input name , xpath： //*[@id="locale_name"]
                    input_locale_element = driver.find_element(By.XPATH, "//*[@id='locale_name']")
                    input_locale_element_value = input_locale_element.get_attribute("value")
                    print(f"input_locale_element_value: {input_locale_element_value}")

                    # time.sleep(2)
                    # get language locale from locales_list, names includes input_locale_element_value

                    language_locale = next((locale for locale in locales_list if input_locale_element_value in locale["names"]), None)

                    if language_locale:
                        print(f"language_locale: {language_locale}")
                    else:
                        # 报错 并退出程序
                        print(f"language_locale not found: {input_locale_element_value}")
                        raise Exception(f"language_locale not found: {input_locale_element_value}") 
                        continue


                    # ---------------------------------

                    # click select, xpath://*[@id="general"]/div[2]/div/div[1]

                    # select_element = wait.until(
                    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="general"]/div[2]/div/div[1]'))
                    # )
                    # select_element.click()

                    # # input //*[@id="general"]/div[2]/div/div[1]/input
                    # input_element = wait.until(
                    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="general"]/div[2]/div/div[1]/input'))
                    # )
                    # input_element.clear()
                    # # input_element.send_keys(language_locale["locale"])
                    # input_element.send_keys("")
                    # input_element.send_keys(Keys.RETURN)

                    # time.sleep(1)


                    select_element = wait.until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="general"]/div[2]/div/div[1]'))
                    )
                    select_element.click()

                    # input //*[@id="general"]/div[2]/div/div[1]/input
                    input_element = wait.until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="general"]/div[2]/div/div[1]/input'))
                    )
                    input_element.clear()
                    input_element.send_keys(language_locale["locale"])
                    # input_element.send_keys("")
                    # input_element.send_keys(Keys.RETURN)
                    # //*[@id="general"]/div[2]/div/div[2]/div/div[1]
                    select_element_2 = wait.until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="general"]/div[2]/div/div[2]/div/div[1]'))
                    )
                    select_element_2.click()




                    # 点击 value 为 'save' 的 input 元素
                    try:
                        # //*[@id="locale_form"]/div/div/div/div[3]/input
                        # save_button = wait.until(
                        #     EC.element_to_be_clickable((By.XPATH, '//*[@id="locale_form"]/div/div/div/div[3]/input'))
                        # )
                        # save_button.click()
                        # print(f"已点击{page_name}页面 save 按钮")
                        print(f" 开始 save : {page_name}")
                        time.sleep(1)

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
                    # 退出
                    raise Exception(f"{page_name}页面第 {i+1} 个元素不存在，跳过")
                    continue

            except Exception as e:
                print(f"处理{page_name}页面第 {i+1} 个元素时出错: {e}")
                raise Exception(f"处理{page_name}页面第 {i+1} 个元素时出错: {e}")
                continue

    except Exception as e:
        print(f"{page_name}页面执行过程中出错: {e}")
        raise Exception(f"{page_name}页面执行过程中出错: {e}")

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
    {
        "url": phrase_project_url + "affiliate-language/locales",
        "name": "affiliate-language",
        "source": "en"
    },
    {
        "url": phrase_project_url + "asset-language/locales",
        "name": "asset-language",
        "source": "en-US"
    },
    {
        "url": phrase_project_url + "gateway-language/locales",
        "name": "gateway-language",
        "source": "en-US"
    },
    {
        "url": phrase_project_url + "mix-language/locales",
        "name": "mix-language",
        "source": "en-US"
    },
    {
        "url": phrase_project_url + "msg-language/locales",
        "name": "msg-language",
        "source": "en-US"
    },
    {
        "url": phrase_project_url + "new-trace-language/locales",
        "name": "new-trace-language",
        "source": "en-US"
    },
    {
        "url": phrase_project_url + "spot-language/locales",
        "name": "spot-language",
        "source": "en-US"
    },
    {
        "url": phrase_project_url + "unimargin-language/locales",
        "name": "unimargin-language",
        "source": "en-US"
    },
    {
        "url": phrase_project_url + "user-language/locales",
        "name": "user-language",
        "source": "en-US"
    },
    {
        "url": phrase_project_url + "web-language/locales",
        "name": "web-language",
        "source": "en"
    },
    {
        "url": phrase_project_url + "trade-language/locales",
        "name": "trade-language",
        "source": "en"

    },
    {
        "url": phrase_project_url + "web-pages-language/locales",
        "name": "web-pages-language",
        "source": "en"
    },
    {
        "url": phrase_project_url + "activity-backend-language/locales",
        "name": "activity-backend-language",
        "source": "en-US"
    },
    {
        "url": phrase_project_url + "activity-language/locales",
        "name": "activity-language",
        "source": "en"
    },

    {
        "url": phrase_project_url + "app-language/locales",
        "name": "app-language",
        "source": "en_US"
    },
]

# 处理所有页面
for page in pages_to_process:
    process_locale_page(driver, page["url"], page["name"], page["source"])

print("所有页面操作完成，浏览器保持打开状态")
# 如果需要自动关闭浏览器，取消下面这行的注释
# driver.quit()

