import os
import sys


argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]  


def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

if(argument == '-create'):
    create('docker run -p 2400:2400 --name final_redis_container -d redis', 'redis')
