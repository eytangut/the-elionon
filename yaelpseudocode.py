# pseudocode:
# ----------
import os
import urllib.request as url



# A boolean function, that given a file number, returns if it has changed since last check
def checkForChange(fileNumber, fileYear):
	if referenceExists(fileNumber + 'ref'):
		return compareReferenceContentWithCurrentContent(fileNumber)
	else:
		saveToReferenceFile(fileNumber + 'ref', fileYear)
		return False


def saveToReferenceFile(fileNumber, fileYear):
	saveToFile(fileNumber,fileYear)
def saveToFile(fileNumber, fileYear):
	stream = url.urlopen('https://supreme.court.gov.il/Pages/SearchJudgments.aspx?&OpenYearDate={}&CaseNumber={}&DateType=1&SearchPeriod=8&COpenDate=null&CEndDate=null&freeText=null&Importance=null'.format(fileYear, fileNumber))
	content = stream.read()
	file = open(fileNumber + '.txt', 'w')
	file.write(str(content))
	file.close()
def referenceExists(fileNumbe):
	try:
		f = open(fileNumbe + '.txt', 'r')
		return True
	except:
		return False


def compareReferenceContentWithCurrentContent(fileNumber):
	saveToFile(fileNumber, fileYear)
	if open(fileNumber + 'ref' + '.txt', 'r').read() == open(fileNumber + '.txt', 'r').read():
		return False
	else:
		os.remove(fileNumber + 'ref' + '.txt')
		os.rename(fileNumber + '.txt', fileNumber + 'ref' + '.txt')
		return True


# Main flow
############
file = open('urls.txt', 'r').read()
files = file.split(', ')
fileNumber = files[0]
fileYear = files[1]
if checkForChange(fileNumber, fileYear) == True:
	print('change')
else:
	print('no change')
