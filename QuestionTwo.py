import logging
import re

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="StringParser.log", level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger()


class SecondQuestion:

    def __init__(self, data):
        self.data = data

    def getPositionListForString(self, stringExpression):

        listOfPosition = [i for i in range(len(self.data)) if self.data.startswith(stringExpression, i)]

        return listOfPosition

    def getZippedList(self, list1, list2):

        zipped = zip(list1, list2)
        zippedlist = list(zipped)

        return zippedlist

    def findQuestions(self):

        res = self.getPositionListForString('?')
        res2 = self.getPositionListForString('QUESTION')
        zippedlist = self.getZippedList(res, res2)
        for positionTuple in zippedlist:
            end, start = positionTuple
            print(self.data[start:end + 2])

    def findAnswers(self):

        res_answer = self.getPositionListForString('Answer(s):')
        resquestion = self.getPositionListForString('QUESTION')
        zippedlistAnswers = self.getZippedList(resquestion, res_answer)

        for i in zippedlistAnswers:
            start, end = i
            print(self.data[start:start + 11])
            print(self.data[end:end + 13])

    def findReferences(self):

        res_reference = self.getPositionListForString('Reference:')
        newline = '\n'
        for i in res_reference:
            print(self.data[i + 11:self.data.index(newline, i + 11)])

    def findHtmlPagesName(self):

        res_reference = self.getPositionListForString('Reference:')
        s = ''
        newline = '\n'
        for i in res_reference:
            newlineindex = self.data.index(newline, i + 11)
            for j in reversed(range(newlineindex)):
                if self.data[j] == '/':
                    s += self.data[j + 1:newlineindex] + ','
                    break
        print(s[0:len(s) - 1])

    def company_extraction(self):

        dict = {'Enquero': 'Enquero Limited', 'GENPACT': 'Genpact Limited', 'H': 'Hindustan', 'A': 'Aeronautics',
                'L': 'Limited'}
        data = re.sub('Enquero', dict['Enquero'], self.data, flags=re.I)
        data = re.sub('GENPACT', dict['GENPACT'], data, flags=re.I)
        data = re.sub('HAL', dict['H'] + " " + dict['A'] + " " + dict['L'], data, flags=re.I)
        extracted_companies = re.findall(r"Enquero Limited|Genpact Limited|Hindustan Aeronautics Limited", data)

        print([i.strip() for i in extracted_companies])


def QuestionTwo():
    try:
        fileObject = open("input.txt", "r")
        data = fileObject.read()
    except IOError:
        print('file not found')

    obj = SecondQuestion(data)
    obj.findQuestions()
    obj.findAnswers()
    obj.findHtmlPagesName()
    obj.findReferences()
    obj.company_extraction()


QuestionTwo()
