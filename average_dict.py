def avg_dict (d : dict )-> dict:
    result ={}
    for k,v in d.items ():
        result.setdefault (f'{k}.average',round(sum(v)/len(v)))
    return result

print(avg_dict ({'l1':[1,2,2,5],'l2':[5,3,2],'l3':[1,2,3,4,5,6]}))
        
        
    
