#! /usr/bin/python

###########################################################################
# Program     : s3keygen
# Description : Generates a unique s3 key to overcome race conditions
###########################################################################

import argparse
from datetime import date
from dateutil import relativedelta
import sys
import os

inception_year=1970
inception_month=01
inception_date=01

hash={
0:'0',
1:'1',
2:'2',
3:'3',
4:'4',
5:'5',
6:'6',
7:'7',
8:'8',
9:'9',
10:'a',
11:'b',
12:'c',
13:'d',
14:'e',
15:'f',
16:'g',
17:'h',
18:'i',
19:'j',
20:'k',
21:'l',
22:'m',
23:'n',
24:'o',
25:'p',
26:'q',
27:'r',
28:'s',
29:'t',
30:'u',
31:'v',
32:'w',
33:'x',
34:'y',
35:'z'
}



def generate_s3hashkey(ddate):

	#extract date, week, month index
	yyyymmdd = str(ddate).replace('-','')
	year = yyyymmdd[:4]
	month = yyyymmdd[4:6]
	dt = yyyymmdd[6:8]
	cur_date = date(int(year), int(month), int(dt))
	
	# Get Delta
	inception_ddate = date(inception_year, inception_month, inception_date)
	delta = cur_date - inception_ddate

	ndays = delta.days
	nday_ind = ndays % 36

	nweeks = int(ndays/7)
	nweeks_ind = nweeks % 36

	rdelta = relativedelta.relativedelta(cur_date, inception_ddate)
	
	nyears = rdelta.years
	nyears_ind = nyears % 36

	nmonths = rdelta.months
	nmonths_ind = nmonths % 36

	print ndays, nday_ind, nweeks, nweeks_ind, nmonths, nmonths_ind
	s3hashkey = str(hash[nday_ind]) + str(hash[nweeks_ind]) + str(hash[nmonths_ind]) + yyyymmdd[::-1]
	return s3hashkey

if __name__ == "__main__":

    try:
        parser = argparse.ArgumentParser(add_help=True, description='Process the input params')
        parser.add_argument('--date', dest='ddate', help='input date in yyyy-mm-dd or yyyymmdd format')
        args = parser.parse_args()

        if args.ddate is None:
        	print "\nERROR: Enter input date in yyyy-mm-dd or yyyymmdd format \n"
        	parser.parse_args(['-h'])
        	sys.exit(1)

        s3hashkey = generate_s3hashkey(args.ddate)
        print s3hashkey

    except Exception as e:
    	print "Oops! Something went wrong..."
    	print str(e)