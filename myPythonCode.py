
class Employee(object):
    def __init__(self, fName, lName, address, email):
        self.fName = fName
        self.lName = lName
        self.address = address
        self.email = email

class Developer(Employee):
    def __init__(self, fName, lName, address, email, sal):
        super().__init__(fName, lName, address, email) 
        self.sal = sal




def main():
    emp = Employee("Broom", "Ashami", "1324 S Winchester Blvd apt 121 San Jose, CA 95128")

if __name__ == "__main__":
    main()