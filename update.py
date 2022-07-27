#!/usr/bin/python3
import time
import datetime
import os
from qqwry import updateQQwry

'''获取文件的创建时间'''
def get_FileCreateTime(filePath):
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)

'''把时间戳转化为时间: 1479264792 to 2016-11-16'''
def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d',timeStruct)


def deletefile(PATH, DAYS_N):
    for eachfile in os.listdir(PATH):
        filename = os.path.join(PATH, eachfile)
        if os.path.isfile(filename):
            lastmodifytime = os.stat(filename).st_mtime
            # Sets how many days old files are deleted
            endfiletime = time.time() - 3600 * 24 * DAYS_N
            if endfiletime > lastmodifytime:
                # To remove the following comment is to delete the.log suffix file
                # Comment is delete path under all files do not match
                if filename[-4:] == ".dat":
                    os.remove(filename)
                    print("del %s success!!!" % filename)
        # If it is a directory, the current function is called recursively
        elif os.path.isdir(filename):  
            deletefile(filename)

if not os.path.exists('data'):
    os.makedirs('data')

if(os.path.exists('data/qqwry.dat')):
    os.rename('data/qqwry.dat', 'data/qqwry_' + get_FileCreateTime('qqwry.dat') + '.dat')

ret = updateQQwry('data/qqwry.dat');

print(ret)

deletefile('data', 90)
