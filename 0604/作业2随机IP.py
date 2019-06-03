from urllib import request
import random

IP = []

def UserAgent():
    print(IP[random.randint(0,len(IP)-1)])
    print(IP[random.randint(0, len(IP)-1)])
    print(IP[random.randint(0, len(IP)-1)])

if __name__ == '__main__':
    with open('IP.txt','r') as f:
        for line in f.readlines():
            ip1 = line.strip('\n')
            b = ip1.replace(' ',':')
            IP.append(b)
    UserAgent()
