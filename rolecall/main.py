import logging

from classroom import Classroom


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


cr = Classroom(4, (2, 2))
cr.create_students()
cr.place_students()