keyWords = [
    '精通',
    '熟悉',
    '掌握',
    '了解',
    '编写',
    '开发',
    '理解',
    '熟练',
    '能力',
    '维护'
]


def deal_position_desc(descriptions):
    import re

    result = []
    for desc in descriptions:
        # 判断是否包含汉字
        Chinese_characters = re.compile(r'[\u4e00-\u9fa5]')
        char = Chinese_characters.findall(desc)
        if not char:
            result.append(desc)
            continue

        # 筛选关键字
        for key in keyWords:
            if desc.find(key) > -1:
                # 去除结尾
                if desc.endswith('；'):
                    desc = desc[:-1]
                if desc.endswith('。'):
                    desc = desc[:-1]
                if desc.endswith(';'):
                    desc = desc[:-1]
                if desc.endswith('.'):
                    desc = desc[:-1]

                # 去除序号和开头的符号
                number = re.compile(r'\d')
                nums = number.findall(desc)
                if nums:
                    for num in nums:
                        index = desc.index(num)
                        if index == 0:
                            if desc[index + 1] == '年':
                                continue
                            else:
                                desc = desc[1:]
                if desc.startswith('.'):
                    desc = desc[1:]
                if desc.startswith('、'):
                    desc = desc[1:]
                if desc.startswith('•'):
                    desc = desc[1:]
                if desc.startswith(')'):
                    desc = desc[1:]
                if desc.startswith('）'):
                    desc = desc[1:]
                if desc.startswith('●'):
                    desc = desc[1:]

                result.append(desc.strip())
                break
    return ';'.join(re for re in result)


def deal_position_temptation(temptation):
    tem = temptation
    if temptation.startswith('职位诱惑：'):
        tem = temptation[5:]
    if temptation.startswith('职位诱惑:'):
        tem = temptation[5:]
    return tem
