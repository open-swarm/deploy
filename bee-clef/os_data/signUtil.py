#!/usr/bin/env python2.7
# coding:utf-8

import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA, MD5
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5




TEST_PRIKEY = '''-----BEGIN PRIVATE KEY-----
MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBANWjjXoSIDbnOZuO
4vjtQXLV6zbQm/6V/V9hERrq/s1KnpWYG5RrxuapGqB90JEPXm26uHxQleIooiCD
7ch/qB+XHs4k8kfrdmyaWvwDz3EsodpVm6vFFYG4czQMX4h7rlXcNyqrHNBH7VoH
07WwoVQvCky1QTQ3e8jD3jJ4UHPPAgMBAAECgYEAjJ2aAT7s9TY8NKdXvYBsE6m5
p9qm0mrm2mCJYa5LB9SVjOERRh+qSygC3p/xJ4l2HcNIqopgHPuhusUbPVzIys23
Fr/BOlxW7/GWrijaZb2UdTPvjnrOzfKu2wl41sF++pDCe2y2YnvrAr3gCAHM0t1u
n4EjbzkfGJjjhYI27AECQQD49iaSeUAhyv/e3aEOaWNrb4mAP+y9g272LLrDU9Nh
MWi5qV8FDchCE7BB79jdjqUnNvAiDaX4lQFrLDaBL9jdAkEA263BdFMVSS/o4jEz
1vZMqa6YkelnzIY/MHFP7iZ7yLKBLBEkPzYQFJVNnQrzCIEW2du8YvJRrz5pk/hz
YqNemwJAChbvuT/wuW3gsMeKn2rl/JSonen5TjTlalSlvQTIrEe0VtHmZ+4HD6Z8
ni96OoBtcQlo8fhboZdoV0+TZejqgQJALPCj1cc1YI6Dhtpn737degz0u0zTZjzE
aoWTw3Vt90XFNR2gm6nUqlFM2mamB0RZR2IzbM6DtWUANjwqZrBjJwJABsoMPr+v
a2QLTqre47Wl/1KWZJ/TLz4xQzXobwyk+PRaO//3DEo1ra2HnnCoSq/rtSaQG3rz
C63nSSCR2wAHDA==
-----END PRIVATE KEY-----'''

TEST_PUBKEY = '''-----BEGIN PUBLIC KEY-----
%s
-----END PUBLIC KEY-----'''


# 私钥签名
def sign(data, priKey=None):
    if priKey == None:
        priKey = TEST_PRIKEY
    key = RSA.importKey(priKey)
    h = MD5.new(data)
    # print h
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(h)
    # print signature
    return_ret = base64.b64encode(signature)
    # print return_ret
    return return_ret


# 公钥验签
def verify(data, signature, publick, DEBUG=False):
    if DEBUG:
        pubKey = TEST_PUBKEY % publick
    else:
        pubKey = ''
    if not data:
        return False
    if not signature:
        return False
    key = RSA.importKey(pubKey)
    h = MD5.new(data)
    verifier = PKCS1_v1_5.new(key)
    if verifier.verify(h, base64.b64decode(signature)):
        return True
    return False


def rsa_decrypt(text):
    """校验RSA加密 使用私钥进行解密"""
    cipher = Cipher_pkcs1_v1_5.new(RSA.importKey(TEST_PRIKEY))
    retval = cipher.decrypt(base64.b64decode(text), 'ERROR').decode('utf-8')
    return retval


def rsa_encrypt(message, publicKey):
    publicKey = TEST_PUBKEY % publicKey
    """校验RSA加密 使用公钥进行加密"""
    cipher = Cipher_pkcs1_v1_5.new(RSA.importKey(publicKey))
    cipher_text = base64.b64encode(cipher.encrypt(message.encode())).decode()
    return cipher_text


if __name__ == '__main__':
    #     # result = {"code": 1, "msg": "success", "timestamp": time.time()}
    #     # data = {"ip": "12345678", "ram": 10.88}
    #     # result["data"] = data
    #     # sign_abc = rsa_encrypt(json.dumps(result))
    #     # print(sign_abc)
    #
    data = {"ip": "45.77.59.22", "sshPwd": "aGiZ/uOaS3R/bzJy5+0HY4sO0N1pp0Uq/mb6chMnHe0=",
            "time": "2021-04-21 20:02:28"}
    test = b'{"ip":"45.77.59.22","sshPwd":"aGiZ/uOaS3R/bzJy5+0HY4sO0N1pp0Uq/mb6chMnHe0=","time":"2021-04-21 20:02:28"}'

    public = '''
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDW3FKdZ8Cq4eF+j9yvMkd3m7Y0
    XUeXYzAuWprZjvcBM5Ffm0Krck/WyeSLHa34Tt2yUJaPatFBM1x0+HdfRLeo5oJX
    E0HW92hGEWcyQE7hDcYOgC1TEHwIx4uWmrNNj8yOztZrIKVfjHC1xr58HJxvbCa2
    vU/upeKaMpouXAVwawIDAQAB
    '''

    # s = str(json.dumps(data, sort_keys=True,
    #                    separators=(',', ':')))
    # # s = str(data)
    # test_byte = s.encode("utf-8")
    s = b'123456'
    print(s)
    print(verify(s,
                 "kQTtZCTylRW9k9GPcdNOWOwT2lhCBxRGxT1QPgXFvU3yA7islhW6Fm+3pWUfrtCe68zGdrDEqKCwBB93YBo8Sum1xPAKCmjk5MLuGlAyhYQoaWajUlrvXwjM8OKVvUsaFQWlCIwCFHbohXG8BnO5tO8Ut6DLn0NK8lRYYjs4bzY=",
                 public,
                 DEBUG=True))
