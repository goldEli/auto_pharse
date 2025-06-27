"""
curl 'https://app.phrase.com/accounts/weex-global/projects/activity-backend-language/locales/ru-ru' \
  -H 'accept: */*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
  -b 'language=en; OptanonAlertBoxClosed=2025-06-27T06:14:34.013Z; __hstc=24829477.4a2966fd08420c829906d0c955b36c26.1751004884984.1751004884984.1751004884984.1; hubspotutk=4a2966fd08420c829906d0c955b36c26; _ga=GA1.1.303134808.1751004889; _uetsid=0977a220531e11f086391d29e7b31eaf; _uetvid=0977c180531e11f0ac6c4ff9f104a230; _hjSessionUser_3270412=eyJpZCI6ImI4NmQ3MmRhLWU0YzctNWZiYS1hZDJmLTg0ZTk0NjU2MTM0NSIsImNyZWF0ZWQiOjE3NTEwMDQ4OTI2NzgsImV4aXN0aW5nIjpmYWxzZX0=; _fbp=fb.1.1751004892851.999483891139310622; _gcl_au=1.1.2121443163.1751004888.1134228974.1751004916.1751004916; current_identity=eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqRTNPVGhsTTJVMU4yRmlOREpqWkdRMVl6VmtOVEkwT1dRd01URmxPR1V4SWc9PSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLmN1cnJlbnRfaWRlbnRpdHkifX0%3D--9b872afcd472a07325b905243ff7039268a839a0; current_account=eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqZ3hNelJtTUdOa04yVmhNVGM1WXpJME5tVmlNVFpsTjJKbE5EbGlOekE0SWc9PSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLmN1cnJlbnRfYWNjb3VudCJ9fQ%3D%3D--23639f736b82af47d576d7987fc91952dab8726f; _ga_J2EQJSNGG3=GS2.1.s1751004889$o1$g1$t1751004929$j20$l0$h0; mp_7ee5623b0363d19908a81c8e4e3a62a7_mixpanel=%7B%22distinct_id%22%3A%2219d2ecd7af4719f932079527a44e3857%22%2C%22%24device_id%22%3A%228133761c-59d1-42ce-8da9-b45abe65b251%22%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%2C%22%24user_id%22%3A%2219d2ecd7af4719f932079527a44e3857%22%2C%22Trial%22%3Afalse%2C%22Account%20Code%22%3A%228134f0cd7ea179c246eb16e7be49b708%22%2C%22Account%20Status%22%3A%22paying%22%2C%22Source%22%3A%22Translation%20Center%22%2C%22Scope%22%3A%22Editor%22%2C%22Editor%20Version%22%3A4%2C%22Is%20ICE%22%3Afalse%7D; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jun+27+2025+15%3A42%3A56+GMT%2B0800+(China+Standard+Time)&version=202209.2.0&isIABGlobal=false&hosts=&consentId=4dfe9e7a-2e7c-4979-8a66-96b1232305c6&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=JP%3B12&AwaitingReconsent=false; _phrase_session_sec=I8HQuWQpZWebQ1nWAdNzdIxrIQAUe%2BXzCXhpsUXMycX4tNR15H0Qo4tZ59IZ0cA8PFLQIT6KBI76RsDemcyLxGd50f0pasBagBNz861E0hJ3Jdds5AZ2NbYNXgWGNIO73J2Z%2BOjBin9k4vVXuu%2FHethAJWGlSDP07IWC1gQx4K0aA1e5nChrjMW0S1k8AJFDsGSviBKVyCMLfVt4H5dNFZqcLHOM6A2Jw0%2F6%2Fu8zU3vDR%2BcVUu5XjK0GqRDG%2B4Ef27hf2WDvG%2FPXTaHDNq7rz5qPPfXge7zjmv860NGvHDxoSoUGmvS6YB8SSfHOlRHESv%2BFQLDGU7KJmlTjC8av0qzoZG5eqYEItvp25bnxYiknKZsNQzZwiwjDSyKGtql6u%2F45NvSQ%2BYwxagZckmdQJoyvBGGkaS6wS3kAqSNbeDN0FkvUM5cRal2rmR0Ya0UiAnYzOFNH2le%2Ft8NmwdBOrOndnLJc8a7b6peTsu34%2B7xQJ6r4hK4AJNju5oBUGDmS7NqpauWuu8409yEfHyR0k529VuDPc%2BocELqSvW0Gcemr5B2Wm6VMPnS3%2BsE6a3g3omtBbaWhVovyTxwqfJsqr683aFS0aH0vrbzOs1UjhnL5OBF6G%2FwEx8rh%2Fi9yBg%2FfVA9HbnpF%2B%2FqCY9oJwGmsnQFuW3jr5hBXFt7B2O9A5VbhA%2FQ5XklZpcFDC%2Bt845Q%2BZy2Q4r6bnTVto8UganuK02%2FfBh4pQ95cuE89IRsRMjYHqPchCcN83brGYBuIdXSObA%3D%3D--cBmJV09L7P%2FK06GB--cj37OuYswop8QX5e4rrIcg%3D%3D' \
  -H 'origin: https://app.phrase.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://app.phrase.com/accounts/weex-global/projects/activity-backend-language/locales' \
  -H 'sec-ch-ua: "Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36' \
  -H 'x-csrf-token: 7wsPBp605WGprwmllRt_hJ2btruWQMBP84Zq2j-K4mHhupHtSGYK0YjCiC5k1YZ4AM6muXNIwc7KZk-uD9SFNA' \
  -H 'x-requested-with: XMLHttpRequest' \
  --data-raw '_method=patch&locale%5Bname%5D=ru-RU&locale%5Bcode%5D=ru-RU&locale%5Bis_default%5D=0&locale%5Brtl%5D=0&locale%5Bsource_locale_id%5D=4574879&locale%5Bfallback_locale_id%5D=4574879&locale%5Bis_main%5D=0&locale%5Bunverify_new_translations%5D=0&locale%5Bunverify_updated_translations%5D=0&commit=Save'
"""

import requests
import urllib.parse

def update_locale_settings(locale_id, csrf_token, session_cookie, **kwargs):
    """
    更新locale设置的Python方法
    
    Args:
        locale_id (str): locale的ID，如 'ru-ru'
        csrf_token (str): CSRF token
        session_cookie (str): 完整的session cookie字符串
        **kwargs: 其他参数，如name, code, source_locale_id等
    
    Returns:
        requests.Response: 请求响应对象
    """
    
    # 基础URL
    url = f'https://app.phrase.com/accounts/weex-global/projects/activity-backend-language/locales/{locale_id}'
    
    # 请求头
    headers = {
        'accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://app.phrase.com',
        'priority': 'u=1, i',
        'referer': 'https://app.phrase.com/accounts/weex-global/projects/activity-backend-language/locales',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'x-csrf-token': csrf_token,
        'x-requested-with': 'XMLHttpRequest'
    }
    
    # 默认数据
    default_data = {
        '_method': 'patch',
        'locale[name]': 'ru-RU',
        'locale[code]': 'ru-RU',
        'locale[is_default]': '0',
        'locale[rtl]': '0',
        'locale[source_locale_id]': '4574879',
        'locale[fallback_locale_id]': '4574879',
        'locale[is_main]': '0',
        'locale[unverify_new_translations]': '0',
        'locale[unverify_updated_translations]': '0',
        'commit': 'Save'
    }
    
    # 更新默认数据
    default_data.update(kwargs)
    
    # 解析cookie字符串为字典
    cookies = {}
    for cookie in session_cookie.split('; '):
        if '=' in cookie:
            name, value = cookie.split('=', 1)
            cookies[name] = value
    
    try:
        # 发送请求
        response = requests.patch(
            url,
            headers=headers,
            cookies=cookies,
            data=default_data,
            timeout=30
        )
        
        print(f"请求状态码: {response.status_code}")
        print(f"响应内容: {response.text[:200]}...")  # 只显示前200个字符
        
        return response
        
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None

# 使用示例
if __name__ == "__main__":
    # 这些值需要从浏览器中获取
    csrf_token = "7wsPBp605WGprwmllRt_hJ2btruWQMBP84Zq2j-K4mHhupHtSGYK0YjCiC5k1YZ4AM6muXNIwc7KZk-uD9SFNA"
    session_cookie = "language=en; OptanonAlertBoxClosed=2025-06-27T06:14:34.013Z; __hstc=24829477.4a2966fd08420c829906d0c955b36c26.1751004884984.1751004884984.1751004884984.1; hubspotutk=4a2966fd08420c829906d0c955b36c26; _ga=GA1.1.303134808.1751004889; _uetsid=0977a220531e11f086391d29e7b31eaf; _uetvid=0977c180531e11f0ac6c4ff9f104a230; _hjSessionUser_3270412=eyJpZCI6ImI4NmQ3MmRhLWU0YzctNWZiYS1hZDJmLTg0ZTk0NjU2MTM0NSIsImNyZWF0ZWQiOjE3NTEwMDQ4OTI2NzgsImV4aXN0aW5nIjpmYWxzZX0=; _fbp=fb.1.1751004892851.999483891139310622; _gcl_au=1.1.2121443163.1751004888.1134228974.1751004916.1751004916; current_identity=eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqRTNPVGhsTTJVMU4yRmlOREpqWkdRMVl6VmtOVEkwT1dRd01URmxPR1V4SWc9PSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLmN1cnJlbnRfaWRlbnRpdHkifX0%3D--9b872afcd472a07325b905243ff7039268a839a0; current_account=eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqZ3hNelJtTUdOa04yVmhNVGM1WXpJME5tVmlNVFpsTjJKbE5EbGlOekE0SWc9PSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLmN1cnJlbnRfYWNjb3VudCJ9fQ%3D%3D--23639f736b82af47d576d7987fc91952dab8726f; _ga_J2EQJSNGG3=GS2.1.s1751004889$o1$g1$t1751004929$j20$l0$h0; mp_7ee5623b0363d19908a81c8e4e3a62a7_mixpanel=%7B%22distinct_id%22%3A%2219d2ecd7af4719f932079527a44e3857%22%2C%22%24device_id%22%3A%228133761c-59d1-42ce-8da9-b45abe65b251%22%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%2C%22%24user_id%22%3A%2219d2ecd7af4719f932079527a44e3857%22%2C%22Trial%22%3Afalse%2C%22Account%20Code%22%3A%228134f0cd7ea179c246eb16e7be49b708%22%2C%22Account%20Status%22%3A%22paying%22%2C%22Source%22%3A%22Translation%20Center%22%2C%22Scope%22%3A%22Editor%22%2C%22Editor%20Version%22%3A4%2C%22Is%20ICE%22%3Afalse%7D; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jun+27+2025+15%3A42%3A56+GMT%2B0800+(China+Standard+Time)&version=202209.2.0&isIABGlobal=false&hosts=&consentId=4dfe9e7a-2e7c-4979-8a66-96b1232305c6&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=JP%3B12&AwaitingReconsent=false; _phrase_session_sec=I8HQuWQpZWebQ1nWAdNzdIxrIQAUe%2BXzCXhpsUXMycX4tNR15H0Qo4tZ59IZ0cA8PFLQIT6KBI76RsDemcyLxGd50f0pasBagBNz861E0hJ3Jdds5AZ2NbYNXgWGNIO73J2Z%2BOjBin9k4vVXuu%2FHethAJWGlSDP07IWC1gQx4K0aA1e5nChrjMW0S1k8AJFDsGSviBKVyCMLfVt4H5dNFZqcLHOM6A2Jw0%2F6%2Fu8zU3vDR%2BcVUu5XjK0GqRDG%2B4Ef27hf2WDvG%2FPXTaHDNq7rz5qPPfXge7zjmv860NGvHDxoSoUGmvS6YB8SSfHOlRHESv%2BFQLDGU7KJmlTjC8av0qzoZG5eqYEItvp25bnxYiknKZsNQzZwiwjDSyKGtql6u%2F45NvSQ%2BYwxagZckmdQJoyvBGGkaS6wS3kAqSNbeDN0FkvUM5cRal2rmR0Ya0UiAnYzOFNH2le%2Ft8NmwdBOrOndnLJc8a7b6peTsu34%2B7xQJ6r4hK4AJNju5oBUGDmS7NqpauWuu8409yEfHyR0k529VuDPc%2BocELqSvW0Gcemr5B2Wm6VMPnS3%2BsE6a3g3omtBbaWhVovyTxwqfJsqr683aFS0aH0vrbzOs1UjhnL5OBF6G%2FwEx8rh%2Fi9yBg%2FfVA9HbnpF%2B%2FqCY9oJwGmsnQFuW3jr5hBXFt7B2O9A5VbhA%2FQ5XklZpcFDC%2Bt845Q%2BZy2Q4r6bnTVto8UganuK02%2FfBh4pQ95cuE89IRsRMjYHqPchCcN83brGYBuIdXSObA%3D%3D--cBmJV09L7P%2FK06GB--cj37OuYswop8QX5e4rrIcg%3D%3D"
    
    # 调用方法
    response = update_locale_settings(
        locale_id='ru-ru',
        csrf_token=csrf_token,
        session_cookie=session_cookie,
        # 可以覆盖默认参数
        # 'locale[name]': 'en-US',
        # 'locale[code]': 'en-US'
    )