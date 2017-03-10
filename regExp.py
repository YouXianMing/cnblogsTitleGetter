import re


class RegExp:
    @staticmethod
    def match(pattern, string, flag=re.MULTILINE):
        """
        正则表达式匹配,每一个匹配结果均加上了'\n'并将这些参数进行拼接返回
        :param pattern: 正则表达式
        :param string: 匹配字符串
        :return: 拼接的字符串
        """

        try:
            re.compile(pattern)
            is_valid = True

        except re.error:
            is_valid = False

        if not is_valid:
            assert False, '正则表达式有误.'

        # 用正则表达式查找符合要求的字符串
        matchString = ""
        matches = re.finditer(pattern, string, re.MULTILINE)
        for matchNum, match in enumerate(matches):
            matchString += match.group() + "\n"

        return matchString[0:len(matchString) - 1]

    # 终端输入可以用 pattern = r'%s' %inputString 来达到实现 r'正则表达式' 的目的
    @staticmethod
    def replaceStringWithPattern(pattern, replaceString, sourceString):
        """
        替换字符串
        :param pattern: 正则表达式
        :param replaceString: 替换的文本
        :param sourceString: 原始文本
        :return:
        """
        return re.sub(pattern, replaceString, sourceString)

    @staticmethod
    def match_Multiline_Ignorecase(pattern, string):
        """
        正则表达式匹配,Multiline与Ignorecase模式
        :param pattern: 正则表达式
        :param string: 文本
        :return: BOOL值
        """

        try:
            re.compile(pattern)
            is_valid = True

        except re.error:
            is_valid = False

        if not is_valid:
            assert False, '正则表达式有误.'

        match = False
        matchObj = re.search(pattern, string, re.M | re.I)

        if matchObj:
            match = True

        return match

    @staticmethod
    def match_Multiline(pattern, string):
        """
        正则表达式匹配,Multiline模式,返回布尔值
        :param pattern: 正则表达式
        :param string: 文本
        :return: BOOL值
        """

        try:
            re.compile(pattern)
            is_valid = True

        except re.error:
            is_valid = False

        if not is_valid:
            assert False, '正则表达式有误.'

        match = False
        matchObj = re.search(pattern, string, re.M)

        if matchObj:
            match = True

        return match
