from collections import OrderedDict

import psutil
import os

import logger

log = logger.Logger('info.log', level='debug')


def node_data():
    mem = memory_stat()
    data = {}

    # cpu 核数
    data["cpu_count"] = str(os.cpu_count())

    # 总共内存大小
    data["ram_total"] = str(mem['MemTotal'] / 1024 / 1024 / 1024)

    # cpu使用率
    data["cpu_usage"] = str(psutil.cpu_percent(interval=1, percpu=False))
    # 内存使用大小
    data["ram_usage"] = str(mem['MemUsed'] / 1024 / 1024 / 1024)

    # 服务器磁盘大小
    disk = os.popen(
        "lsblk |egrep '^(v|s)d[a-z]' |awk '{print $4}'|sed 's/[a-Z]//'|awk '{disk[$1]++} END {for(i in disk){print i}}' |awk '{sum +=$1};END{print sum}'").readlines()[
        0]
    # data["disk"] = str(int(str(disk).replace("G", "").strip("G\t/root\n")))

    data["disk"] = str(disk).strip("\n")

    # swarm bee 数据目录占用的空间
    data["folder"] = str(int(disk_usage()) * 1024)

    log.logger.info(data)

    return data


def disk_usage():
    disk = os.statvfs("/")
    folder = disk.f_bsize * (disk.f_blocks - disk.f_bfree) / (1024 ** 3)
    return folder


def memory_stat():
    mem = {}
    f = open("/proc/meminfo")
    lines = f.readlines()
    f.close()
    for line in lines:
        if len(line) < 2: continue
        name = line.split(':')[0]
        var = line.split(':')[1].split()[0]
        mem[name] = int(var) * 1024.0
    mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
    return mem


def test():
    log.info('张三')


if __name__ == "__main__":
    node_data()
