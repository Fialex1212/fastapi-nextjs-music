import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(port=REDIS_PORT, host=REDIS_HOST, password="redisadmin", decode_responses=True)
