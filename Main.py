from tittle_getter import *

# http://www.cnblogs.com/YouXianMing/

# 博客园url上的个人名字
title_getter = TittleGetter("YouXianMing")

# 如果存在这个人,则继续
if title_getter.user_exist:

    # 开始分析以及遍历数据
    for item in title_getter.start_analyse.title_object_list:

        print("%s %s" % (item.title_name, item.url))
