#/bin/bash

supervisorctl stop  bee-clef

supervisorctl stop   bee

yum -y remove supervisor
yum -y remove unzip

rm -rf /etc/supervisord.d


rm -rf /etc/supervisord.conf


rpm -qa| grep bee |xargs rpm -ev --allmatches --nodeps

groupdel bee-clef

userdel bee-clef

rm -rf /root/bee*

rm -rf /root/.bee

rm -rf /etc/bee-clef

rm -rf /etc/bee

rm -rf /var/lib/bee
rm -rf /var/lib/bee-clef

rm -rf /root/*.log

sed -i '/cashout/d' /etc/crontab
sed -i '/request/d' /etc/crontab


