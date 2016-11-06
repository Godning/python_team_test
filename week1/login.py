# coding = utf-8


def login():
    lock_num = 0
    flag = True
    while flag:
        f = open('member.txt', 'r')
        file_content = f.readlines()[1:]
        f.close()
        username = raw_input("Please input your username").strip()
        password = raw_input("Please input your password").strip()
        for line in file_content:
            user, pwd, num= line.split(' ')
            num = num.strip(' ').strip('\n')
            if user == username and pwd == password:
                if num == '0':
                    flag = False
                    break
                else:
                    print 'Locked account!\n'
                    break
            if user == username and pwd != password:
                if lock_num < 2:
                    print "Password is not right!\nPlease retry!\n"
                    lock_num += 1
                else:
                    f = open('member.txt','r')
                    file_content = f.readlines()
                    f.close()
                    write_txt = ""
                    for line in file_content:
                        user, pwd, num = line.split(' ')
                        if user == username:
                            write_txt  += user+' '+pwd+' 1'+'\n'
                        else:
                            write_txt += line
                    fw = open('member.txt','w')
                    fw.writelines(write_txt)
                    fw.close()
                    print 'Your account has been locked !\n'
                    break

    if flag == False:
        print "Welcome "+ username


