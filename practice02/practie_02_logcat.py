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
========================================================
(3)要求在保存日志时，控制台可以实时输出日志信息，并保存；不能有乱码的问题
(4)统计日志中出现error信息的次数
(5)捕获日志中的crash、anr等信息，分别保存到不同文件中（1、如anr建个anr的文件夹，统发生anr的行数，写到一个文件中；2、crash发生时，统计crash发生的日志所在的第一行，在crash的文件夹下保存一个crash的文件），建议文件名用开始记录的时间戳
思路：
1、使用subprocess中的stdout来指向输出，并通过转码来存储输出，乱码的问题用utf-8格式统一一下
2、
'''
#cd /Users/minzeng/PycharmProjects/myProject/practice02
#可以转成exe运行     pyinstaller --onefile --nowindowed --icon="/Users/minzeng/PycharmProjects/myProject/practice02" practie_02_logcat.py
import logging
import time
import datetime
import os
import re
import subprocess

class Get_logcat():
    def __init__(self):
        pass

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
        devices_name=re.findall('\n(.+?)\t',str_init,re.S) #re.S表示"."表示可以在跨行匹配，将整个字符串作为整体
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
        self.mk_file()#创建文件夹
        daytime = datetime.datetime.now().strftime('%Y%m%d')
        name = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        while True:
            device_num = self.choose_device()
            if device_num is not False:
                action1 = "adb -s {num} logcat -v time > ./logcat/{day}/{file}.txt".format(num=device_num,day=daytime,file=name)
                # action2 = "adb -s {num} logcat *:E > ./logcat/{day}/Error/{file}.txt".format(num=device_num,day=daytime,file=name)
                log_error = subprocess.Popen("adb -s {num} logcat *:E".format(num=device_num),stdout=subprocess.PIPE,shell=True)
                #在控制台输出日志
                log = subprocess.Popen("adb -s {num} logcat".format(num=device_num),stdout=subprocess.PIPE,shell=True)
                s = log.stdout
                time.sleep(3)
                log.kill()
                log_error.kill()
                log_path = r'./logcat/{day}/{file}.txt'.format(day=daytime,file=name)
                log_error_path = r'./logcat/{day}/Error/{file}.txt'.format(day=daytime,file=name)
                #设备日志打印到控制台，并逐行读取保存
                with open(log_path,'w',encoding='utf-8') as f1:
                    for line in log.stdout:
                        print(line.decode('utf-8'))
                        f1.write(line.decode('utf-8'))
                #错误日志写入文件并计数
                with open(log_error_path,'w',encoding='utf-8') as f2:
                    count = 0
                    for line in log_error.stdout:
                        f2.write(line.decode('utf-8'))
                        count = count + 1
                    print("当前error发生%s次" % (count-1))
                break
            else:
                return False







if __name__ == '__main__':
    Get_logcat().get_logcat()

    # logging.info("this is test")
