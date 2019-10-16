# club_script
## python 爬虫实践
### 开发环境
* python3.7
* beautifulsoup4 : 4.8.1
* chardet 3.0.4
* request 2019.4.13

### 开发步骤
* 用request包获取想要爬取的页面的html，并用chardet解码，对应代码中gethtlm函数。
* 在htlm中找到所需爬取的项目的格式，名称等，进行select,find, 对应代码中parse 函数。其中time在基础网页中没有找到，点进二级网页，获取到了json，用json包解析得到publish time.
* 将获取到的属性们放入字典，输出。
* 设置时间戳，用sleep()函数设置，隔一天一循环。

### 使用说明
clone 到本地，配置依赖包，运行club.py文件
