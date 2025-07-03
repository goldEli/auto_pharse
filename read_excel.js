const { readExcelFirstColumn } = require('./libs/excel_reader');

// 读取Excel文件的第一列数据
const filePath = './data/Hidden keys on Crowdin (Web).xlsx';

console.log('开始读取Excel文件...');
const firstColumnData = readExcelFirstColumn(filePath);

const list = []

if (firstColumnData.length > 0) {
    console.log('\n第一列数据:');
    firstColumnData.forEach((item, index) => {
        // console.log(`${index + 1}. ${item}`);
        list.push(item)
    });

    console.log(`\n总共读取到 ${firstColumnData.length} 条数据`);
} else {
    console.log('没有读取到任何数据');
}

async function update_key(key) {
    const res = fetch("https://app.phrase.com/accounts/weex-global/projects/web-language/keys/6a2da70f863ecdf457b50860a21e2f0c", {
        "headers": {
            "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
            "accept-language": "en,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-csrf-token": "K93BsOoQG-Y7_zfZlKONbtlqbEWIK5CvUoccrGnS_t9AjmgDlq44wEJHilxjwaZGIPvpWnQXtc5RfrVW3V_9UA",
            "x-requested-with": "XMLHttpRequest",
            "cookie": "OptanonAlertBoxClosed=2025-04-07T09:31:30.264Z; hubspotutk=94a6cf11465e07a2d7d797b9e9d7014d; _fbp=fb.1.1744018294586.913929660835416247; __adroll_fpc=19367fda3c8748ee02ed94f27c3c91da-1744781378459; language=en; _hjSessionUser_3270412=eyJpZCI6IjcwMTY5MTY4LWM3ZWItNTQ5Yy04ZjRhLWNkMTY5ZjIxZWExNSIsImNyZWF0ZWQiOjE3NDQwMTgyOTQyNDcsImV4aXN0aW5nIjp0cnVlfQ==; current_account=eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqZ3hNelJtTUdOa04yVmhNVGM1WXpJME5tVmlNVFpsTjJKbE5EbGlOekE0SWc9PSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLmN1cnJlbnRfYWNjb3VudCJ9fQ%3D%3D--23639f736b82af47d576d7987fc91952dab8726f; intercom-id-qnzpmkdl=591c0135-dde8-44e9-b402-b3d9549c197e; intercom-device-id-qnzpmkdl=38c71023-20ce-4e44-b90d-5d71f4de455a; _hjSessionUser_5097121=eyJpZCI6ImIxNDE1Y2VlLWI5YzEtNTlkOC05YmZlLWYxZDBhOWFhMGQzNSIsImNyZWF0ZWQiOjE3NDQ4NTI5MjU0MjIsImV4aXN0aW5nIjp0cnVlfQ==; _clck=14plpfz%7C2%7Cfx9%7C0%7C1937; intercom-session-qnzpmkdl=; _uetvid=180ee2e0139311f0b74799af779eb9bc; _gcl_au=1.1.79869147.1744018291.516511742.1751419565.1751419631; current_identity=eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqRTNPVGhsTTJVMU4yRmlOREpqWkdRMVl6VmtOVEkwT1dRd01URmxPR1V4SWc9PSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLmN1cnJlbnRfaWRlbnRpdHkifX0%3D--9b872afcd472a07325b905243ff7039268a839a0; _ga_J2EQJSNGG3=GS2.1.s1751419429$o16$g1$t1751419854$j60$l0$h0; _gid=GA1.2.591017033.1751420450; __hstc=24829477.94a6cf11465e07a2d7d797b9e9d7014d.1744018294498.1751419431776.1751439582170.15; _clsk=1ksrji2%7C1751449279333%7C1%7C1%7Cj.clarity.ms%2Fcollect; _ga=GA1.1.239268067.1744018291; _ga_KGJ9S35JX0=GS2.1.s1751506315$o10$g0$t1751506315$j60$l0$h0; _ga_K43BDZYM18=GS2.1.s1751506315$o16$g0$t1751506315$j60$l0$h0; _hjSession_3270412=eyJpZCI6IjRhMGMyZDcyLWViZjYtNDVmNy05ZjI4LTNiOWUwMzBmYWZmNCIsImMiOjE3NTE1MjE4MDI3NTksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; ph_phc_TXdpocbGVeZVm5VJmAsHTMrCofBQu3e0kN8HGMNGTVW_posthog=%7B%22distinct_id%22%3A%220197c4d9-290d-7958-99dd-5cdf77a53746%22%2C%22%24sesid%22%3A%5B1751521879741%2C%220197ced5-b09d-7175-9805-a396cdacc70b%22%2C1751521800349%5D%7D; mp_7ee5623b0363d19908a81c8e4e3a62a7_mixpanel=%7B%22distinct_id%22%3A%2219d2ecd7af4719f932079527a44e3857%22%2C%22%24device_id%22%3A%225fb4cb1e-b22a-4f5d-b242-f7c3b0955721%22%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%2C%22%24user_id%22%3A%2219d2ecd7af4719f932079527a44e3857%22%2C%22Trial%22%3Afalse%2C%22Account%20Code%22%3A%228134f0cd7ea179c246eb16e7be49b708%22%2C%22Account%20Status%22%3A%22paying%22%2C%22Source%22%3A%22Translation%20Center%22%2C%22Scope%22%3A%22Editor%22%2C%22Editor%20Version%22%3A4%2C%22Is%20ICE%22%3Afalse%7D; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jul+03+2025+14%3A17%3A05+GMT%2B0800+(China+Standard+Time)&version=202209.2.0&isIABGlobal=false&hosts=&consentId=41bbf510-667c-4c2b-af0f-dd7e173ab700&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=JP%3B12&AwaitingReconsent=false; _phrase_session_sec=gCwvZew8R5%2FWyN3q4bsi%2FSXYRpvkquFdbyuygqIIc0HhxburS3rmzJgje5PmOezNm5Ww5E1ovMcr7lPCHYE%2FJ0y65SLX8yKD6cyZoGVTGyPUtfkgC5kQklUP4cuoEKOxwqCOYL1oxv6GJ8bxQmOMmHKcUvIyAitX0RLtXEQ5OhuMUyHH%2FbvdF2l9GUfpkkXuTbEpwZPgnPCBHgxyIR7Tu8qab7kSJq0w9pBZsziwB8cfGYpuMmppus1FpQOoVwLRjq%2Bi2G2GLA92S65KjyflLsOrtCgytwJA01LvXhOjzt%2F7c9zVdHdl8rNWgMZ8CRxoLj59jj6A4fRo0oalCepVkn1BDOIm9x%2B42CnVJUroSM1H7d70f7KpeWgKGIKA6N%2FVonv1Rg8sC6FYvc3nn%2BnNBLPoDtpUisfnMcKXVNbVCdFvaO1PIO2AjdRJ9DuoVxcPUIlWbUXqmVx6wnh9Xz50gxzciOsky3GQgn1qOmorYUr%2BeTb1dNxNRhDGOPvUd2Fo1UnBWyxYcXQD8XXlV1rUCq24ZwD5iilC3GlmgZG%2BI9zToZQCYt2hxSQM%2FoxJTI%2BYGNPcQeBWRVmi%2FihUx%2BItjb4sdBZK3nUYj%2FEwkcoCsdeEAXnFMGHDQjwNNngPvKzaExadMK7F%2Fmgwz5DpXeKPJ8K8z59FcD4xZfTpcRvJxHlJjzg0VlvMzAeaIp1MRveQfA7cJK5e%2F0%2FE5epuAmgzHmJNdAZ4DpUGfMP9vOFRJ2AePGOgfFzX1wgXix1g2cb4hQ%3D%3D--KrCZ3gT8oOduP6cL--TPEUgEVzFY0aGk75ooOzag%3D%3D",
            "Referer": `https://app.phrase.com/accounts/weex-global/projects/web-language/keys?translation_key_search%5Bquery%5D=${key}&commit=Create+Translation+key+search`,
            "Referrer-Policy": "strict-origin-when-cross-origin"
        },
        "body": `_method=patch&scope=&screenshot_marker_id=&original_translation_key_id=&translation_key%5Bname%5D=${key}&translation_key%5Bdescription%5D=&translation_key%5Bexcluded_in_locales%5D%5B%5D=2c5df130502468bb56c0af6b13ae2a7c&translation_key%5Bexcluded_in_locales%5D%5B%5D=4380db9ef5d33c2041423553568ff4a2&translation_key%5Bexcluded_in_locales%5D%5B%5D=dc2160578ccc3752fbeb1668c4fb7293&translation_key%5Bexcluded_in_locales%5D%5B%5D=fc7cb42f867778a29962b4599a0f2d2a&translation_key%5Bexcluded_in_locales%5D%5B%5D=2692f7fe7a92210c34bb262cd429d594&translation_key%5Bexcluded_in_locales%5D%5B%5D=93bbad51303d8ef448074e323b5f76f9&translation_key%5Bexcluded_in_locales%5D%5B%5D=4f6963203a57bd85f9c655f6933585ba&translation_key%5Bexcluded_in_locales%5D%5B%5D=da86a54caa08526b7057961a33967731&translation_key%5Bexcluded_in_locales%5D%5B%5D=f0359452f94b49b4ed35519d1f270e95&translation_key%5Bexcluded_in_locales%5D%5B%5D=0d3a6dfc57d2fbdeb84b41e56e0423c9&translation_key%5Bexcluded_in_locales%5D%5B%5D=c89c1e440d45a16d5cd4a6c2fb59d4b9&translation_key%5Bexcluded_in_locales%5D%5B%5D=d3d8924ff42c485376fc60f4d4586d93&translation_key%5Bexcluded_in_locales%5D%5B%5D=e0e1348470cf82929438fe4a4c7cc9af&translation_key%5Bexcluded_in_locales%5D%5B%5D=e12f4039d961b8f4df1ee40ceaa82863&translation_key%5Bexcluded_in_locales%5D%5B%5D=c469ed5b091c1de2e38c7d1de2500067&translation_key%5Bis_plural%5D=0&translation_key%5Bplural_form_type%5D=cardinal&translation_key%5Bname_plural%5D=&translation_key%5Bmax_characters_allowed%5D=0&translation_key%5Bdata_type%5D=string&translation_key%5Bunformatted%5D=0&translation_key%5Bxml_space_preserve%5D=0`,
        "method": "POST"
    });

    return res.then(res => {
        const status = res.status
        console.log(`${key} ${status}`)
        if (status != 200) {
            console.log(`${key} 更新失败`)
            console.log(res)
        }

    }).catch(err => {
        console.log(err)
    })

}

// console.log(list)
// for (const key of list) {
//     update_key(key)
// }

function wait(ms) {
    return new Promise(resolve => setTimeout(resolve, ms))
}

async function main() {
    for (let i = 0; i < 2; i++) {
        await update_key(list[i].trim())
        await wait(2000)
    }

}

main()
