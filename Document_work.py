import os
import requests
from bs4 import BeautifulSoup
from const import *



class File_worker():

    def __init__(self, problems, URSL):
        self.problems = problems
        self.URLS = URSL

    def create_file(self, path): #создание файла <номерзадачи сложность>.txt
        if not os.path.isdir(path):
            os.mkdir(path)

        for problem in self.problems:
            new_file = open(path+"{id}{difficult}.txt".format(id=problem.problem_id, difficult=problem.difficult), "w")
            new_file.close()


    def fiil_file(self, path): #заполняет тхт файл кодом
        len_ = len(self.URLS)-1
        for i in range(len_):
            response = requests.get(self.URLS[i])
            soup = BeautifulSoup(response.text, 'lxml')
            if(i>=1) and (self.problems[i].problem_id == self.problems[i-1].problem_id):
                continue
            else:
                file = open(path+"{id}{difficult}.txt".format(id=self.problems[i].problem_id, difficult=self.problems[i].difficult), "w")
                quotes = soup.find_all('pre', class_="prettyprint lang-c linenums program-source")
                for quote in quotes:
                    file.write(quote.text)
                file.close()

    def rename_to(self, path): #создает из тхт файла файл с нужным расщирением
        for problem in self.problems:
            try:
                os.rename(path+"{id}{difficult}.txt".format(id=problem.problem_id, difficult=problem.difficult),
                      path+"{id}{difficult}.{lang}".format(id=problem.problem_id, difficult=problem.difficult,
                                                                 lang=LANGUAGES[problem.lagnuage]))
            except(FileNotFoundError):
                continue

