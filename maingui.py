import sys
import PySimpleGUI as sg
import urllib.request as url
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('c:\python\Agmon\webdriver\chromedriver.exe', options=options)
driver.get('https://eytangut.github.io/lawyers_application_pay_confirmation_website/')
yesno = driver.find_element(by=By.CLASS_NAME, value='yellow')
print(yesno.text)
if yesno.text == 'yes':
	sys.exit()
layout = [[sg.Text("את/ה נמצא/ת בתיק מספר  ", key='-label-')], [sg.Text('טוען...', key='-ulabel-')], [sg.Button("פתח")], [sg.Button("הבא")], [sg.Button("הקודם")]]

# Create the window
window = sg.Window("", layout, finalize=True)

# Create an event loop
import webbrowser
fileurl = open('urls.txt', 'r')
file = fileurl.read()
file_lst = file.split('\n')
file_lst_split = []
# url formation = https://supreme.court.gov.il/Pages/SearchJudgments.aspx?&OpenYearDate=YEAR&CaseNumber=NUM&DateType
# =1&SearchPeriod=8&COpenDate=null&CEndDate=null&freeText=null&Importance=null
index = 0
for i in file_lst:
	num, year = i.split(', ')
	file_lst_split.append([num, year])
    # End program if user closes window or
    # presses the OK button
while True:
	try:
		var = "את/ה נמצא/ת בתיק " + str(file_lst_split[index][0]) + '/'+ str(file_lst_split[index][1])+'.'
		window['-label-'].update(" את/ה נמצא/ת בתיק {}/{}. ".format(str(file_lst_split[index][0]), str(file_lst_split[index][1])))
	except:
		index = 0
	num1, year1 = file_lst_split[index]
	stream = url.urlopen('https://supreme.court.gov.il/Pages/SearchJudgments.aspx?&OpenYearDate={}&CaseNumber={}&DateType=1&SearchPeriod=8&COpenDate=null&CEndDate=null&freeText=null&Importance=null'.format(year1, num1))
	content = stream.read()
	print(content)
	f = open('content{}.txt'.format(num1) ,'w')
	f.write(content)
	f.close()
	filehtml = open('content{}.txt'.format(num1), 'r')
	print(filehtml)
	print(filehtml.read())
	if not(str(filehtml.read()) == str(content)):
		f = open("{}.txt".format(num1), "w")
		f.write(str(content))
		f.close()
		window['-ulabel-'].update("יש עדכון בתיק הנוכחי!")
	if filehtml.read() == content:
		window['-ulabel-'].update("אין עדכון בתיק הנוכחי")
	event, values = window.read()
	if event == sg.WIN_CLOSED:
		break
	if event == 'פתח':
		webbrowser.open('https://supreme.court.gov.il/Pages/SearchJudgments.aspx?&OpenYearDate={}&CaseNumber={}&DateType=1&SearchPeriod=8&COpenDate=null&CEndDate=null&freeText=null&Importance=null'.format(year1, num1))
	elif event == 'הבא':
		index = index.__add__(1)
	elif event == 'הקודם':
		index = index.__add__(-1)



window.close()