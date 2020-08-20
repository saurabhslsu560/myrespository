class Test:
    def __init__(self):
        print("constructor Test")
        print("address:",self)
        print("init val:",id(self))
        print("class type:",type(self))
        return
Test()
class b:
    def __init__(self):
        print("constructor b")
        print("address:",self)
        print("init val:",id(self))
        print("class type:",type(self))
        return
b()
