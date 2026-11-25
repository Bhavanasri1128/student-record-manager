import os
import unittest
from records import add_student, rank_by_marks, save_records, load_records

class TestStudentRecords(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_students.txt"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_ranking_highest_to_lowest(self):
        students = {
            "101": {"name": "Anitha", "marks": 88, "attendance": 85.0},
            "102": {"name": "Sneha", "marks": 92, "attendance": 90.0}
        }
        ranked = rank_by_marks(students)
        # rank_by_marks returns tuples: (marks, name, roll_no, attendance)
        self.assertEqual(ranked[0][1], "Sneha")
        self.assertEqual(ranked[0][0], 92)
        self.assertEqual(ranked[1][1], "Anitha")

    def test_file_persistence(self):
        students = {"101": {"name": "Ravi", "marks": 76, "attendance": 72.0}}
        save_records(students, self.test_file)
        loaded = load_records(self.test_file)
        self.assertEqual(loaded["101"]["name"], "Ravi")
        self.assertEqual(loaded["101"]["attendance"], 72.0)

if __name__ == "__main__":
    unittest.main()
