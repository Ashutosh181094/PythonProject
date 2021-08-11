from string import punctuation
from english_words import english_words_set
import re
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="UserPasswordValidation.log", level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger()


class validateUserNamePassword:

    def __init__(self, Username, Password):
        self.UserName = Username
        self.Password = Password

    def validateUserName(self):

        if self.ValidateFloatNumber() and self.countCapitalLetters() and self.countSpecialCharacters():
            return True
        return False

    def countCapitalLetters(self):
        '''
        function to countCapital Letters
       '''
        countCapital = 0
        for i in self.UserName:
            if ord(i) in range(65, 90):
                countCapital = countCapital + 1
        if countCapital == 2:
            return True
        return False

    def countSpecialCharacters(self):
        '''
        Function to Count Special Characters
        '''
        countOfSpecialCharacter = 0
        for ch in self.UserName:
            if ch == '@' or ch == '#' or ch == '!' or ch == '~':
                countOfSpecialCharacter = countOfSpecialCharacter + 1
        if countOfSpecialCharacter == 2:
            return True
        else:
            return False
        pass

    def ValidateFloatNumber(self):
        '''
        Function to Validate if the float number is of 5 digits with 2 digits in decimal part
        '''
        if self.UserName.find('.'):
            check1 = self.UserName[self.UserName.find('.') - 3:self.UserName.find('.')]
            check2 = self.UserName[self.UserName.find('.') + 1:self.UserName.find('.') + 3]
            check3 = self.UserName[self.UserName.find('.') - 4:self.UserName.find('.') - 3].isdigit()
            check4 = self.UserName[self.UserName.find('.') + 3:self.UserName.find('.') + 4].isdigit()
            if len(check1) == 3 and len(check2) == 2 and check1.isdigit() == True and check2.isdigit()==True and check3 != True and check4 != True:
                return True
            else:
                return False

    def validatePassword(self):
        '''
        Function to Validate Pass
        '''
        countSpecialCharacter = 0
        countLowerCase = 0
        countUpperCase = 0

        if not (12 <= len(self.Password) <= 18):
            return False

        for character in self.Password:
            if ord(character) in range(65, 90):
                countUpperCase += 1
            elif ord(character) in range(97, 122):
                countLowerCase += 1
            elif character in list(set(punctuation)):
                countSpecialCharacter += 1

        if not (countSpecialCharacter == 3 and countLowerCase >= 1 and countUpperCase >= 1 and '_' in self.Password and
                self.Password[0] != '_' and self.Password[-1] != '_'):
            return False

        for word in english_words_set:
            if self.Password.find(word) != -1 and len(word) > 1:
                return False

        listOfThreeDigitNum = re.findall(r'\d{3}', self.Password)
        for ThreeDigitNum in listOfThreeDigitNum:
            if repeatingDigitcheck(ThreeDigitNum) == False:
                return False
            if sequentialDigitCheck(ThreeDigitNum) == False:
                return False

        return True


def repeatingDigitcheck(Value):
    '''
    Function to check if Digits are repeating
    '''
    listNumber = []
    for ch in Value:
        if ch in listNumber:
            return False
        else:
            listNumber.append(ch)
    return True


def sequentialDigitCheck(Value):
    '''
    Function to check if digits are in sequence
    '''
    previousValue = 0
    currentValue = 0
    countDifference = 0
    diff = 0
    count = 0
    valueLength = len(Value)
    for ch in Value:
        previousValue = currentValue
        currentValue = int(ch)
        diff = currentValue - previousValue
        if diff == 1:
            countDifference += 1

    if countDifference == valueLength:
        return False

    return True


def validatePassedUserNamePassword(username: str, password: str):
    obj = validateUserNamePassword(Username=username, Password=password)
    print(obj.validateUserName())
    # print(obj.validateUserName() and obj.validatePassword())


#validatePassedUserNamePassword(username='AshutoshRai@!123.44', password='')
