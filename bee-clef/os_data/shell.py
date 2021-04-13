import os

import sys

import json

import math
import time


def shell():
    data = {}
    # data = os.system("chmod +x /root/bee-clef/address.sh && /root/bee-clef/address.sh")
    # 地址bee 节点分配的地址
    tmp = os.popen("chmod +x /root/bee-clef/address.sh && /root/bee-clef/address.sh").readlines()[0]
    str_data = json.loads(str(tmp).strip("\n").encode("utf-8"))
    data["address"] = str_data["result"][0]
    # 获取余额
    balance = os.popen("curl localhost:1635/chequebook/balance").readlines()
    if len(balance) > 0:
        balance_str = json.loads(str(balance[0]).strip("\n").encode("utf-8"))
        data["balance"] = balance_str["totalBalance"]
        data["balance"] = int(data["balance"]) / math.pow(10, 16)
    else:
        data["balance"] = 0

    # 获取版本号
    node_version = os.popen("rpm -qa | grep bee | grep -v bee-clef").readlines()[0]
    data["node_version"] = str(node_version).strip("\n")

    # 获取bee状态
    swarm_state = os.popen("curl localhost:1633").readlines()
    if len(swarm_state) > 0:
        data["swarm_state"] = str(swarm_state[0]).strip("\n")
        if data["swarm_state"].__contains__("Ethereum Swarm Bee"):
            data["swarm_state"] = 1
        else:
            data["swarm_state"] = -2
    else:
        data["swarm_state"] = -2
    print(data)
    return data


if __name__ == "__main__":
    shell()
