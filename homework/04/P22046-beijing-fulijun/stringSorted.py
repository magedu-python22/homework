#!/usr/bin/env python
#coding:utf-8
# @author: fulijun
# @date: 2019-06-24

'''
s = "Sorting1234" 
给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
1 所有的小写字母在大写字母前面
2 所有的字母在数字前面
3 所有的奇数在偶数前面 
'''

upper_case = []
lower_case = []
odd_case = []
even_case = []
sorted_case = []

        
def selectedSort(nums_list):
    for idx,num in enumerate(nums_list):
        max_idx = idx
        for i in range(idx+1, len(nums_list)):
            if nums_list[i] > nums_list[max_idx]:
                max_idx = i
        if idx != max_idx:
            nums_list[idx], nums_list[max_idx] = nums_list[max_idx], num
            
    return nums_list.reverse()
        
def decimal2Ascii(aList):
    for i in range(len(aList)):
        aList[i] = chr(aList[i]) 
        
    return aList
    
def main(aString):
    for i in aString:
        if i.isupper():
            upper_case.append(ord(i))
            selectedSort(upper_case)
        elif i.islower():
            lower_case.append(ord(i))
            selectedSort(lower_case)
        elif i.isdigit():
            aNum = int(i)
            if aNum % 2 == 0:
                even_case.append(aNum)
                selectedSort(even_case)
            else:
                odd_case.append(aNum)
                selectedSort(odd_case)
        else:
            print('Do not support special characters')
            
    for j in (decimal2Ascii(lower_case), decimal2Ascii(upper_case), odd_case, even_case):
        sorted_case.extend(j)
    return sorted_case

if __name__ == '__main__':
    s = "Sorting1234"
    print(main(s))