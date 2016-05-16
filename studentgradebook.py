# Student Grade Book Application

class Student(object):

    def __init__(self, name, average, scores):
        self.name = name
        self.average = 0
        self.scores = scores

    def add_score(self, score):
        self.scores.append(score)
