class calc:
    def add(self,x,y):
        z=x+y
        print("sum is:",z)
        return
    def add(self,x,y,z):
        p=x+y+z
        print("sum is :",p)
        return
class main:
    def overloading():
        obj=calc()
        obj.add(10,20,30)
        return
main.overloading()    
