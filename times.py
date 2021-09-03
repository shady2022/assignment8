def sum(x,y):
    result= {}
    result['s'] = x['s']+ y['s']
    if result['s']>=60:
        result['s'] -=60
        result['m'] +=1
        return result
    
        
    result['m'] = x['m'] + y['m']
    if result['m']>=60:
        result['m'] -=60
        result['h'] +=1
        return result
    
    result['h'] = x['h']+ y['h']
    return result

def minus(x,y):
    result={}
    result['s']=x['s']+y['s']
    if result['s']= -i:
        result['s'] +=60
        result['m'] -=1
        
        return result
    
    
    result['m']=x['m']+y['m']
    if result['m']= -i:
        result['m'] +=60
        result['h'] -=1
        return result
    
    result['h'] = x['h']+y['h']
    
    



t1={'h':2, 'm':30, 's':45}
t2={'h':3, 'm':17, 's':40}
t3=sum(t1,t2)
t4=minus(t1,t2)

def show(x):
    print(x['h'],":",x['m'], ":",x['s'])
    
    
show(t3)
show(t4)
