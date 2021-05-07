chmod +x /root/bee-clef/CentOS_Python3.6.sh

yum install net-tools -y

v=`python3 -V | cut -c 1-6`

echo $v

if [[ "$v" != "Python" ]] 
then 
   sh /root/bee-clef/CentOS_Python3.6.sh
fi


python3 /root/bee-clef/get-pip.py

pip install --upgrade pip

pip install ConfigParser


pip install requests

pip install psutil

echo "* * * * * root python3 /root/bee-clef/os_data/request.py" >> /etc/crontab

systemctl restart crond
