# 请右键直接运行该文件
import requests

# 模拟登录
resp = requests.post("http://127.0.0.1:8000/login/",data={"username":"jerry","password":"123"})
res = resp.json()


# 取出返回的token
token = None
if res["code"] == 1:
    print("登录成功!")
    token = res["token"]
else:
    print("登录失败!")

# 请求数据接口
resp1 = requests.get("http://127.0.0.1:8000/get_some_data/",headers={"token":token})
print(resp1.json())










