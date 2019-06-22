import logging

from const import STUDENT_NAMES
from student import Student


logger = logging.getLogger(__name__)


class Klass(object):


    def __init__(self, num_students, dimensions):
        self.num_students = num_students
        self.num_cols = dimensions[0]
        self.num_rows = dimensions[1]

        assert self.num_students <= self.num_cols * self.num_rows, 'More students than there are chairs!'

        self.students = []

    def create_students(self):
        for i in range(self.num_students):
            name = STUDENT_NAMES[i]
            self.students.append(Student(name))
            logger.debug('Created student: "{}"'.format(name))