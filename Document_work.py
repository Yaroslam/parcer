from main import Parcer
import os
import requests
from bs4 import BeautifulSoup


class File_worker():

    def __init__(self):
        self.problems = Parcer().get_sucses()
        self.URLS = Parcer().get_url_of_sucsess(self.problems)
        self.create_file()
        self.fiil_file()
        self.rename_to_c()

    def create_file(self):
        if not os.path.isdir("C://folder"):
            os.mkdir("C://folder")
        i = 0
        for problem in self.problems:
            new_file = open("C://folder/{id}{difficult}.txt".format(id=problem.problem_id, difficult=problem.difficult), "w")
            new_file.close()


    def fiil_file(self):
        len_ = len(self.URLS)-1
        for i in range(len_):
            response = requests.get(self.URLS[i])
            soup = BeautifulSoup(response.text, 'lxml')
            if(i>=1) and (self.problems[i].problem_id == self.problems[i-1].problem_id):
                continue
            else:
                file = open("C://folder/{id}{difficult}.txt".format(id=self.problems[i].problem_id, difficult=self.problems[i].difficult), "w")
                quotes = soup.find_all('pre', class_="prettyprint lang-c linenums program-source")
                for quote in quotes:
                    file.write(quote.text)
                file.close()
            print(i)

    def rename_to_c(self):
        for problem in self.problems:
            try:
                os.rename("C://folder/{id}{difficult}.txt".format(id=problem.problem_id, difficult=problem.difficult),
                      "C://folder/{id}{difficult}.c".format(id=problem.problem_id, difficult=problem.difficult))
            except(FileNotFoundError):
                continue


File_worker()