import logging

from classroom import Classroom


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


cr = Classroom(7, 3, 3)
cr.create_students()
cr.place_students()