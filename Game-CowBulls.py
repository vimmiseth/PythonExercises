import random


print("***** Welcome to Cows and Bulls Game *****")
print("A 4-digit random number will be generated")
print(" For each digit that you guess right, at right place, you get 1 cow")
print(" For each digit that you guess right, but wrong place, you get 1 bull")

#base_num = random.randint(0,9)
#get the lenght of list & for each cell see that it does not match

mylist = []
n = random.randint(1,9)
mylist.append(n)

for j in range(2,5):
    while( 1):
        m = random.randint(1, 9)
        if m not in mylist:
            mylist.append(m)
            break

#print(mylist)
smylist = [ str(s) for s in mylist  ]

s=""
snum = s.join(smylist)
inum = int(snum)

file1 = open(r"C:\Game\CowBull\MyFile-CB.txt","w+")
file1.writelines(["\n", snum])

#for every pos, if it matched cow +1 else mybulls
#if it is there bulls+

while( 1 ):
    cow = 0
    bull = 0
    mybull = []
    sres = input("Please enter a 4-digit number. 0 to quit: ")
    try:
        ires = int(sres)
    except:
        print("enter integer only")
        sres  = "1"
        ires = 1

    if ires == 0 :
        break
    else:
        pass
    if len(sres) != 4:
        continue
    else:
        pass

    file1.writelines(["\n", sres])
    for i in range(0,4):
        if sres[i] == snum[i]:
            cow = cow + 1
        else:
            mybull.append(sres[i])

    for j in range(0, len(mybull)):
        if mybull[j] in snum:
            bull = bull + 1
        else:
            pass
    mydict = {}
    mydict["cow"] = cow
    mydict["bull"] = bull
    print(mydict)
    file1.writelines("\n")
    file1.writelines(str(mydict ))

    if cow == 4 :
        print ("Great")
        break
    else :
        pass

file1.writelines("\n")
file1.close()
