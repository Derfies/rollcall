import logging

import constraint

from const import STUDENT_NAMES
from student import Student
from board import Board


logger = logging.getLogger(__name__)


class Classroom(object):


    def __init__(self, num_students, num_cols, num_rows):
        self.num_students = num_students
        self.num_cols = num_cols
        self.num_rows = num_rows

        assert self.num_students <= self.num_cols * self.num_rows, 'More students than there are chairs!'

        self.students = []

    def create_students(self):
        for i in range(self.num_students):
            name = STUDENT_NAMES[i]
            self.students.append(Student(name))
            logger.debug('Created student: "{}"'.format(name))

        if self.num_students < self.num_cols * self.num_rows:
            empty = Student('EMPTY', empty=True)
            for i in range(self.num_students, self.num_cols * self.num_rows):
                self.students.append(empty)
                logger.debug('Creating empty chair')

    def seat_constraint(self, *args, **kwargs):

        # Constraint that returns permutations where:
        # - The number of non-empty chairs equals the number of students
        # - No student is duplicated
        non_empty = filter(lambda x: not x.empty, args)
        return len(non_empty) == self.num_students and len(non_empty) == len(set(non_empty))

    def loner_constaint(self, *students):
        #print '->', students
        b = Board(students, self.num_cols)
        #is_next_to = b.is_next_to(self.students[0], self.students[1])
        #if left_of is not None:
        #print b
        #print '{} is_next_to {} == {}'.format(self.students[0], self.students[1], is_next_to)
        #print '-' * 35

        is_alone = b.is_alone(self.students[3])
        #print '{} is_alone: {}'.format(self.students[0], is_alone)

        return is_alone

    def friends(self, *students):
        #print '->', students
        b = Board(students, self.num_cols)
        #is_next_to = b.is_next_to(self.students[0], self.students[1])
        #if left_of is not None:
        #print b
        #print '{} is_next_to {} == {}'.format(self.students[0], self.students[1], is_next_to)
        #print '-' * 35

        is_next_to = b.is_next_to(self.students[0], self.students[1])
        #print '{} is_next_to: {}: {}'.format(self.students[0], self.students[1], is_next_to)

        return is_next_to

    def enemies(self, *students):
        b = Board(students, self.num_cols)
        is_next_to = b.is_next_to(self.students[1], self.students[2])
        #print '{} is_next_to: {}: {}'.format(self.students[1], self.students[2], is_next_to)
        return not is_next_to

    def place_students(self):
        problem = constraint.Problem()
        problem.addVariables(range(self.num_cols * self.num_rows), self.students)
        problem.addConstraint(constraint.FunctionConstraint(self.seat_constraint))
        problem.addConstraint(constraint.FunctionConstraint(self.loner_constaint))
        problem.addConstraint(constraint.FunctionConstraint(self.friends))
        problem.addConstraint(constraint.FunctionConstraint(self.enemies))
        
        solution = problem.getSolution()
        print 'solution:', solution
        students = [solution[i] for i in range(len(solution.keys()))]
        b = Board(students, self.num_cols)
        print b
        print '-' * 35
        '''
        sols = problem.getSolutions()
        unique_sols = [i for n, i in enumerate(sols) if i not in sols[n + 1:]]
        print len(unique_sols)
        for solution in unique_sols:
            students = [solution[i] for i in range(len(solution.keys()))]
            b = Board(students, self.num_cols)
            print b
            print '-' * 35
            #print b.left_of(self.students[0])
        #print self._solution_to_array(unique_sols[0])

        '''