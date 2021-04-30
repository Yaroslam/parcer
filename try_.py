class _try_():
    def __init__(self, id, solve, difficult, language):
        self.problem_id = id
        self.problem_solve = solve
        self.difficult = difficult
        self.lagnuage = language

    def get_problem(self, whatGet):
        if whatGet == "id":
            return self.problem_id
        elif whatGet == "solve":
            return self.problem_solve
        elif whatGet == "difficult":
            return self.difficult
        elif whatGet == "language":
            return self.lagnuage