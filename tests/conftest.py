import sys
from os.path import abspath, dirname, join

ROOT = dirname(abspath(__file__))
UTILS = join(ROOT, 'utils')
sys.path.append(UTILS)
