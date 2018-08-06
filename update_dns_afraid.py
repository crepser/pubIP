#!/usr/bin/python3

import requests as r
import re
import datetime
import os
from pathlib import Path

url = 'https://www.whatismyip.org/my-ip-address'
ip_path = '/tmp/myip/current_ip'
log_path = '/tmp/myip/log'
update_dns = os.environ['UPDATE_DNS']

if not update_dns:
  print('You need to setup your UPDATE_DNS environment variable berfore launching this script')

try:
  req = r.get(url)
  ip = re.search(r'\d+\.\d+\.\d+\.\d+', req.text).group()
  if os.path.isfile(log_path):
    log_file = open(log_path, 'a')
  else:
    log_file = open(log_path, 'w')
  
  if os.path.isfile(log_path):
    ip_file = open(ip_path, 'r')
  else:
    ip_file = open(ip_path, 'w')
   
  saved_ip = ip_file.read()
  if ip != saved_ip:
    ip_file.close()
    ip_file = open(ip_path, 'w')
    ip_file.write(ip)
    log_file.write('{} ip changed from {} to {} \n'.format(datetime.datetime.now(), saved_ip, ip))
  else:
    log_file.write('{} ip didnt change \n'.format(datetime.datetime.now()))
    
except:
  with open(log_path) as log_file:
    log_file.write('{} couldnt reach {} \n'.format(datetime.datetime.now(), url)) 
