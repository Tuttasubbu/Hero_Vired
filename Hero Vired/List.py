lis = []
for i in range(5):
    while True:
        n = int(input("enter a number"))
        if n>0:
            lis.append(n)
            break
        else:
            print("enter a positive number")
summ = sum(lis)
print(summ)
n = open("List.txt","w")
print(lis,file=n)
print(summ,file=n)
n.close()       