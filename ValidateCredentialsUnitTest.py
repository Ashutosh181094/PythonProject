import unittest
import ValidateUsernamePassword


class TestCaseUserPasswordValidation(unittest.TestCase):

    def setUp(self):
        self.obj = ValidateUsernamePassword.validateUserNamePassword

    def test_User(self):
        self.assertTrue(self.obj(Username='AshutoshRai@!123.44', Password='').validateUserName())
        self.assertFalse(self.obj(Username='AshutoshRai@!12.44', Password='').validateUserName())
        self.assertFalse(self.obj(Username='AshutoshRai@!1234.44', Password='').validateUserName())
        self.assertTrue(self.obj(Username='AshutoshRai@~123.44', Password='').validateUserName())
        self.assertFalse(self.obj(Username='AshutoshRai@!!123.44', Password='').validateUserName())

    def test_password(self):
        self.assertTrue(self.obj(Username='', Password='Elxop~_!jna146').validatePassword())
        self.assertFalse(self.obj(Username='', Password='Elxop~_!jna111').validatePassword())
        self.assertFalse(self.obj(Username='', Password='Elxop~_!jna123').validatePassword())
        self.assertTrue(self.obj(Username='', Password='Elxop~_!jna785').validatePassword())
        self.assertFalse(self.obj(Username='', Password='Elxop~!jna146').validatePassword())

    def test_Count_Capital_Letter(self):
        self.assertEqual(self.obj(Username='AshutoshRai@!123.44', Password='').countCapitalLetters(), True)
        self.assertEqual(self.obj(Username='AsHhutoshRai@!123.44', Password='').countCapitalLetters(), False)

    def testCountSpecialCharacters(self):
        self.assertEqual(self.obj(Username='AshutoshRai@!123.44', Password='').countSpecialCharacters(), True)
        self.assertEqual(self.obj(Username='AshutoshRai@@!123.44', Password='').countSpecialCharacters(), False)

    def testFloatNumbers(self):
        self.assertEqual(self.obj(Username='AshutoshRai@!1234.44', Password='').ValidateFloatNumber(), False)
        self.assertEqual(self.obj(Username='AshutoshRai@!123.44', Password='').ValidateFloatNumber(), True)
        self.assertEqual(self.obj(Username='AshutoshRai@!12.44', Password='').ValidateFloatNumber(), False)
        self.assertEqual(self.obj(Username='AshutoshRai@!123.4', Password='').ValidateFloatNumber(), False)
        self.assertEqual(self.obj(Username='AshutoshRai@!', Password='').ValidateFloatNumber(), False)


