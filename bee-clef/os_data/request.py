import requests
import math
import time

import hashlib
import json
import node_data
import shell
import os

import logger

timstamp = math.ceil(time.time())

# 上报数据接口，上报数据全部都是json格式
url = ''

log = logger.Logger('info.log', level='debug')


def request():
    data = {}
    m = hashlib.md5()
    try:
        result = {"code": 1, "msg": "success", "data": data, "timestamp": timstamp}

        # 获取服务器相关数据
        data["monitor_data"] = node_data.node_data()

        # 获取bee 节点相关数据
        data["node_data"] = shell.shell()

        # 每个系统的唯一id,标识是哪台服务器
        nid = os.popen("cat /sys/class/dmi/id/product_uuid")
        data["nid"] = str(nid.readlines()[0]).strip("\n")
        m.update(str(result).encode("utf-8"))
        result["sec"] = m.hexdigest()
        log.logger.info(result)
        out = requests.post(url,
                            json=result)
        log.logger.info(out)
    except:
        result["code"] = 0
        result["msg"] = "获取数据错误".encode("utf-8")
        m.update(str(result).encode("utf-8"))
        result["sec"] = m.hexdigest()
        requests.post(url,
                      data=json.dumps(str(result), ensure_ascii=False))

        log.logger.error(result)


if __name__ == '__main__':
    request()
