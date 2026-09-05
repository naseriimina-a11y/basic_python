Dict = {'a':12, 'b':13, 'c':14, 'd':15, 'e':16}
l = []
print("solution 1 ")
for i in Dict:
    if Dict[i]%3==0:
        l.append(Dict[i])

print ('tagsimpazir be 3: ',l)
print("-"*30)
print("solution 2 ")
l = []

for k,v in Dict.items():
    if v%3==0:
        l.append(v)

print ('tagsimpazir be 3: ',l)
