# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def popsort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp
    print(list)
def directsort(list):
    for i in range(len(list)):
        max = i
        for j in range(i+1,len(list)):
            list_max= list[max]
            list_j = list[j]
            if(list[max] < list[j]):
                max = j
        tmp = list[i]
        list[i] = list[max]
        list[max] = tmp

    print(list)

def lengthOfLongestSubstring(str):
    '''

    :param str:输入的字符串
    :return: 返回首个不含有重复字符的最长子串
    方法一：
    最笨方法，按序排列组合，找出该字符串的所有不重复子串，去除含有重复字符的，然后找出长度最长的子串
    方法二：
    从字符串第一位开始，利用循环和切片，判断下一位是否存在于前几位中，如果存在，则从第二位开始
    左指针和右指针

    '''

    l = len(str)
    # list = []
    i = j = 0
    max = 0
    while(i < l and j < l):
        if str[j] in str[i:j]:
            i = i + 1
        else:
            j = j + 1
        if ((j + 1 - i) > max):
            max = j - i
    # if(j == l and max == 0):
    #     max = j - i
    print(max)

def longestPalindrome(str):
    '''
    :param str: 输入的字符串
    :return: 返回最长子串
    方法一from林妈：
    1、先建一个方法判断该字符串全长是否为回文
    2、取出不同长度的字符串合集，依次调用回文的方法

    方法二
    '''

def isPali(list):
    '''

    :param list: 输入数组
    :return: 返回数组最高位加一，每一个位置只能存储单个数字
    从最后一位开始判断，如果为9，则赋值为0，判断前一位是否为9，依次类推，到
    '''
    l = len(list)
    while(l > 0):
        if(list[l-1] == 9):
            list[l-1] = 0
            l = l - 1
        else:
            list[l-1] = list[l-1] + 1
            break
    if(l == 0):
        list.insert(0,1)
    return list

def maxProfit(list):
    '''
    :param list:给定一个数组，它的第i 个元素是一支给定股票第 i 天的价格。
    如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
    :return:返回最大利润
    方法一：
    循环左右对比，判断右边比左边大的，如果右边比左边大就相减存下差值，最后取所有差值中的最大值返回
    方法二：

    '''
    new_list = []
    for i in range(len(list)):
        for j in range((i+1),len(list)):
            if list[j] > list[i]:
                new_list.append(list[j] - list[i])
            else:
                continue

    if new_list == []:
        return 0
    else:
        return max(new_list)


def isempty(bool):
    if bool is True:
        return False
    else:
        return True




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # directsort([2,4,1,3,6,2,9,0,16])
    # lengthOfLongestSubstring("abcde")
    # print(isPali([9,9]))
    # print(list)
    # print(maxProfit([7,4,3]))
    print(isempty(True))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
