def min_max_len (x : list)->dict:
    if not isinstance(x,list):
        raise TypeError ('input  must be list')
    out = {'min':1e12 , 'max':0 , 'len':0}
    for i in x:
        if i < out['min']:
            out['min'] = i
        if i > out['max']:
            out['max'] = i
        
        out['len'] += 1

    return out

print(min_max_len ([1,3,4,12,100]))
print(min_max_len (1))


# solution 2
'''
def min_max_len (x : list)->dict:
    if not isinstance(x,list):
        raise TypeError ('input  must be list')
    return {'min': min(x) ,'max' : max(x) , 'len' : len(x)}
'''


        
