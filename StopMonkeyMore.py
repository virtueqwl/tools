# -*- coding: UTF-8 -*- 
#author:liuwenquan
import sys, os
import threading

def SearchSN():
    cmd = 'adb devices'
    os.system(cmd)
    result = os.popen(cmd).read()
    if "List of devices attached" in result:
        deviceslist = [device.split('\t')[0] for device in result.split('\n')[1:] if device != '']

        if len(deviceslist) > 0:
            print deviceslist
            return deviceslist
        else:
            print 'no devices found, script exit'
            return False
            sys.exit()
    else:
        print ('adb status error, script exit')
        return False
        sys.exit(1)
def StopMonkey(SN):
    cmd = 'adb -s %s shell "ps | grep monkey"'%SN
    os.system(cmd)
    output = os.popen(cmd).read()
    if "root" in output:
        pid = output.split(" ")[6]
        print pid

    stopcmd = "adb -s %s shell kill %s" %(SN,pid)
    os.system(stopcmd)

def batchRun():
    workers = []
    sn_list = SearchSN()
    for sn in sn_list:
        workers.append(threading.Thread(target=StopMonkey, args=(sn,)))
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
if __name__ == '__main__':
    batchRun()