import os

for root, dirs, files in os.walk(".", topdown=False):
     for file in files:
        with open(os.path.join(root, file), "r") as auto:
            if '.log' or '.LOG' in file:
                print(file)
                if 'Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch  Software (cat4500es8-UNIVERSALK9NPE-M), Version 03.06.04.E RELEASE SOFTWARE (fc2)' in open (os.path.join(root, file)).read():
                    print('IOS - Good')
                else:
                    print('IOS - Bad')
                if 'ROM: 15.1(1r)SG5' in open (os.path.join(root, file)).read():
                    print('ROMMON - Good')
                else:
                    print('ROMMON - Bad')
                if 'BOOT variable = bootflash:cat4500es8-universalk9npe.SPA.03.06.04.E.152-2.E4.bin,1;' in open (os.path.join(root, file)).read():
                    print('Boot Var - Good')
                else:
                    print('Boot Var - Bad')
                print('\n')
                          

            


input('Press ENTER to exit')
