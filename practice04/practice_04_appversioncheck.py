'''
app版本的命名规则为A.B.C.D  例如2.1.5.20120107，在app打包的时候 ，会生成app的版本号。
ABC为版本号，D为打包时间Y-M-D
目前有两个测试包，已经获取到了他们的版本号，写一个方法实现版本大小的比较。
思路：
获取到两个测试包的版本号后，进行split分割，从A开始对比
问题点：
1、判断版本号是否符合规范，需要验证一下：检查分割后是否为长度为4的列表；检查分割后列表中的各个值是否均为数字
2、当ABC都相同时，是根据D的时间先后判断版本是否更新
'''
import time
import datetime
class compare_version():
    def __init__(self):
        pass
    def versioncheck(self,v):
        l = v.split('.')
        if len(l) == 4:
            for i in range(4):
                if l[i].isdigit():
                    continue
                else:
                    print("该测试包版本不规范")
                    return False
                    # break
        return l
    def versioncompare(self,v1,v2):
        try:
            l1 = self.versioncheck(v1)
            l2 = self.versioncheck(v2)
            if l1[0] == l2[0]:
                if l1[1] == l2[1]:
                    if l1[2] == l2[2]:
                        print('两个测试包的版本号相同')
                        time1 = time.strptime(l1[3],'%Y%m%d')
                        time2 = time.strptime(l2[3],'%Y%m%d')
                        a1 = datetime.date(time1.tm_year, time1.tm_mon, time1.tm_mday)
                        b1 = datetime.date(time2.tm_year, time2.tm_mon, time2.tm_mday)
                        if a1.__eq__(b1) is False:
                            if a1.__gt__(b1) is True:
                                print('{a}版本时间比{b}要新'.format(a=v1,b=v2))
                            else:
                                print('{b}版本时间比{a}要新'.format(a=v1,b=v2))
                        else:
                            print('{a}和{b}版本时间也相同'.format(a=v1, b=v2))
                    elif l1[2] > l2[2]:
                        print('{a}版本高于{b}'.format(a=v1, b=v2))
                    elif l1[2] < l2[2]:
                        print('{a}版本低于{b}'.format(a=v1, b=v2))
                elif l1[1] > l2[1]:
                    print('{a}版本高于{b}'.format(a=v1, b=v2))
                elif l1[1] < l2[1]:
                    print('{a}版本低于{b}'.format(a=v1, b=v2))
            elif l1[0] > l2[0]:
                print('{a}版本高于{b}'.format(a=v1,b=v2))
            elif l1[0] < l2[0]:
                print('{a}版本低于{b}'.format(a=v1, b=v2))
        except TypeError:
            print('版本号出现问题，无法进行比较')

if __name__ == '__main__':
    test = compare_version()
    test.versioncompare('.2.3.20210304','1.2.3.20210304')






