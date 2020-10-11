import os
import time
import sys


os.system('clear')
os.system('''
pkg install python python2 nano ruby figlet
gem install lolcat
''')
os.system('clear')
print " Tools Installer"
print "+---------------+"
print "    Nama Lu"
print "+---------------+"
print "__________________"
print "{!}    Menu    {!}"
print "{1} Hack Facebook "
print "{2} Crack Random"
print "{0} Keluar"
print "__________________"
pilih = raw_input('Pilih Menu:')
if pilih == '':
        os.system('clear')
        print "Salah !!!"
        sys.exit()
elif pilih == '1':
        os.system('clear')
        os.system('git clone https://github.com/storiku/darkfb')
        os.system('cd darkfb')
        os.system('python2 Dark.py')
elif pilih == '2':
        os.system('clear')
        os.system('git clone https://github.com/RIZY4/pro')
        os.system('cd pro')
        os.system('python2 pro.py')
elif pilih == '0':
        os.system('clear')
        print "terima kasih :)"
        sys.exit()
else:
        os.system('clear')
        print "Salah"
