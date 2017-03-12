import re


class RegExpString:
    def __init__(self, match_string):

        self._match_string = match_string

        # [字符串] 先调用了search_with_pattern之后再获取这个值,匹配成功返回字符串,匹配失败,返回None
        self._search_result = None

        # [字符串数组] 先调用find_all最后再获这个值,匹配成功返回字符串数组,匹配失败,返回None
        self._item_list = None

    # Property
    # ---------------------------------------

    @property
    def search_result(self):
        return self._search_result

    @property
    def item_list(self):
        return self._item_list

    # Public method
    # ---------------------------------------

    def search_with_pattern(self, pattern, flags=0):
        """
        用正则表达式匹配一次
        :param pattern: 正则表达式
        :param flags: 匹配方式
        :return: RegExpString对象
        """

        # 验证正则表达式是否合法,不合法则报错
        RegExpString._check_pattern(pattern)

        # 开始匹配
        result = re.search(pattern, self._match_string, flags)

        # 获取匹配结果
        self._search_result = None
        if result:
            self._search_result = result.group(0)

        return self

    def find_all(self, pattern, flags=0):
        """
        用正则表达式匹配所有的结果
        :param pattern: 正则表达式
        :param flags: 匹配方式
        :return: RegExpString对象
        """

        # 验证正则表达式是否合法,不合法则报错
        RegExpString._check_pattern(pattern)

        # 获取匹配的数组
        self._item_list = None
        item_list = re.findall(pattern, self._match_string, flags)
        if len(item_list):
            self._item_list = item_list

        return self

    # Internal method
    # ---------------------------------------

    @staticmethod
    def _check_pattern(pattern):
        """
        验证正则表达式是否正确,不正确则崩溃
        :param pattern: 正则表达式
        :return: None
        """

        try:
            re.compile(pattern)
            is_valid = True

        except re.error:
            is_valid = False

        if not is_valid:
            assert False, '正则表达式有误.'
