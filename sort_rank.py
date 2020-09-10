fname = input("Please enter a filename: ")
if len(fname) < 1 : fname = clown.txt
fhand = open(fname)

#Chapter 9 lesson
wdic = dict()
#print(wdic)
for line in fhand :
    line = line.rstrip()
    words = line.split()
    for word in words :
        wdic[word] = wdic.get(word, 0) + 1
#print(wdic)

#Chapter 10 lesson
#version 1
#x = sorted(wdic.items())
#print(x[:5])

#version 2
tem_list = list()
for k,v in wdic.items() :
    new_tup = (v, k)
    tem_list.append(new_tup)
#print(tem_list)

tem_list = sorted(tem_list, reverse=True)
for v,k in tem_list[:5] :
    print(k,v)

print("all done")
