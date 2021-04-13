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
echo "0 0 * * * root /root/bee-clef/cashout.sh cashout-all 5 start" >> /etc/crontab
systemctl restart crond.service
systemctl start supervisord.service 
supervisorctl start bee-clef
echo '{"id": 1, "jsonrpc": "2.0", "method": "account_list"}' | nc -U /var/lib/bee-clef/clef.ipc
rpm -Uvh /root/bee-clef/bee_0.5.3_amd64.rpm
supervisorctl start bee
chmod +x /root/bee-clef/python.sh
sh /root/bee-clef/python.sh
