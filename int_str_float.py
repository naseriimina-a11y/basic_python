l = [1,20, 12.5, 'x', 'm', 19.1]

STR = []
INT =[]
FLOAT =[]

for i in l:
    if isinstance (i,int):
        INT.append(i)
    elif isinstance (i,str):
        STR.append(i)
    elif isinstance (i,float):
        FLOAT.append(i)

print('int:',INT,"-" , 'float:',FLOAT,"-" ,'str:',STR )
