import webbrowser
import time

url1 = 'IP HERE'	# Printer 1
url2 = '#'  		# Printer 2
url3 = '#'  		# Printer 3
url4 = '#' 		# Printer 4
url5 = '#' 		# Printer 5
url6 = '#'  		# Printer 6
url7 = '#' 		# Printer 7
url8 = '#' 		# Printer 8

chrome_path: str = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

webbrowser.get(chrome_path).open_new_tab(url1)
time.sleep(2)
webbrowser.get(chrome_path).open_new_tab(url2)
time.sleep(2)
webbrowser.get(chrome_path).open_new_tab(url3)
time.sleep(2)
webbrowser.get(chrome_path).open_new_tab(url4)
time.sleep(2)
webbrowser.get(chrome_path).open_new_tab(url5)
time.sleep(2)
webbrowser.get(chrome_path).open_new_tab(url6)
time.sleep(2)
webbrowser.get(chrome_path).open_new_tab(url7)
time.sleep(2)
webbrowser.get(chrome_path).open_new_tab(url8)
time.sleep(2)