#!/bin/bash
yum install epel-release -y
yum install -y  wget jq nc supervisor
timedatectl set-timezone Asia/Shanghai
hwclock -w
firewall-cmd --zone=public --add-port=1635/tcp --permanent
firewall-cmd --zone=public --add-port=1634/tcp --permanent
firewall-cmd --zone=public --add-port=1633/tcp --permanent
firewall-cmd --reload
rpm -Uvh /root/bee-clef/bee-clef_0.4.9_amd64.rpm
chmod +x /root/bee-clef/cashout.sh
chmod +x /root/bee-clef/start/clef-service
chmod +x /root/bee-clef/start/bee.sh
mv /root/bee-clef/bee-clef.ini  /etc/supervisord.d/
mv /root/bee-clef/bee.ini  /etc/supervisord.d/
systemctl enable supervisord.service
rpm -Uvh /root/bee-clef/bee_0.5.3_amd64.rpm
rm -rf /root/bee-clef/bee_0.5.3_amd64.rpm  
rm -rf /root/bee-clef/bee-clef_0.4.9_amd64.rpm
systemctl start supervisord.service
rm -rf /root/bee-clef/install.sh
rm -rf /root/bee-clef.zip

