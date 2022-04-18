import os

# os.chdir("Logical/challenge")

with open("Flag","r") as f:
    flag=f.read().replace(" \n","").replace("x","0").replace("y","1").split(" , ")

with open("page.dat","r") as f:
    page=f.read().replace("\n","").replace("x","0").replace("y","1").split(" , ")

with open("MEM.dat","rb") as f:
    mem=f.read().replace(b"\n",b"").split(b" , ")

# converting mem (bytes) to mem2 (string/char)
mem2 = []
for i in mem:
    mem2.append(i.decode())

# Flag loop
for i in flag:
    p = int(i[:6],2)
    o = int(i[6:],2)
    f = int(page[p],2)
    c = mem2[f][o]
    # print(p,f,o,c)
    print(c,end="")
print()
