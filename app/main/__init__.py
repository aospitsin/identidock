import redis
from flask import Flask

app = Flask(__name__)
cache = redis.StrictRedis(host="redis", port=6379, db=0)