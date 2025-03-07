import unittest
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from student_list import StudentManagement

class TestStudentList(unittest.TestCase):
    def test_add_student(self):
        student_management = StudentManagement()
        self.assertEqual(student_management.add_student("1", "John_Snow", 25), True)
        self.assertEqual(student_management.add_student("2", "Arya_Stark", 0), False)
        self.assertEqual(student_management.add_student("3", "Sansa_Stark", -30), False)
        self.assertEqual(student_management.add_student("4", "Bran_Stark", 2250), False)
        print("\nTest add_student passed")

    def test_update_student(self):
        student_management = StudentManagement()
        student_management.add_student("1", "John_Snow", 25)
        student_management.update_student("1", "Arya_Stark", 23)
        self.assertNotEqual(student_management.student_list[0]['name'], "John_Snow")
        self.assertNotEqual(student_management.student_list[0]['age'], 25)
        self.assertEqual(student_management.update_student("2", "Arya_Stark", 23), False)
        self.assertEqual(student_management.update_student("1", "Arya_Stark", 50), True)
        self.assertEqual(student_management.update_student("1", "Arya_Stark", 0), False)
        self.assertEqual(student_management.update_student("1", "Sansa_Stark", -30), False)
        self.assertEqual(student_management.update_student("1", "Bran_Stark", 2250), False)
        print("\nTest update_student passed")

    def test_remove_student(self):
        student_management = StudentManagement()
        student_management.add_student("1", "John_Snow", 25)
        student_management.remove_student("1")
        student_management.remove_student("1")
        self.assertEqual(student_management.student_list, [])
        print("\nTest remove_student passed")

    def test_add_grade(self):
        student_management = StudentManagement()
        student_management.add_student("1", "John_Snow", 25)
        self.assertEqual(student_management.add_grade("1", "Math", 2.0), True)
        self.assertEqual(student_management.add_grade("1", "Math", 3.2), False)
        self.assertEqual(student_management.add_grade("2", "Math", 3.0), False)
        print("\nTest add_grade passed")
    
    def test_avr_grade(self):
        student_management = StudentManagement()
        student_management.add_student("1", "John_Snow", 25)
        student_management.add_grade("1", "Math", 2.0)
        student_management.add_grade("1", "Math", 3.0)
        student_management.add_grade("2", "Math", 5.0)
        self.assertEqual(student_management.avg_grades("Math"), 2.5)
        self.assertNotEqual(student_management.avg_grades("Math"), 5.0)
        self.assertEqual(student_management.avg_grades("History"), 0.0)
        print("\nTest avg_grades passed")


if __name__ == '__main__':
    unittest.main()
