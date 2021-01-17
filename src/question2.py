f=open("input/connexion.log","r")
w=open("output/filtre.txt","w")
for line in f:
    l=line.split(";")
    h=l[-1].split(" ")[-1].strip()
    if h<"08:00" or h>"19:00":
        w.write(f"{l[1]}; {l[0]}\n")
f.close()
w.close()