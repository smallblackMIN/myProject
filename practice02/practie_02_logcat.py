'''
（1）使用python，抓取logcat（android），并保存为文件，文件命名为抓取时的时间戳（例如 2021_01_16_19_23_45.log）
（2）同时抓取多个logcat，第1个直接logcat，第2个使用过滤（grep或findstr，过滤error等级的日志），两个都保存下来，
都用时间戳命名；直接抓取的logcat放置在logcat文件夹下，第二个保存在error文件目录下
思路：
step1、判断是否连接设备，如果设备没连接，则结束并提示连接，如连接则进入step2
step2、用户选择基于哪个设备进行日志抓取
step3、起两个线程:一个线程进行logcat 日志抓取;第二个线程进行过滤后的日志抓取;
step4、每个线程的结果都写入文件夹
细节：
写入文件并存入文件夹：
1、判断是否存在当天的文件夹，如果不存在就先新建一个，然后存入文件夹
2、文件名需要命名组合，时间加日期

'''
#cd /Users/minzeng/PycharmProjects/myProject/practice02
#可以转成exe运行     pyinstaller --onefile --nowindowed --icon="/Users/minzeng/PycharmProjects/myProject/practice02" practie_02_logcat.py

import time
import datetime
import os
import re
import sys
import signal
import subprocess
class Get_logcat():
    def __init__(self):
        pass
#作为文件名
# name = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    def get_devices(self):
        """
        获取设备列表
        :return: 设备列表
        """
        str_init = ''
        devices_info = os.popen('adb devices').readlines()
        # print(devices_info)
        for i in range(len(devices_info)):
            # print(devices_info[i])
            str_init += devices_info[i]
            # print('第一次',str_init)
        devices_name=re.findall('\n(.+?)\t',str_init,re.S)
        # devices = re.findall(r'(.*?)\tdevice\b', devices_info)
        devices = {}
        j = 1
        for i in devices_name:
            devices[j] = i
            print("{xuhao}、 {device}".format(xuhao=j,device=i))
            j = j + 1

        return devices


    def choose_device(self):
        devices_dict = self.get_devices()
        if devices_dict=={}:
            print("暂无设备连接")
            return False
        else:
            while 1:
                try:
                    number = input("请选择要操作的设备编号:")
                    number = int(number)
                    device_number = devices_dict[number]
                    break
                except ValueError as e:
                    print("输入的内容有误，请重新输入已有的序号")
            return device_number

    def mk_file(self):
        name = datetime.datetime.now().strftime('%Y%m%d')
        if not os.path.exists('./logcat/%s' % name):
            os.makedirs('./logcat/%s' % name)
            os.makedirs('./logcat/%s/Error' % name)
            return True
        else:
            return False


    def get_logcat(self):
        daytime = datetime.datetime.now().strftime('%Y%m%d')
        name = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        while True:
            device_num = self.choose_device()
            if device_num is not False:
                action1 = "adb -s {num} logcat -v time > ./logcat/{day}/{file}.txt".format(num=device_num,day=daytime,file=name)
                action2 = "adb -s {num} logcat *:E > ./logcat/{day}/Error/{file}.txt".format(num=device_num,day=daytime,file=name)
                pro1 = subprocess.Popen(action1,shell=True)
                pro2 = subprocess.Popen(action2,shell=True)
                time.sleep(2)
                print("日志抓结束了")
                pro1.kill()
                pro2.kill()
                break
            else:
                return False



if __name__ == '__main__':
    Get_logcat().get_logcat()
