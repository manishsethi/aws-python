#!/usr/bin/python
#
# Author: Manish
#

import boto.ec2, sys

# AWS_ACCESS_KEY_ID
AAKI=''
# AWS_SECRET_ACCESS_KEY
ASAK=''
# Region string
REGION=''

def print_usage(args):
  print 'Usage:', args[0], 'stop|start <instance name>'
  sys.exit(1)

def usage(args):
  arg1 = ['stop', 'start']
  if not len(args) == 3:
    print_usage(args)
  else:
    if not args[1] in arg1:
      print_usage(args)
    else:
      return args[2]

myinstance = usage(sys.argv)
conn = boto.ec2.connect_to_region(REGION, aws_access_key_id=AAKI, aws_secret_access_key=ASAK)
if sys.argv[1] == 'start':
  try:
    inst = conn.get_all_instances(filters={'tag:Name': myinstance})[0].instances[0]
  except IndexError:
    print 'Error:', myinstance, 'not found!'
    sys.exit(1)
  if not inst.state == 'running':
    print 'We are starting the instance with tag', myinstance
    inst.start()
  else:
    print 'Error:', myinstance, 'already running or starting up!'
    sys.exit(1)

if sys.argv[1] == 'stop':
  try:
    inst = conn.get_all_instances(filters={'tag:Name': myinstance})[0].instances[0]
  except IndexError:
    print 'Error:', myinstance, 'not found!'
    sys.exit(1)
  if inst.state == 'running':
    print 'We are stopping instance with tag', myinstance
    inst.stop()
  else:
    print 'Error:', myinstance, 'already stopped or stopping'
    sys.exit(1)
