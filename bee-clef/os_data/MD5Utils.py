import hashlib

import json

# import uuid
#
# import demjson

import codecs


def md5To2(message, salt):
    m = hashlib.md5()
    m.update(str(message).encode("utf-8"))
    p = m.hexdigest()
    m1 = hashlib.md5()
    s = str(p).__add__(salt)
    m1.update(s.encode("utf-8"))
    return m1.hexdigest()


if __name__ == "__main__":
    data = {"ip": "1.14.144.106", "salt": "rASbk2IX", "sshPwd": "epgH+nHuVJaR6MbdpWJLd4sO0N1pp0Uq\/mb6chMnHe0=",
            "time": "2021-04-22 13:40:17"}
    #
    # data = r'{"ip":"1.14.144.106","salt":"rASbk2IX","sshPwd":"epgH+nHuVJaR6MbdpWJLd4sO0N1pp0Uq\/mb6chMnHe0=","time":"2021-04-22 13:40:17"}'
    s = json.dumps(data, sort_keys=True,
                   separators=(',', ':'))
    # uid = uuid.uuid3(uuid.NAMESPACE_DNS, "!@#$%")
    print(s)
    d2 = codecs.getdecoder("unicode_escape")(s)[0]
    print(d2)
    # print(demjson.decode(str(data)))
    print(md5To2(d2, "rASbk2IX"))
