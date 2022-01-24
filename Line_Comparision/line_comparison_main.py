import logging
import math
from filecmp import cmp

logging.basicConfig(filename="address_book_log.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')


class LineCompaisionMain:
    def calculate_length(self, x1, x2, y1, y2):
        """

        :param x1: x1 Coordinate
        :param x2: x2 Coordinate
        :param y1: y1 Coordinate
        :param y2: y2 Coordinate
        :return: Length of Line
        """
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    def check_equality(self, line1, line2):
        """

        :param line1:
        :param line2:
        :return: True if Equal and False if Not Equal
        """
        if line1 == line2:
            return True
        else:
            return False

    def comparison_method(self, line1, line2):
        """

        :param line1: length of line 1
        :param line2: length of line 2
        :return: cmp value 0,1,-2
        """
        if line1 > line2:
            return 1
        if line1 == line2:
            return 0
        if line1 < line2:
            return -1


if __name__ == "__main__":
    try:
        line = LineCompaisionMain()
        print(line.calculate_length(2, 3, 3, 2))
        print(line.check_equality(line.calculate_length(2, 3, 3, 2), line.calculate_length(2, 3, 3, 2)))
        print(line.comparison_method(line.calculate_length(1, 12, 3, 2), line.calculate_length(1, 2, 33, 2)))
    except TypeError as te:
        print(te)
        logging.error(te)
    except Exception as e:
        logging.error(e)
