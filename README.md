

##  bee-clef 目录文件介绍

#### os_data目录里面脚本介绍

！！！ 需要使用本脚本前提必须是要会python基础知识



1、 shell.py   主要是获取swarmbee节点相关的数据



2、 node_data.pyt 主要是用来监听服务器基础设施设备数据的



3、request.py 是把 swarmbee 和服务器相关的数据上报给上层服务进行整理和展示





### 部署安装swarm-bee

1、需要把bee-clef 上传到服务 /root 目录厦门

2、需要安装python pip 环境

3、修改os_data/request.py 的 上报数据的接口（改成自己的接口）

4、 执行 bee-clef /install.sh 脚本



## 环境要求

python 版本 >=3.6 

系统版本 linux centos 7.6 + 

硬件要求最低配置：2核4g  硬盘100g





