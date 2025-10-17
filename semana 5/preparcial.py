c=input()

print(c.count('@')==1 and len(c.split('@')[0]) >= 3 and len(c.split('@')[1]) >= 3 and c.count(".")>=1 and " "not in c and c[0]!="." and c[-1]!=".")