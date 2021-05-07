import os

import json

import math
import platform
from collections import OrderedDict

import logger
import re

log = logger.Logger('info.log', level='debug')


def shell():
    data = {}
    points = []
    # data = os.system("chmod +x /root/bee-clef/address.sh && /root/bee-clef/address.sh")
    # tmp = os.popen("chmod +x /root/bee-clef/address.sh && /root/bee-clef/address.sh").readlines()[0]
    tmp = os.popen("curl -s localhost:1635/addresses | jq .ethereum").readlines()[0]
    # str_data = json.loads(str(tmp).strip("\n").encode("utf-8"))
    print(tmp)
    data["address"] = tmp.strip("\n").strip("\"")
    try:
        # 获取余额
        balance = os.popen("curl localhost:1635/chequebook/balance").readlines()
        balance_str = json.loads(str(balance[0]).strip("\n").encode("utf-8"))
        if str(balance_str).__contains__("totalBalance"):
            data["balance"] = balance_str["totalBalance"]
            data["balance"] = int(data["balance"]) / math.pow(10, 16)
        else:
            data["balance"] = 0
        data["balance"] = str(data["balance"])
        # 获取版本号
        node_version = os.popen("rpm -qa | grep bee | grep -v bee-clef").readlines()[0]
        data["node_version"] = str(node_version).strip("\n")

        # 获取bee状态
        swarm_state = os.popen("curl localhost:1633").readlines()
        if str(swarm_state[0]).strip("\n").__contains__("Ethereum Swarm Bee"):
            data["swarm_state"] = str(swarm_state[0]).strip("\n")
            if data["swarm_state"].__contains__("Ethereum Swarm Bee"):
                data["swarm_state"] = 1
            else:
                data["swarm_state"] = -2
        else:
            data["swarm_state"] = -2

        # 与服务器占用的空间
        ips = os.popen(
            "netstat -tun | grep \":1634\" | awk '{print $5}' | cut -d: -f1 | sort | sort -n").readlines()
        for n in ips:
            trueIp = re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', n)
            if trueIp:
                points.append(n.strip("\n"))
            else:
                print("未匹配到")
        data["point_ip"] = points
        data["os.version"] = platform.platform()
        cashs = []
        # 未兑换的支票信息
        cash = os.popen("/root/bee-clef/cashout.sh").readlines()
        for i in cash:
            cashs.append(str(i).strip("\n"))
        data["cash"] = cashs

        log.logger.info(data)
        return data
    except:
        log.logger.error(data)
        return data


if __name__ == "__main__":
    print(shell())
