import psutil
import os
import platform


def node_data():
    mem = memory_stat()
    data = {}
    points = []
    data["cpu_count"] = os.cpu_count()
    data["ram_total"] = mem['MemTotal'] / 1024 / 1024 / 1024
    data["cpu_usage"] = psutil.cpu_percent(interval=1, percpu=False)
    data["ram_usage"] = mem['MemUsed'] / 1024 / 1024 / 1024
    disk = os.popen(
        "lsblk |egrep '^(v|s)d[a-z]' |awk '{print $4}'|sed 's/[a-Z]//'|awk '{disk[$1]++} END {for(i in disk){print i}}' |awk '{sum +=$1};END{print sum}'").readlines()[
        0]
    data["disk"] = int(str(disk).replace("G", "").strip("G\t/root\n"))
    data["folder"] = int(disk_usage()) * 1024
    ips = os.popen(
        "netstat -tun | grep \":1634\" | awk '{print $5}' | cut -d: -f1 | sort | sort -n").readlines()
    for n in ips:
        points.append(n.strip("\n"))
    data["point_ip"] = points
    data["os.version"] = platform.platform()
    cashs = []
    # 未兑换的支票信息
    cash = os.popen("/root/bee-clef/cashout.sh").readlines()
    for i in cash:
        cashs.append(str(i).strip("\n"))
    data["cash"] = cashs
    print(data)
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


if __name__ == "__main__":
    node_data()
