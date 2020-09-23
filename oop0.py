class customer:
    def __init__(self,id,name,email,phone_no):
        self.id=id
        self.name=name
        self.email=email
        self.phone_no=phone_no

class payment:
    def __init__(a,price,billno):
        a.price=price
        a.billno=billno


c1=customer("123","Hari pandey","haripandey@gmail.com","9800000000")
c2=customer("124","bikash gyawali",'bikash123@gmail.com',"9867278262")

p1=payment("200","123")
p2=payment("300","124")

print(c2.name)
print(p2.price)