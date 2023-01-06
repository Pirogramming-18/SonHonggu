#함수 이름은 변경 가능합니다.

##############  menu 1
def Menu1(name, mid, final):
    student_list.append([name,int(mid),int(final)])

# ##############  menu 
def Menu2():
    for data in student_list:
        if len(data) == 3:
            score = (data[1]+data[2])/2
            if score >= 90:
                data.append('A')
            elif 80 <= score < 90:
                data.append('B')
            elif 70 <= score < 80:
                data.append('C')
            else:
                data.append('D')

# ##############  menu 3
def Menu3():
    print('------------------------')
    print('name  mid  final  grade')
    print('------------------------')
    for i in student_list:
        print('%-6s' % i[0], end='')
        print('%-5s' % i[1], end='')
        print('%-7s' % i[2], end='')
        print('%-7s' % i[3])
        

# ##############  menu 4
def Menu4(delete):
    for idx, data in enumerate(student_list):
        if delete in data:
            del student_list[idx]

student_list = []
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        flag = True
        try:
            name, mid, final = input('Enter name mid-score final-score : ').split()
        except ValueError:
            print('Num of data is not 3!')
        else:
            for i in student_list:
                if name in i:
                    print('Already exist name!')
                    flag = False
                    break
            try:
                int(mid)
                int(final)
            except ValueError:
                print('Score is not positive integer!')
            else:
                if flag:
                    Menu1(name, mid, final)

    elif choice == "2" :
        if len(student_list) == 0:
            print('No student data!')
        else:
            print('Grading to all students.')
            Menu2()

    elif choice == "3" :
        if len(student_list) == 0:
            print('No student data!')
        else:
            for i in student_list:
                if len(i) != 4:
                    print("There is a student who didn't get grade.")
                    break
            else:
                Menu3()

    elif choice == "4" :
        if len(student_list) == 0:
            print('No student data!')
        else:
            delete = input('Enter the name to delete : ')
            for i in student_list:
                if delete in i:
                    Menu4(delete)
                    print(delete, 'student information is deleted.')
                    break
            else:
                print('Not exist name!')

    elif choice == "5" :
        print('Exit Program!')
        break

    else :
        print('Wrong number. Choose again')