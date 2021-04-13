import requests
import math
import time

import hashlib
import json
import node_data
import shell

import os

timstamp = math.ceil(time.time())

# 上报数据接口
var url = ''


def request():
    data = {}
    m = hashlib.md5()

    headers = {"content-type": "application/json"}
    try:
        result = {"code": 1, "msg": "success", "data": data, "timestamp": timstamp}
        data["monitor_data"] = node_data.node_data()
        data["node_data"] = shell.shell()
        nid = os.popen("cat /sys/class/dmi/id/product_uuid")
        data["nid"] = str(nid.readlines()[0]).strip("\n")
        m.update(str(result).encode("utf-8"))
        result["sec"] = m.hexdigest()
        print(result)
        out = requests.post(url,
                            json=result)
        print(out.text)
    except:
        result["code"] = 0
        result["msg"] = "获取数据错误".encode("utf-8")
        m.update(str(result).encode("utf-8"))
        result["sec"] = m.hexdigest()
        requests.post(url,
                      data=json.dumps(str(result), ensure_ascii=False))


if __name__ == '__main__':
    request()
