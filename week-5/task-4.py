class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    def get_salary(self):
        return self._salary
    def get_role(self):
        return "Employee"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def get_role(self):
        return "Manager"
    def get_bonus(self):
        return self.bonus

def show_slaves(slaves):
    for e in slaves:
        print(f"{e.name} is {e.get_role()}. Their salary is {e.get_salary()} zimbabwean dollars.")

def main():
    employee = Employee("Sara", 5000)
    manager = Manager("Mike", 8000, 1000)
    slaves = [employee, manager]
    show_slaves(slaves)

main()