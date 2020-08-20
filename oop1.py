a=50
class A:
    a=40
    def __init__(self):
        self.a=30
        print("from constructor")
        print(id(self))
        return
    def m1():
        a=10
        print("class level")
        return
    def m2(self):
        a=20
        print("object level")
        print("a:",a)
        print(self.a)
        return
    def main():
        global a
        print(a)
        a=5
        print(a)
        print(A.a)
        obj=A()
        print(obj.a)
        print(id(obj))
        return
A.main()    

