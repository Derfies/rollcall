import logging

import constraint

from const import STUDENT_NAMES
from student import Student


logger = logging.getLogger(__name__)


class Classroom(object):


    def __init__(self, num_students, dimensions):
        self.num_students = num_students
        self.num_cols = dimensions[0]
        self.num_rows = dimensions[1]

        assert self.num_students <= self.num_cols * self.num_rows, 'More students than there are chairs!'

        self._board = []
        self._students = []

    def create_students(self):
        for i in range(self.num_students):
            name = STUDENT_NAMES[i]
            self._students.append(Student(name))
            logger.debug('Created student: "{}"'.format(name))

        if self.num_students < self.num_cols * self.num_rows:
            logger.debug('Creating empty chair')
            empty = Student('EMPTY', empty=True)
            for i in range(self.num_students, self.num_cols * self.num_rows):
                self._students.append(empty)

    def seat_constraint(self, *args, **kwargs):
        non_empty = filter(lambda x: not x.empty, args)
        #print len(non_empty), len(set(non_empty)), non_empty, args
        return len(non_empty) == self.num_students and len(non_empty) == len(set(non_empty))

    def place_students(self):
        problem = constraint.Problem()
        problem.addVariables(range(self.num_cols * self.num_rows), self._students)
        problem.addConstraint(constraint.FunctionConstraint(self.seat_constraint))
        sols = problem.getSolutions()
        unique_sols = [i for n, i in enumerate(sols) if i not in sols[n + 1:]]
        print len(unique_sols)
        for sol in unique_sols:
            print sol