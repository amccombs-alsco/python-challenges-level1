import unittest
import num2word
from challengefour.numbertoword import num_to_word


class fibi(unittest.TestCase, object):
    def set_up(self):
        pass

    def numberGame(self, n):
        a = 0
        b = 1
        for i in range(n - 1):
            c = a + b
            a = b
            b = c
            print(c, '-', num_to_word(c))

    def test_the_process(self):
        self.numberGame(10)

    if __name__ == '__main__':
        unittest.main()
