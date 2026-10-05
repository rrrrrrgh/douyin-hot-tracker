import requests
import json

def fetch_douyin_hot():
    url = "https://uapis.cn/api/v1/misc/hotboard?type=douyin"
    body = ""
    hot_list = []
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
        hot_list = data.get('data', [])
        if not hot_list:
            body = "今日热榜抓取失败：API返回的数据列表为空。\n"
        else:
            body = "今日抖音热榜（数据来源：uapis.cn）：\n\n"
            for i, item in enumerate(hot_list[:20], 1):
                title = item.get('title', '未知标题')
                hot_value = item.get('hot_value', '')
                body += f"{i}. {title}  (热度: {hot_value})\n"
    except Exception as e:
        body = f"今日热榜抓取失败，错误信息：{e}\n"
        hot_list = []
    
    # 无论成功或失败，都创建文件
    with open('email_body.txt', 'w', encoding='utf-8') as f:
        f.write(body)
    with open('douyin_hot.json', 'w', encoding='utf-8') as f:
        json.dump(hot_list, f, ensure_ascii=False, indent=2)
    
    print("抓取完成，文件已生成。")

if __name__ == "__main__":
    fetch_douyin_hot()
