###爬取豆瓣电影top250      https://movie.douban.com/top250         的电影数据，并保存在MongoDB中。


启动MongoDB数据库需要两个命令：

mongod：是mongoDB数据库进程本身
mongo：是命令行shell客户端


sudo mongod # 首先启动数据库服务，再执行Scrapy
sudo mongo # 启动数据库shell

在mongo shell下使用命令:

# 查看当前数据库
> db

# 列出所有的数据库
> show dbs

# 连接DouBan数据库
> use DouBan

# 列出所有表
> show collections

# 查看表里的数据
> db.DouBanMoives.find()
