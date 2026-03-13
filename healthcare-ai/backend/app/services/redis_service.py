import redis
r=redis.Redis(host='localhost',port=6379)
r.set("heart_rate",72)
print("heart rate stored in redis")