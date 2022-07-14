# -*- coding: utf-8 -*-
# @Time    : 2022/7/14 18:38
# @Author  : AI悦创
# @FileName: template.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
for f in range(100, 106):
	c = 5 * (f - 32) / 9
	print("%8.0f%10.2f" % (f, c))
