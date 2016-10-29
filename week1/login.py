# coding = utf-8


def login():
    username = raw_input("Please input your username").strip()
    password = raw_input("Please input your password").strip()

    file = open('member.txt','r')
    file_content = file.readlines()[1:]
    flag = False
    for line in file_content:
        user, pwd = line.split(' ')
        if user == username and pwd == password:
            flag = True
            break
    if flag:
        print "Welcome "+ username
    else:
        print "No user!"

