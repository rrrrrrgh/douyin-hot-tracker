import requests
import json

def fetch_douyin_hot():
    # 抖音官方热搜接口（网页版实际调用的 API）
    url = "https://www.douyin.com/aweme/v1/web/hot/search/list/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://www.douyin.com/",
        "Accept": "application/json, text/plain, */*",
    }
    
    body = ""
    hot_list = []
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        # 抖音官方接口的数据在 data.word_list 里
        word_list = data.get('data', {}).get('word_list', [])
        
        if not word_list:
            body = "今日热榜抓取失败：抖音接口返回的数据列表为空。\n"
        else:
            body = "今日抖音热榜（数据来源：抖音官方）：\n\n"
            for i, item in enumerate(word_list[:20], 1):
                title = item.get('word', '未知标题')
                hot_value = item.get('hot_value', '')
                body += f"{i}. {title}  (热度: {hot_value})\n"
            hot_list = word_list
            
    except Exception as e:
        body = f"今日热榜抓取失败，错误信息：{e}\n"
        hot_list = []
    
    # 无论成功或失败，都创建文件
    with open('email_body.txt', 'w', encoding='utf-8') as f:
        f.write(body)
    with open('douyin_hot.json', 'w', encoding='utf-8') as f:
        json.dump(hot_list, f, ensure_ascii=False, indent=2)
    
    print(f"抓取完成，共获取 {len(hot_list)} 条数据。")

if __name__ == "__main__":
    fetch_douyin_hot()
