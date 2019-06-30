#from behaviour import Behaviour


class Student(object):

    def __init__(self, name, empty=False):
        self.name = name
        self.empty = empty

        #self.behaviour = Behaviour()

    def __hash__(self):
        if self.empty:
            return 'empty'
        return hash(self.name)

    def __repr__(self):
        return '{}("{}")'.format(self.__class__.__name__, self.name)