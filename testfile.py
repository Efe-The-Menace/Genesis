class stafff:
  def __innit__(self, first, last, age, department):
    self.first = first
    self.age = age
    self.department = department
    self.last = last

    def intro(self):
      return '{} {}'.format(self.first, self.last)
    
class Developer(stafff):
  def __init__(self, first, last, department, pay, age, level, pro_lang):
        super().__init__(first, last, age, department)
        self.pro_lang = pro_lang
        self.level = level
        self.pay = pay
    
emp1 = stafff('david', 'oba', 20, 'HR')