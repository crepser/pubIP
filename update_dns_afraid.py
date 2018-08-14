#!/usr/bin/python3

import requests as r
import re
import datetime
import os

url = 'https://www.whatismyip.org/my-ip-address'
root_path = '/tmp/myip'
ip_path = '/tmp/myip/current_ip'
log_path = '/tmp/myip/log'
saved_ip = ''

#create directory
if not os.path.exists(root_path):
  os.makedirs(root_path)

try:
  os.environ['UPDATE_DNS']
except KeyError:
  print('You need to set UPDATE_DNS before running this script')
  exit()

try:
  req = r.get(url)
  ip = re.search(r'\d+\.\d+\.\d+\.\d+', req.text).group()
  if os.path.isfile(log_path):
    log_file = open(log_path, 'a')
  else:
    log_file = open(log_path, 'w')
  
  if os.path.isfile(ip_path):
    ip_file = open(ip_path, 'r')
    saved_ip = ip_file.read()
    ip_file.close()

  if ip != saved_ip:
    ip_file = open(ip_path, 'w')
    ip_file.write(ip)
    log_file.write('{} ip changed from {} to {} \n'.format(datetime.datetime.now(), saved_ip, ip))
  else:
    log_file.write('{} ip didnt change \n'.format(datetime.datetime.now()))
    
except:
  with open(log_path) as log_file:
    log_file.write('{} couldnt reach {} \n'.format(datetime.datetime.now(), url)) 
