#!/usr/bin/python

"""DataPlotter.

Usage:
    DataPlotter.py [options]... DATA

Options:
    -h -? --help                                     Show this screen.
    -v --version                                     Show version.

"""

import docopt
import matplotlib.pyplot as plt
import pandas as pd
import os


################################################################################
################################################################################
if __name__ == "__main__":
  Args = docopt.docopt(__doc__, version =1.0)

  if not os.path.exists(Args['DATA']):
    print Args['DATA'], 'is not found'

  Data = pd.read_csv(Args['DATA'], header=None)

  if not os.path.exists('ReferenceProfile.csv'):
    print 'ReferenceProfile.csv not found'

  ReferenceData = pd.read_csv('ReferenceProfile.csv', header=None)

  plt.plot(Data[0], Data[2], label='New Data', color='r', linewidth=3)

  plt.plot(ReferenceData[0], ReferenceData[1], label='Reference Data', color='b', linewidth=3)

  plt.legend()

  plt.show()
