#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY format

import shutil, os, re

#Regex that matches American date format MM-DD-YYYY
datePatter = re.compile("""^(.*?)	# all text before the date
	((0|1)?\d)-			# one or two digits for the month
	((0|1|2|3)?\d)-			# one or two digits for the day
	((19|20)\d\d)			# four digits for the year
	(.*?)$				# all text after the date
	""", re.VERBOSE)

#Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
	mo = datePattern.seach(amerFilename)

	#skip files without a date
	if mo == None:
		continue

	# Get different parts of the filename
	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)

	# Form the European-style filename
	euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

	# get the full, absolute filepaths
	absWorkingDir = os.path.abspath('.')
	amerFilename = os.path.join(absWorkingDir, amerFilename)
	euroFilename = os.path.join(absWorkingDir, euroFilename)

	# rename the files
	print('Renaming "%s" to "%s"...' % (amerFilenames, euroFilename))
	#shutil.move(amerFilename, euroFilename) # UNCOMMENT AFTER TESTING


