from TittleGetter import *

# http://www.cnblogs.com/YouXianMing/

# 博客园url上的个人名字
titleGetter = TittleGetter("YouXianMing")

# 如果存在这个人,则继续
if titleGetter.userExist:

    # 开始分析以及遍历数据
    for item in titleGetter.startAnalyse.titleObjectList:

        print("%s %s" % (item.titlename, item.url))
