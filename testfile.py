class Employee:
    raise_amount = 1.09
    def __init__(self, first, last, department, pay, level):
        self.first = first
        self.last = last
        self.department = department
        self.pay = pay
        self.level = level
        self.email = first + last + '.' + '@menace.com'

    def fullName(self):
        return '{} {} {}'.format(self.first, self.last, self.raise_amount)
    
class Developer(Employee):
  def __init__(self, first, last, department, pay, level, pro_lang):
        super().__init__(first, last, pay, level,  department)
        self.pro_lang = pro_lang
        
class manager(Employee):
    def __init__(self, first, last, department, pay, level, zone, employees = None):
        super().__init__(first, last, department, pay, level)
        self.zone = zone
        self.employees = employees

emp_1 = Employee('Efe', 'Obasuyi', 'Admin', 200000, 400)
emp_2 = Developer('David', 'Obasuyi', 500, 'HR', 150000, 'Python')
manager_1 = manager('Elon', 'Musk', 'Executive', 1000000, 1000, 'kaduna', ['David', 'John', 'Emmannuel','oghogho', 'Cathrine', 'Sandra'])
'''print(Employee.raise_amount)
print(manager_1.__dict__)'''

