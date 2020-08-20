class bank:
    bank_name="union bank of india"
    def __init__(self,bank_bal,acc_no,name):
        self.bank_bal=bank_bal
        self.acc_no=acc_no
        self.name=name
        return
    def display(self):
        print("bank name is :",bank.bank_name)
        print("account holder name is:",self.name)
        print("account number is :",self.acc_no)
        print("account balance is :",self.bank_bal)
        return
    def main():
        print("enter  first customer detail:")
        k=input("enter name:")
        l=int(input("enter account number:"))
        m=int(input("enter balance:"))
        print("enter  second customer detail:")
        n=input("enter name:")
        o=int(input("enter account number:"))
        p=int(input("enter balance:"))
        print("first customer detail is:")
        obj=bank(m,l,k)
        obj.display()
        print("second customer detail is:")
        obj=bank(p,o,n)
        obj.display()
        return
    
bank.main()        
       
