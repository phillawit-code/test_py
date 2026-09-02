import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import test_func

test_func.main()

def hello():
    world()

def world():
    print("Hello, world")

hello

print('')