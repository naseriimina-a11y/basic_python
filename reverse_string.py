Str = input( "yek matn vared kon:" )
x = []
for i in range (len(Str)-1,-1,-1):
    print(Str[i],end='')
    x.append(Str[i])
print()
print("".join (x))
