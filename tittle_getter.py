import requests
from regexp_string import *


class TittleObject:

    def __init__(self, title_name, url):

        self.title_name = title_name
        self.url = url


class TittleGetter:

    def __init__(self, username):

        self.__user_name = username
        self.__title_object_list = None

    @property
    def title_object_list(self):
        return self.__title_object_list

    @property
    def user_exist(self):
        """
        检验给定的用户名是否存在
        :return: 存在则返回True,不存在则返回False
        """

        is_user_exist = True

        r = requests.get("https://home.cnblogs.com/u/" + self.__user_name)
        if r.ok:

            # 请求通了,但并不一定存在这个用户
            if RegExpString(r.text).find_all(r'用户不存在',re.MULTILINE).item_list:
                is_user_exist = False
        else:

            # 请求没有通
            is_user_exist = False

        return is_user_exist

    @property
    def start_analyse(self):
        """
        开始进行分析
        :return: TittleGetter对象
        """

        self.__title_object_list = []

        # 开始逐个网页分析,直到网页文章数目为0就停止
        for i in range(1, 10000):

            web_url_string = "http://www.cnblogs.com/%s/default.html?page=%d" % (self.__user_name, i)
            itemCount = self.__analyse_url(web_url_string)
            if itemCount <= 0:
                break

        return self

    def __analyse_url(self, urlString):
        """
        开始分析网页
        :param urlString: 网页地址
        :return: 文章的数目
        """

        print("======> 准备开始解析页面 %s" % urlString)

        # 用于记录文章数目,为0则表示已经爬完了
        item_count = 0

        # 开始请求
        r = requests.get(urlString)
        if r.ok:

            print("成功解析页面 %s ,准备开始匹配数据" % urlString)

            # 开始寻找标题url
            items_list = RegExpString(r.text).find_all(r'_TitleUrl_.+?</a>', re.MULTILINE | re.IGNORECASE).item_list

            if items_list:

                # 进行分割
                for item in items_list:

                    if len(item):

                        url = RegExpString(item).search_with_pattern(r'(?<=href=").+?(?=")', re.M | re.I).search_result
                        title = RegExpString(item).search_with_pattern(r'(?<=">).+?(?=</a>)', re.M | re.I).search_result

                        if url and title:
                            # 文章数目统计
                            item_count += 1
                            print("%s %s" % (title, url))
                            self.__title_object_list.append(TittleObject(title, url))

                if len(items_list):
                    print("<该页面有 %s 条数据>" % item_count)
                    print("---------------------------------------\n")

            else:
                print("该页面无数据,已到最后一页,停止解析\n\n\n")

        else:

            print("获取页面 %s 失败, 即将终止解析\n" % urlString)

        return item_count

