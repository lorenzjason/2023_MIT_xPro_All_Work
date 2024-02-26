# pip install redis
import redis

# connect to server
r = redis.Redis(host='localhost', port=6379, db=0)


# read items
for item in r.mget('Italy', 'France'):
    print(item)

