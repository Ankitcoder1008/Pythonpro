x=40
y=30
if(x>y):
    print("True")
elif(x==y):
    print("both are same")
else:
    print("False")
a=5
b=4
c=9
if(a<b and a<c):
    print("a is less than both")
elif(a==b and a==c):
    print("a is equal to both")
elif(a>b and a>b):
    print("a is less than both")
if(a<b or a<c):
    print("a is less than both or anyone of them")
if(a<b):
    print("a is lesser from b")
    if(a<c):
        print("it is also lesser from c")
else:
    print("other result")