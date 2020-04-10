from one_kyu import *
from two_kyu import *
from three_kyu import *
from four_kyu import *
from five_kyu import *
from six_kyu import *
from seven_kyu import *
from eight_kyu import *
import unittest

suite = unittest.TestLoader().loadTestsFromModule(seven_kyu)
unittest.TextTestRunner(verbosity=2).run(suite)
