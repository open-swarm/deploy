import config
import requests
import time
import node
import swarm
import logger
import MD5Utils

log = logger.Logger('info.log', level='debug')

import os

timstamp = int(time.time())


def bee():
    data = {}
    try:
        result = {"code": 1, "msg": "success", "data": data}
        data["monitor_data"] = node.node_data()
        data["node_data"] = swarm.shell()
        nid = os.popen("cat /sys/class/dmi/id/product_uuid")
        data["nid"] = str(nid.readlines()[0]).strip("\n")
        data["time"] = timstamp
        uid = data["nid"]
        result["type"] = "swarm"
        result["data"] = str(data)
        da = str(data)
        result["sign"] = MD5Utils.md5To2(da, uid)
        log.logger.info(result)
        url = config.getConfig("node", "push.url")
        out = requests.post(url + "m/swarm/api/swarm_node_data",
                            data=result)
        log.logger.info(out.text)
    except:
        log.logger.error("发生错误了")


if __name__ == "__main__":
    bee()
