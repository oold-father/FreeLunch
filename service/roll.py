# Copyright (C) 2019-2022 成都太行云梯科技有限公司
# Author  yinxin
# Date  2022/4/8 上午11:06
import random

from config import assassination_list

def roll_menu():
    max_len = len(assassination_list)

    loop = random.randint(1000, 10000)

    result = []

    for i in range(loop):
        result.append(random.randint(0, max_len - 1))

    result_map = {}

    for i in result:
        if result_map.get(i):
            result_map.update({i: result_map.get(i) + 1})
        else:
            result_map.update({i: 1})

    max_key = max(result_map, key=result_map.get)

    return {
        'loop': loop,
        'name': assassination_list[max_key]
    }


if __name__ == '__main__':
    print(roll_menu())
