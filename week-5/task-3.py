class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def introduction(self):
        return f"I am {self._name}, {self._age} years old."

class Student(Person):
    def __init__(self, name, age, sid):
        super().__init__(name, age)
        self.sid = sid
    def introduction(self):
        return f"Student {self._name}, ID: {self.sid}"

def main():
    p = Person("John", 40)
    s = Student("Alice", 20, "123")
    print(p.introduction())
    print(s.introduction())

main()