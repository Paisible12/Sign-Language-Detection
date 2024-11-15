import os

def CompareAndRename():
    for A in B:
        B = "ABCDEFGHIKLMNOPQRSTUVWXY"
        DIR = f"./Maitri(A-Z)/{A}"
        DIR2 = f"./data/{A}"
        n = len(os.listdir(DIR2))
        # print(n)
        start = n
        buff = 1000
        # start = int(input("Number: "))
        l = list(os.listdir(DIR))
        for i in l:
            os.rename(os.path.join(DIR,i),os.path.join(DIR,f"{buff}.jpg"))
            buff = buff + 1

        l = list(os.listdir(DIR))
        for i in l:
            os.rename(os.path.join(DIR,i),os.path.join(DIR,f"{start}.jpg"))
            start = start + 1

def Rename(DIR, start = 0):
    buff = 1000
    l = list(os.listdir(DIR))
    for i in l:
        os.rename(os.path.join(DIR,i),os.path.join(DIR,f"{buff}.jpg"))
        buff = buff + 1
    
    l = list(os.listdir(DIR))
    for i in l:
        os.rename(os.path.join(DIR,i),os.path.join(DIR,f"{start}.jpg"))
        start = start + 1

Rename("./data/A", 0)