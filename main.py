import codeforces_api
import time
import itertools
from try_ import _try_


class Parcer():

    def __init__(self, handle):
        self.handle = handle  # имя пользователя
        self.time = time.time()  # текущее время
        self.session = codeforces_api.CodeforcesApi()  # создание сессии
        self.tryes = self.session.user_status(self.handle)  # список всех попыток пользователя

    def get_sucses(self, time_limit):  # заполняем массивы id решений и задач
        problems = []  #список проблем(объект _try_ с полями id, solve, difficult, language) solve - номер решения id - номер задачи difficult - класс задачи
        for t in self.tryes:
            if (self.time - t.creation_time_seconds > int(time_limit)) and (t.verdict == 'OK'):
                problems.append(_try_(t.contest_id, t.id, t.problem.index, t.programming_language))
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
