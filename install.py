import os
CorrectUsername = "g0sain"
CorrectPassword = "sim"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[#] \x1b[0;36m Enter Username\x1b[1;92m➤ ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[#] \x1b[0;36m Enter Password\x1b[1;92m➤ ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #fb-cloning-id SG
            loop = 'false'
        else:
            print "Wrong password!"
            os.system('xdg-open https://www.instagram.com/shubham_g0sain/?hl=en')
    else:
        print "Wrong username!"
        os.system('xdg-open https://www.instagram.com/shubham_g0sain/followers/')
os.system("pkg install git")
os.system("pkg install python")
os.system("git clone https://github.com/ShuBhamg0sain/instareport.git")
os.system("cd instareport")
os.system("cd main")
os.system("nano users.txt #set username and password")
os.system("python3 -m pip install requests")
os.system("python3 report.py")


