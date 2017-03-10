# cnblogsTitleGetter

> 博客园个人文章抓取


* 网络库基于requests

* 项目基于Python3.60版本,其他版本未做验证

```
from TittleGetter import *

# http://www.cnblogs.com/YouXianMing/

# 博客园url上的个人名字
titleGetter = TittleGetter("YouXianMing")

# 如果存在这个人,则继续
if titleGetter.userExist:

    # 开始分析以及遍历数据
    for item in titleGetter.startAnalyse.titleObjectList:

        print("%s %s" % (item.titlename, item.url))
```

![demo.gif](http://images2015.cnblogs.com/blog/607542/201703/607542-20170310205153545-1345443343.gif)
