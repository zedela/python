a = input("Enter Sentence: ")
k = input("Enter Key Value: ")
s = a.split(" ")
d = " "

print("Entered Sentence: ", s)

for i in range(len(s)):
    for j in s[i]:
        d += j  # yvela sityva gavaertiane ro gvepova chven key-s sheicavda tu ara

if k not in d:
    print("-1")

else:

    for i in range(len(s)):
        # davbechdet listis yvela sityva da shevamowmet romeli sheicavda key-s
        if k in s[i]:
            print("Index Of Word: ", i)  # vipovet indexi im sityvis romelic key-s sheicavs
            sityva = s[i]  # shevinaxet cvladshi is sityva romelic sheicavda key-s
            break

    for j in range(len(sityva)):
        # shenaxuli sityva davshalet asoebad da satitaod shevadaret key-s
        if k in sityva[j]:
            print("Index Of Key: ", j)  # vipovet key-s index sityvashi
            break