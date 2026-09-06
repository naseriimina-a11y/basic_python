def inter_union_set (s : set)-> dict:
    result = {}
    result['intersection']=s['s1'].intersection(s['s2'])
    result['union']=s['s1'].union(s['s2'])
    
    return result

print(inter_union_set ({'s1':{1,2,4,5},'s2':{5,3,2}}))
        
        
    
