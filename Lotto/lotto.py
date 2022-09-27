import random

dictonary = {} 

def lottozahlen():
    num_list = random.sample(range(1, 46), 6,)
    num_list.sort()
    print(num_list)
    return num_list

def speichern(ziehung):
    global dictonary
    for i in ziehung:
        if i in dictonary:
            dictonary[i] += 1
        else:
            dictonary[i] = 1

if __name__ == '__main__':
    for i in range(0,1000):
        speichern(lottozahlen())
    print(dictonary)    


