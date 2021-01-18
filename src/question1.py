f=open("input/connexion.log","r")
w=open("output/utilisateurs.txt","w")
l=[]
for line in f:
    l.append(line.split(";")[1])
for elt in sorted(set(l)):
    w.write(f"{elt}\n")
f.close()
w.close()