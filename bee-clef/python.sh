curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python3 get-pip.py

pip install requests

pip install psutil

echo "* * * * * root python3 /root/bee-clef/os_data/request.py" >> /etc/crontab

systemctl restart crond
