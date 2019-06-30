class Board(object):

    def __init__(self, students, num_cols):
        self.students = students
        self.num_cols = num_cols

    def __str__(self):
        rows = []
        for i in range(0, len(self.students), self.num_cols):
            row_format = '{:>20}' * self.num_cols
            row_students = self.students[i:i + self.num_cols]
            rows.append(row_format.format(*row_students))
        return '\n'.join(rows)

    def left_of(self, student):
        # print '-' * 35
        # print self.students
        # print 'num_cols:', self.num_cols
        idx1 = self.students.index(student)
        idx2 = idx1 - 1
        if idx2 > -1:


            row_idx1 = int(float(idx1) / self.num_cols)
            row_idx2 = int(float(idx2) / self.num_cols)

            # print 'students:', self.students
            # print '    idx1:', idx1
            # print '    idx2:', idx2
            # print '    row_idx1:', row_idx1
            # print '    row_idx2:', row_idx2

            if row_idx1 == row_idx2:
                return self.students[idx2]
        
        return None

        # print 'student', student, '->', idx1, ':', idx2
        # if idx2 >= 0:
        #     #print '    ', idx1 % self.num_cols, idx2 % self.num_cols
        #     row_idx1 = int(float(idx1) / 3)
        #     row_idx2 = int(float(idx2) / 3)
        #     print row_idx1, row_idx2

    def right_of(self, student):
        idx1 = self.students.index(student)
        idx2 = idx1 + 1
        if idx2 < len(self.students):
            row_idx1 = int(float(idx1) / self.num_cols)
            row_idx2 = int(float(idx2) / self.num_cols)
            if row_idx1 == row_idx2:
                return self.students[idx2]
        return None

    def is_next_to(self, s1, s2):
        return self.left_of(s1) == s2 or self.right_of(s1) == s2

    def is_alone(self, s):
        left_of = self.left_of(s)
        right_of = self.right_of(s)
        return (left_of is None or left_of.empty) and (right_of is None or right_of.empty)


if __name__ == '__main__':
    b = Board(['foo', 'bar'], 2)
    print b
    for student in b.students:
        print '{} is left of {}'.format(b.left_of(student), student)
    print '-' * 80

    b = Board(['foo', 'bar', 'baz'], 3)
    print b
    for student in b.students:
        print '{} is left of {}'.format(b.left_of(student), student)
    print '-' * 80

    b = Board(['foo', 'bar', 'baz', 'quiz', 'quark', 'quack'], 3)
    print b
    for student in b.students:
        print '{} is left of {}'.format(b.left_of(student), student)
    print '-' * 80