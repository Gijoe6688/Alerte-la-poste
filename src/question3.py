w=open("input/warning.txt","r")
c=open("input/connexion.log","r")
s=open("output/suspect.txt","w")
# l=[]
# for line in w:
#     line=line.strip()
#     l.append(line)
l=[line.strip() for line in w]
l_suspect=[]
for lin in c:
    lc=lin.split(";")
    ip=lc[0].strip()
    name=lc[1].strip()
    if ip in l:
        l_suspect.append(name)
l_suspect_unique=sorted(set(l_suspect))
for elt in l_suspect_unique:
    n=l_suspect.count(elt)
    s.write(f"{elt};{n}\n")
w.close()
c.close()
s.close()
