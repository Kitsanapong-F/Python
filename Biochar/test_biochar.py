import unittest
from biochar_module import calculate_biochar_ratio

class TestBiocharModule(unittest.TestCase):
    def test_acid_soil(self):
    # คืนเป็นกรด pH 4.5 น้ำหนักรวม 188 กก. สัดส่วนปุ้ยต้องเย็น 38 ก.
        self.assertEqual(
            calculate_biochar_ratio(100, 4.5),30)

    def test_invalid_ph(self):
    # คำ pH ผิดพลาด ต้องโยน ValueError
        with self.assertRaises(ValueError):
            calculate_biochar_ratio(100, 15)

    def test_base_soil(self):
        self.assertEqual(calculate_biochar_ratio(100,8.0),5)

    def test_neutral_soil(self):
        self.assertEqual(calculate_biochar_ratio(100,6.5),15)
    
if __name__ == "__main__": unittest.main()
