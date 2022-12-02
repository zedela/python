a = int(input("Enter Number: "))
b = int(input("Enter Number: "))
c = int(input("Enter Number: "))
d = int(input("Enter Number: "))

list1ricxvebi = list()
list2ricxvebi = list()

tanakveta = list()

list1 = list()
list2 = list()

list1.append(a)
list1.append(b)
list2.append(c)
list2.append(d)

list1.sort()
list2.sort()

for i in range(list1[0] - 1, list1[1]):
    i += 1
    list1ricxvebi.append(i)

for i in range(list2[0] - 1, list2[1]):
    i += 1
    list2ricxvebi.append(i)

for i in range(len(list1ricxvebi)):

   if list1ricxvebi[i] in list2ricxvebi:
       tanakveta.append(list1ricxvebi[i])
print(tanakveta[0], tanakveta[-1])
    
#for i in range(list1ricxvebi[0],list2ricxvebi[-1]+1):
    #if i not in list1ricxvebi and i not in list2ricxvebi:
        #print("0")