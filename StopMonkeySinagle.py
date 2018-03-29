# -*- coding: UTF-8 -*- 
#author:liuwenquan
import sys, os
def StopMonkey():
    cmd = 'adb shell "ps | grep monkey"'
    os.system(cmd)
    output = os.popen(cmd).read()
    if "root" in output:
        pid = output.split(" ")[6]

    print pid
    stopcmd = "adb shell kill %s" %pid
    os.system(stopcmd)
if __name__ == '__main__':
    StopMonkey()