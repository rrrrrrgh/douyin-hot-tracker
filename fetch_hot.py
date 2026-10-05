import requests
import json

def fetch_douyin_hot():
    # 更换为 uapis.cn 的免费热榜接口
    url = "https://uapis.cn/api/v1/misc/hotboard?type=douyin"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status() # 检查HTTP错误
        data = response.json()
        
        # uapis.cn 返回的数据中，热榜列表在 'data' 字段里
        hot_list = data.get('data', [])
        
        if not hot_list:
            print("警告: API返回的数据列表为空")
            return

        # 保存为 JSON 文件用于附件
        with open('douyin_hot.json', 'w', encoding='utf-8') as f:
            json.dump(hot_list, f, ensure_ascii=False, indent=2)
        
        # 生成邮件正文
        body = "今日抖音热榜（数据来源：uapis.cn）：\n\n"
        for i, item in enumerate(hot_list[:20], 1):
            title = item.get('title', '未知标题')
            hot_value = item.get('hot_value', '')
            body += f"{i}. {title}  (热度: {hot_value})\n"
        
        with open('email_body.txt', 'w', encoding='utf-8') as f:
            f.write(body)
            
        print(f"抓取成功！共获取 {len(hot_list)} 条数据")
    except Exception as e:
        print(f"抓取失败: {e}")
        # 写入一个空的邮件正文，避免后续步骤因文件不存在而报错
        with open('email_body.txt', 'w', encoding='utf-8') as f:
            f.write("今日热榜抓取失败，请检查GitHub Actions日志。")
        with open('douyin_hot.json', 'w', encoding='utf-8') as f:
            json.dump([], f)
        raise

if __name__ == "__main__":
    fetch_douyin_hot()
