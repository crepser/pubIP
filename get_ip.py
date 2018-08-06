#!/usr/bin/python3

import requests as r
import re
import datetime

url = 'https://www.whatismyip.org/my-ip-address'
ip_path = '/tmp/myip/current_ip'
log_path = '/tmp/myip/log'

try:
  req = r.get(url)
  ip = re.search(r'\d+\.\d+\.\d+\.\d+', req.text).group()
  with open(ip_path, 'w') as ip_file:
    ip_file.write(ip)
    
except:
  with open(log_path) as log_file:
    log_file.write('{} couldnt reach {}'.format(datetime.datetime.now(), url)) 
