# coding = utf-8


def register():
    username = raw_input("Please input your username").strip()
    while True:
        password1 = raw_input("Please input your password").strip()
        password2 = raw_input("Please input your password again").strip()

        if password1 == password2:
            password = password1
            break
        else:
            print "Please retry!"
    f = open('member.txt', 'r')
    lines = f.readlines()
    lines.append('\n')
    lines.append(username+' '+password+' '+0)
    f.close()
    f = open('member.txt', 'w')
    f.writelines(lines)

    print 'Register Success!'
    f.close()

