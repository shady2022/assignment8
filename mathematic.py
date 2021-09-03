def mul(x,y):
    result = {}
    result['s']= x['s']* y['s']
    
    result['m']=x['m'] * y['m']
    
    return result

def show(x):
    print(x['s'], '/', x['m'])
    
a = {'s':2, 'm':3}
b = {'s':5, 'm':4}

c = mul(a,b)
show(c)

def sum(x,y):
    result= {}
    result['s']=x['s']* y['m'] +x['m']* y['s']
    result['m']= x['m']*y['m']
    
    return result
d = sum(a,b)
show(d)

def minus(x,y):
    result = {}
    result['s']= x['s']*y['m']-y['s']* x['m']
    result['m']= x['m']*y['m']
    
    return result

E = minus(a,b)
show(E)

def divide(a,b):
    result={}
    result['s']=x['s']*y['m']
    result['m']= x['m']* y['s']
    
    return result

F = divide(a,b)
show(F)