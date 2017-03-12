# cnblogsTitleGetter

> 博客园个人文章抓取


* 网络库基于requests

* 项目基于Python3.60版本,其他版本未做验证

```
from tittle_getter import *

# http://www.cnblogs.com/YouXianMing/

# 博客园url上的个人名字
title_getter = TittleGetter("YouXianMing")

# 如果存在这个人,则继续
if title_getter.user_exist:

    # 开始分析以及遍历数据
    for item in title_getter.start_analyse.title_object_list:

        print("%s %s" % (item.title_name, item.url))
```

![demo.gif](http://images2015.cnblogs.com/blog/607542/201703/607542-20170310205153545-1345443343.gif)
