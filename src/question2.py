f=open("input/connexion.log","r")
w=open("output/filtre.txt","w")
lunique=[]
for line in f:
    l=line.split(";")
    h=l[-1].split(" ")[-1].strip()
    if h<"08:00" or h>"19:00":
        lunique.append(l[1]+"; "+l[0])
for elt in sorted(set(lunique)):
    w.write(f"{elt}\n")
f.close()
w.close()