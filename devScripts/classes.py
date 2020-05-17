class employees:
    #raiseAmount = 1.04

    def __init__(self, firstName, lastName, email, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.pay = pay

    def fullName(self):
        return self.firstName + ' ' + self.lastName

    def applyRaise(self,raiseAmount=1):
        self.pay = int(self.pay) * raiseAmount
        return self.pay


emp1 = employees('Karthik', 'Shekarappa', 'karthikms.erappa@gmail.com', '72000')
emp2 = employees('Kyle', 'Clarkson', 'kyle.clarkson@intel.com', '140000')
#emp1.raiseAmount = 1.2
#emp2.raiseAmount = 1.5
print(emp1.applyRaise(),emp2.applyRaise(1.1))
print(emp2.__dict__.get('pay'))