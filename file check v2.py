import os

for root, dirs, files in os.walk(".", topdown=False):
     for file in files:
        with open(os.path.join(root, file), "r") as auto:
            if '.log' in file:
                if 'Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch  Software (cat4500es8-UNIVERSALK9NPE-M), Version 03.06.04.E RELEASE SOFTWARE (fc2)' in open (os.path.join(root, file)).read():
                    print('true - BOOT ' + file)
                else:
                    print('false - BOOT ' + file)
                if 'ROM: 15.1(1r)SG5' in open (os.path.join(root, file)).read():
                    print('true - ROMMON ' + file)
                else:
                    print('false - ROMMON' + file)

            


input('Press ENTER to exit')
