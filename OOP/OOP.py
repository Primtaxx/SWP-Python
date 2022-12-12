
from enum import Enum


class Gender(Enum):
    Male = 0
    Female = 1

class Person:
    def __init__(self, first_name, last_name, gender:Gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
    
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name + " " + self.gender

class Abteilungen:
    def __init__(self, d_name):
        self.d_name = d_name

    def __str__(self) -> str:
        return self.d_name


class Mitarbeiter(Person):
    def __init__(self, person, dep):
        super().__init__(person.first_name, person.last_name, person.gender )
        self.dep = dep

class Gruppenleiter(Mitarbeiter):
    def __init__(self, person, dep):
        super().__init__(person, dep)


class Firma:
    def __init__(self, m, dep):
        self.m = m
        self.dep = dep

    def add_department(self, department):
        self.dep.append(department)

    def add_employee(self, employee):
        self.m.append(employee)

    def mcount(self):
        return len(self.m)
    
    def groupcount(self):
        gcount = 0
        for i in range(len(self.m)):
            if type(self.m[i]) == Gruppenleiter:
                gcount += 1
        return gcount

    def department_count(self):
        return len(self.dep)
    
    
    def biggest_department(self):
        dcount = 0
        for i in self.dep:
            temp_count = 0
            for j in self.m:
                if j.dep == i:
                    temp_count += 1
            if temp_count > dcount:
                biggest_dep = i
            dcount = temp_count
        return biggest_dep

    def gendercount(self):
        mcount = 0
        fcount = 0
        for i in self.m:
            if i.gender == Gender.Male:
                mcount += 1
            elif i.gender == Gender.Female:
                fcount +=1
        prozent = str(100.0 * mcount / len(self.m)) + "%" + " " + str(100.0 * fcount / len(self.m)) + "%"
        return prozent

    


def main():
    employeeList = []
    departmentList = []
    company = Firma(employeeList, departmentList)

    p1 = Person("Miguel", "Mayrhofer", Gender.Male)
    p2 = Person("Marie", "Weiss", Gender.Female)
    p3 = Person("Lara", "Mayr", Gender.Female)
    d1 = Abteilungen("Sales")
    d2 = Abteilungen("Marketing")
    m1 = Gruppenleiter(p1, d2)
    m2 = Mitarbeiter(p2, d1)
    m3 = Mitarbeiter(p3, d1)

    company.add_department(d1)
    company.add_department(d2)
    company.add_employee(m1)
    company.add_employee(m2)
    company.add_employee(m3)
    
    print("Prozentanteil Männer/ Frauen: " + str(company.gendercount()))
    print("Mitarbeiter in der Firma: " + str(company.mcount()))
    print("Gruppenleiter in der Firma: " + str(company.groupcount()))
    print("Anzahl der Abteilungen: " + str(company.department_count()))
    print("Größte Abteilung: " + str(company.biggest_department()))

    

if __name__ == '__main__':
    main()


