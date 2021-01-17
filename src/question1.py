f=open("input/connexion.log","r")
w=open("output/utilisateurs.txt","w")
for line in f:
    name=line.split(";")[1]
    w.write(f"{name}\n")
f.close()
w.close()