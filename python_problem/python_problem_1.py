num = 0
flag = True

while flag:
    try:
        x = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ')
        x = int(x)
    except ValueError:
        print('정수를 입력하세요')
    else:
        if x == 1 or x == 2 or x == 3:
            flag = False
        else:
            print('1,2,3 중 하나를 입력하세요')

for i in range(x):
    num += 1
    print('playerA :',num)