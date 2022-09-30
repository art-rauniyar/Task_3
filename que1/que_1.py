import re

f = open("onelinefile.txt")
data = f.read()
f.close()

exp = re.compile(r'(\d+)([A-Za-z]+)(\d+\.\d+)([A-Za-z]+)')
a = exp.findall(data)

f = open("Filename2.csv", "w")
for i in a:
    f.write(",".join(i) + "\n")
f.close()
