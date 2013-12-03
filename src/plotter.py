# -*- encoding: utf-8 -*-

"""plot_handler.py: Gets statistics and draws plots."""

"""
__author__      = "Marco Sacristão, Jorge Batista"
__copyright__   = "Copyright 2013, ESTIG - IPBeja"
__license__ 	= "GPL"
__version__		= "1.0.0"
__maintainer__	= "Jorge Batista"
__email__		= "dwjorgeb@gmail.com"
__status__		= "Development"
"""

from pylab import *


class plot:

	def __init__(self, tile, lbls, percs, expls):

		# make a square figure and axes
		figure(1, figsize=(6,6))
		ax = axes([0.1, 0.1, 0.8, 0.8])

		# The slices will be ordered and plotted counter-clockwise.
		labels = lbls
		fracs = percs
		explode = expls

		pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
		                # The default startangle is 0, which would start
		                # the Frogs slice on the x-axis.  With startangle=90,
		                # everything is rotated counter-clockwise by 90 degrees,
		                # so the plotting starts on the positive y-axis.

		title(tile)

		show()