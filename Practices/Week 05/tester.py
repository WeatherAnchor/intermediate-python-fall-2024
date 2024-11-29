import pandas as pd
import unittest
import employee
import student

class TestEmployee(unittest.TestCase):
<<<<<<< HEAD
=======
    @classmethod
    def setUpClass(cls):
        print("Employee Test Started")

    @classmethod
    def tearDownClass(cls):
        print("Employee Test Finished")

    def setUp(self):
        self.df = pd.read_csv("sample_employees.csv")
        print("Setting up an Employee class")
    
>>>>>>> 245a7f8b346fa98eb4c38d218c9324fb357809f6
    def test_get_fullname(self):
        # "bob marley"
        firstname = 'Bob'
        lastname = 'Marley'
        self.assertTrue(employee.get_fullname(firstname, lastname), 
                        f"{firstname.lower()} {lastname.lower()}")

    def test_get_average(self):
<<<<<<< HEAD
        df = pd.read_csv("sample_employees.csv")
        salary = df['salary']
=======
        salary = self.df['salary']
>>>>>>> 245a7f8b346fa98eb4c38d218c9324fb357809f6

        self.assertTrue(employee.get_average(salary),
                        salary.mean())

class TestStudent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Student Test Started")

    @classmethod
    def tearDownClass(cls):
        print("Student Test Finished")

    def setUp(self):
        self.df = pd.read_csv("sample_students.csv")
        print("Setting up a Student class")
    
    def test_get_max_grade(self):
        grade = self.df['grade']
        self.assertTrue(student.get_max_grade(grade), grade.max())

    def test_get_min_grade(self):
        grade = self.df['grade']
<<<<<<< HEAD
        self.assertTrue(student.get_min_grade(grade), grade.min())
=======
        self.assertTrue(student.get_min_grade(grade), grade.min())
    

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
        
>>>>>>> 245a7f8b346fa98eb4c38d218c9324fb357809f6
