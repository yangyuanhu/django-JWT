from django.http import JsonResponse
from test1 import jwt_tool

def login(req):
    username = req.POST.get("username")
    password = req.POST.get("password")
    # 模拟登录
    if username == "jerry" and password == "123":
        # 用户标识id
        info = {"user_id":"10086"}
        #生成token
        token = jwt_tool.gen_token(info)
        # 返回数据
        data = {"msg":"登录成功!","token":token,"code":1}
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"msg":"登录失败!","code":-1}, safe=False,)


def get_some_data(req):
    try:
    # 获取token
        token = req.META["HTTP_TOKEN"]
        print(token)
    except:
        return JsonResponse({"msg": "缺少token!"}, safe=False)

    # 解析token获取用户身份信息
    res = jwt_tool.parser_token(token)
    if res["code"] == 1:
        user_id = res["data"]["user_id"]
        return JsonResponse({"msg": "您的id为:%s" % user_id,"data":"一些数据!"}, safe=False)
    else:
        return JsonResponse({"msg": "身份验证失败 请重新登录!"}, safe=False)





