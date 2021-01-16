# from nimbella import redis
import json
import redis


def main(args):

    # red = redis()
    red = redis.StrictRedis(host='127.0.0.1', port=6379, password='',db=0)

    connectors = red.get('connectors')

    connectors = connectors.decode("utf-8").split(",") if connectors else []

    return {"body": {"details": {
        "connectors": connectors
        }}}
