# coding = utf-8

import login,register

if __name__ == '__main__':
    choose = raw_input("Welcome! Please select mode: 1 to login || 2 to register\n")
    if choose == '1' :
        login.login()
    if choose == '2':
        register.register()


