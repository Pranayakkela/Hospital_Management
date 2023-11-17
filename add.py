'''
def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    retrun inner
a.outer()
print(a.__name__)
print(a)
'''
a=10
b=20
c=a+b
print(c)