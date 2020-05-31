#!/usr/bin/env python 

#ScriptName: pipUtils.py
#Author: kshekara
#Description:Easier way to pip new modules ...........it's bullshit - Just a wrapper for pip
###################################################################

#Importing all the required libs
import os
import argparse



#To install utils
def installUtils(utilsList):
    #check and install either utils or upgrade all utils
    upgradeFlag = 0
    for util in utilsList:
        if util == 'all' && upgradeFlag == 0:
            os.system('sudo apt-get upgrade')
            upgradeFlag = 1
            #print('sudo apt-get upgrade')
        else:
            os.system('sudo apt-get install ' + util)
            #print('sudo apt-get install ' + util)



#main flow of script
def main(utils):
    utilsList = utils.split(',')
    if utilsList:
        installUtils(utilsList)
    else:
        print('\n')
        print('********************Please provide Utilites Eg:  python3.8 pipUtils.py -u tree,ls')
        print('\n')

#Getting command line argument
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script to pip in ubuntu')
    parser.add_argument('-u', help='Single or multiple utilites to install on ubuntu',required=True)
    args = parser.parse_args()

    main(args.u)
