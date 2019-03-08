import redis

def addTask():

    start_urls = ['http://top.chinaz.com/hangyemap.html']

    for url in start_urls:
        result = redis_cli.lpush('myspider:start_urls',url)
        print(result)

    # result = redis_cli.lpush('myspider:start_urls', *start_urls)
    # print(result)

if __name__ == '__main__':
    #创建redis数据库连接
    redis_cli = redis.StrictRedis(host='118.24.255.219',port=6390)
    addTask()
