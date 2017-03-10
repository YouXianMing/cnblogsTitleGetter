import requests
from regExp import *


class TittleObject:

    def __init__(self, titlename, url):

        self.titlename = titlename
        self.url = url


class TittleGetter:

    def __init__(self, username):

        self.__username = username
        self.__titleObjectList = None

    @property
    def titleObjectList(self):
        return self.__titleObjectList

    @property
    def userExist(self):
        """
        检验给定的用户名是否存在
        :return: 存在则返回True,不存在则返回False
        """

        userExist = True

        r = requests.get("https://home.cnblogs.com/u/" + self.__username)
        if r.ok:

            # 请求通了,但并不一定存在这个用户
            if len(RegExp.match(r'用户不存在', r.text)):
                userExist = False
        else:

            # 请求没有通
            userExist = False

        return userExist

    @property
    def startAnalyse(self):
        """
        开始进行分析
        :return: TittleGetter对象
        """

        self.__titleObjectList = []

        # 开始逐个网页分析,直到网页文章数目为0就停止
        for i in range(1, 10000):

            webUrlString = "http://www.cnblogs.com/%s/default.html?page=%d" % (self.__username, i)
            itemCount = self.__analyseUrl(webUrlString)
            if itemCount <= 0:
                break

        return self

    def __analyseUrl(self, urlString):
        """
        开始分析网页
        :param urlString: 网页地址
        :return: 文章的数目
        """

        print("======> 准备开始解析页面 %s" % urlString)

        # 用于记录文章数目,为0则表示已经爬完了
        itemCount = 0

        # 开始请求
        r = requests.get(urlString)
        if r.ok:

            print("成功解析页面 %s ,准备开始匹配数据" % urlString)

            # 开始寻找标题url
            itemsList = RegExp.match(r'_TitleUrl_.+?</a>', r.text, re.MULTILINE | re.IGNORECASE)

            if len(itemsList):
                print("---------------------------------------")

            # 进行分割
            for item in itemsList.split("\n"):

                if len(item):

                    # 文章url
                    url = (RegExp.match(r'(?<=href=").+?(?=")', item, re.MULTILINE | re.IGNORECASE).split("\n"))[0]

                    # 文章标题
                    title = (RegExp.match(r'(?<=">).+?(?=</a>)', item, re.MULTILINE | re.IGNORECASE).split("\n"))[0]

                    # 文章数目统计
                    itemCount += 1

                    print("%s %s" % (title, url))
                    self.__titleObjectList.append(TittleObject(title, url))

            if len(itemsList):
                print("<该页面有 %s 条数据>" % itemCount)
                print("---------------------------------------\n")
            else:
                print("该页面无数据,已到最后一页,停止解析\n\n\n")

        else:

            print("获取页面 %s 失败, 即将终止解析\n" % urlString)


        return itemCount

