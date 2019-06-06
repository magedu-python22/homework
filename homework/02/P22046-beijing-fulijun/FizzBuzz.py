#!/usr/bin/env python
# coding:utf-8
#
num = 100

def main(a_num, a_list):
    for item in xrange(1, a_num+1):
        if item % 3 == 0:
            if item % 5 == 0:
                a_list.append('FizzBuzz')
            else:
                a_list.append('Fizz')
        elif item % 5 == 0:
            a_list.append('Buzz')   
        else:
            a_list.append('{}'.format(item))
    return a_list

if __name__ == '__main__':
    num_list = ['0']
    res = main(num, num_list)
    print(','.join(res))