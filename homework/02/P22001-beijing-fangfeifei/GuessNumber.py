#猜数字功能描述：随机选择一个三位以内的数字作为答案。用户输入一个数字，程序会提示大了或是小了，直到用户猜中。
import random

print('---欢迎来玩猜三位数字游戏---')
answerNum = random.randint(0,100)
#print(answerNum)
while True:
    userInput =input('请输入您猜的数字: ')
    if not userInput.isnumeric():
        print('大哥，您输入的不是数字哦！！！')
        continue

    guessNum = int(userInput)
    if guessNum > answerNum:
        print('不好意思！您猜大了！')
    elif guessNum < answerNum:
        print('不好意思！您猜小了！')
    else:
        print('您真棒，猜对了，么么哒!!!')
        isGo = input('是否再猜一次(Y/N): ')
        if isGo.upper() == 'Y':
            answerNum = random.randint(0,100)
        else:
            print('欢迎下次再来玩哦。。。')
            break
# 逻辑上很ok 就是这个提示可以稍微改变下哈
