f=open("input/connexion.log","r")
w=open("output/utilisateurs.txt","w")
l=[]
for line in f:
    name=line.split(";")[1]
    l.append(name)
for elt in sorted(set(l)):
    w.write(f"{elt}\n")
f.close()
w.close()