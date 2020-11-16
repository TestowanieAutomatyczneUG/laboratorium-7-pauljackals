import unittest
import json
from ex1_valid_password.ex1_valid_password import ValidPassword


class TestValidPassword(unittest.TestCase):
    def setUp(self):
        self.tmp_valid_password = ValidPassword()

    def test_from_file(self):
        def string_to_bool(string):
            if string == 'True':
                return True
            elif string == 'False':
                return False

        def remove_quotation_marks(string):
            string_new = string
            if string_new[0] == "'":
                string_new = string_new[1:]
            if string_new[-1] == "'":
                string_new = string_new[:-1]
            return string_new

        file_test = open("data/ex1_data.txt")
        for line in file_test:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.rsplit(" ", 1)
                inp, result = remove_quotation_marks(data[0]), string_to_bool(data[1].strip("\n"))
                self.assertEqual(self.tmp_valid_password.valid_password(inp), result)
        file_test.close()

    def test_from_file_error(self):
        def convert_string(string):
            if string[0] != "'" or string[-1] != "'":
                return json.loads(string)

        def convert_error(string):
            if string == 'ValueError':
                return ValueError
        file_test = open("data/ex1_data_err.txt")
        for line in file_test:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.rsplit(" ", 1)
                inp, result = convert_string(data[0]), convert_error(data[1].strip("\n"))
                with self.assertRaises(result):
                    self.tmp_valid_password.valid_password(inp)
        file_test.close()


if __name__ == '__main__':
    unittest.main()
