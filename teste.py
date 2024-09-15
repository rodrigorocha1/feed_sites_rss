import math


class SimpleEquation:
    def demo(self, a: int, b: int, c: int) -> object:
        """

        :param int  a:
        :type a: int
        :param b:
        :type b: int
        :param c:
        :type c: int
        """
        d = math.sqrt(abs(b ** 2 - 4 * a * c))
        root1 = (-b + d) / (2 * a)
        root2 = (-b - d) / (2 * a)
        print(root1, root2)


SimpleEquation().demo(1,3,4)