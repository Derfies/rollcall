class Board(object):

    def __init__(self, num_cols, solution):
        self.num_cols = num_cols
        #self.num_rows = num_rows

        #print 'solution', solution

        #sorted_items = sorted(solution.items(), key=lambda x: x[0])
        #students = map(lambda x: x[1], sorted_items)

        # print students

        students = [solution[i] for i in range(len(solution.keys()))]

        # array_ = []
        # i = 0
        # for x in range(self.num_cols):
        #     row = []
        #     for y in range(self.num_rows):
        #         row.append(solution[i])
        #         i += 1
        #     array_.append(row)

        # self._data = array_
        # print self._data

        self._data = []
        for i in range(0, len(students), self.num_cols):
            self._data.append(students[i:i + self.num_cols])

    def __str__(self):
        lines = []#'-' * 35 + '\n']
        for x in range(len(self._data)):
            row_format = '{:>20}' * len(self._data[x])
            lines.append(row_format.format(*self._data[x]))
            #lines.append('\n')
        #lines.append('-' * 35)
        return '\n'.join(lines)