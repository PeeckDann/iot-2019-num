from manager.middle_rectangles_method import middle_rectangles_method, f, F
import math

if __name__ == '__main__':
    print('RES=', middle_rectangles_method(f, 0, math.pi))
    print(' I =', F(math.pi) - F(0))
