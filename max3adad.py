def max2ada (x:(int,float),y:(int,float))->(int,float):
    if x>y:
        return x
    else:
        return y 

def max3adad (x:(int,float),y:(int,float),z:(int,float) )->(int,float):
    return max2ada( max2ada (y,z),x)
       

print(max3adad (6,1,2 ))
