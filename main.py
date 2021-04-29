import codeforces_api
import time
from try_ import _try_
import itertools


class Parcer():

    def __init__(self):
        self.handle = "sheryaroslam"  # имя пользователя
        self.time = time.time()  # текущее время
        self.session = codeforces_api.CodeforcesApi()  # создание сессии
        self.tryes = self.session.user_status(self.handle)  # список всех попыток пользователя

    def get_sucses(self):  # заполняем массивы id решений и задач
        problems = []  #список проблем(объект _try_ с полями id и solve) solve - номер решения id - номер задачи
        for t in self.tryes:
            if (self.time - t.creation_time_seconds > 0) and (t.verdict == 'OK'):
                problems.append(_try_(t.contest_id, t.id, t.problem.index))
        problems = [el for el, _ in itertools.groupby(problems)]
        return problems

    def get_url_of_sucsess(self, problems): #создает массив со ссылками на решения
        URLS = []
        count_id = len(problems)-1
        for i in range(count_id):
            URLS.append("https://codeforces.com/contest/" + str(problems[i].get_problem("id")) + "/submission/"
                             + str(problems[i].get_problem("solve")))
        URLS = [el for el, _ in itertools.groupby(URLS)]
        return URLS
