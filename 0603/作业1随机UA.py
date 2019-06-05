from urllib import request
import random

UA = []

def UserAgent():
    print(UA[random.randint(0,3)])
    print(UA[random.randint(0, 3)])
    print(UA[random.randint(0, 3)])

if __name__ == '__main__':
    with open('UA.txt','r') as f:
        for line in f.readlines():
            UA.append(line.strip('\n'))
    UserAgent()
