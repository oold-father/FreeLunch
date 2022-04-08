# Copyright (C) 2019-2022 成都太行云梯科技有限公司
# Author  yinxin
# Date  2022/4/8 上午11:19
from pathlib import Path

file_path = Path(__file__).parent / 'static/AssassinationList.txt'

f = open(file_path.absolute(), "r", encoding="utf8")

s = f.read()
assassination_list = s.split("\n")

f.close()
