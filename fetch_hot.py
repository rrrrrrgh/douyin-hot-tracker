import requests
import json

def fetch_douyin_hot():
    # 使用免费的公开热榜 API（数据源来自抖音热榜）
    url = "https://api.vvhan.com/api/hotlist/douyinHot"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        # 提取热榜列表
        hot_list = data.get('data', [])
        
        # 保存为 JSON 文件用于附件
        with open('douyin_hot.json', 'w', encoding='utf-8') as f:
            json.dump(hot_list, f, ensure_ascii=False, indent=2)
        
        # 生成邮件正文
        body = "今日抖音热榜（抓取时间：请注意时差）：\n\n"
        for i, item in enumerate(hot_list[:20], 1):
            title = item.get('title', '未知标题')
            body += f"{i}. {title}\n"
        
        with open('email_body.txt', 'w', encoding='utf-8') as f:
            f.write(body)
            
        print("抓取成功！")
    except Exception as e:
        print(f"抓取失败: {e}")
        raise

if __name__ == "__main__":
    fetch_douyin_hot()
