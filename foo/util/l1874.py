import requests

# 定义请求类型
type = 'evm'
url = f"https://api-bot-v1.dbotx.com/account/wallets?type={type}"
headers = {
    "X-API-KEY": "jmtt41jaowbeckrrvzegxowjnmvf43jv"
}

try:
    # 发送HTTP GET请求
    response = requests.get(url, headers=headers)
    # 检查响应状态码
    response.raise_for_status()  # 如果状态码不是200，会引发HTTPError异常
    # 打印JSON格式的响应
    print(response.json())
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as err:
    print(f"Error occurred: {err}")