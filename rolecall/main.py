import logging

from klass import Klass


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


klass = Klass(9, (3, 3))
klass.create_students()