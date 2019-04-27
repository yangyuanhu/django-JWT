
import hashlib,time
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import  itsdangerous

# 用一个值作为密钥 当然你可以用任何的字符串作为密钥 越复杂越安全
secret_key = "548D859ADA8B084E76730CCEFA052EE1"

# 除去密钥外 再添加一个盐值来提高安全性
salt_str = "this is salt string"

expires_in = 3600 # 控制token的过期有效市场 默认为3600



def gen_token(data):
    data["iat"] = time.time()
    s = Serializer(secret_key=secret_key,expires_in=expires_in,salt=salt_str,)
    token = s.dumps(data).decode("utf-8")
    return token


def parser_token(token):
    s = Serializer(secret_key=secret_key,salt=salt_str)
    try:
        return {"msg":"解析成功","code":1,"data":s.loads(token)}
    except itsdangerous.SignatureExpired:
        return {"msg":"token已过期请重新登录","code":-1}
    except itsdangerous.BadSignature as e:
        if e.payload:
            try:
                s = s.load_payload(e.payload)
                print(s)
                return {"msg": "secret_key 和 salt可能已经泄露", "code": -1}
            except:pass
        return {"msg": "token被篡改", "code": -1}
    except:
        return {"msg": "解析失败 未知原因!", "code": -1}

if __name__ == '__main__':
    token = gen_token({"user_id":1})
    data = parser_token(token)
    print(data)














