class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, hours, pay_rate,CPF_rate):
      self.name = name
      self.hours = hours
      self.pay_rate = float(pay_rate)
      self.CPF_rate = float(CPF_rate)
      self.gross_pay = self.hours* self.pay_rate
      self.CPF_pay = self.CPF_rate/100 * self.gross_pay
      Employee.empCount += 1
   
   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  "\nHours: ", self.hours, "\nPay rate: ", self.pay_rate, "\nCPF rate: ", self.CPF_rate)
      
   def displayPayroll(self):
       print("Payroll statement for "+ self.name)
       print("Number of hours worked in week:", self.hours)
       print("Hourly pay rate: $"+ str("{0:.2f}".format(self.pay_rate)))
       print("Gross pay = $"+  str("{0:.2f}".format(self.gross_pay)))
       print(f"CPF contribution at {self.CPF_rate}% = $" +  str("{0:.2f}".format(self.CPF_pay)))

emp1 = Employee(input("Enter name: "), eval(input("Enter number of hours worked weekly: ")), eval(input("Enter hourly pay rate: ")), eval(input("Enter CPF contribution rate: ")))



emp1.displayPayroll()
'''
num=123.1345346
print("{0:.2f}".format(num))
print'''
