#coding=utf-8
# 2019/05/13
# edit by ito
# 参考サイト
# > subprocessの使い方(Python3.6)
# https://qiita.com/caprest/items/0245a16825789b0263ad
import os
import sys
import subprocess



# データ・セットの総サンプル数を調べるためのスクリプト
PATH="/home/hoge/Pictures/tmp"
LIST = []

# 再帰的にファイルをリストとして返します。
def findAllFiles(dir=PATH, list=LIST):
    for root, dirs, files in os.walk(dir):
        for file in files:
            list.append(os.path.join(root,file))
        for dir_bit in dirs:
            list = findAllFiles(dir_bit, list)
    return list

allFiles = findAllFiles()

# タイムスタンプ更新系
import pathlib
import datetime
import time


allFiles = sorted(allFiles)

# 2019年11月11日 1時2分3秒
Y = 2020
M = 2
D = 14
h = 10
m = 1
s = 1
for file_ in allFiles:
    atime = mtime = time.mktime((Y, M, D, h, m, s, 0,0,0))
    os.utime(file_, (atime, mtime))
    s += 1
