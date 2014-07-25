#!/usr/bin/python
#captcha solver online by sayf_piratos
#this script uses pytesser OCR engine
#to recognise pictures and turn them 
#into  strings 
#MIT license
#######################################
import requests, base64, Image, pytesser, imgHTMLParser
from BeautifulSoup import BeautifulSoup


URL = raw_input("[+] enter the link of the captcha  : ")
#collecting coockies
choice="no"
while ( choice=="no"):
	print "[+] enter captcha details otherwise enter 'no' "
	COOCKIES_NAME = raw_input("[+] enter coockies name : ")
	if COOCKIES_NAME=="no":
		break
	COOCKIES = raw_input("[+] enter your coockies : ")
	cookies[COOCKIES_NAME] = COOCKIES
noise = raw_input("[?] is there any black noise to clean in the captcha ? (yes/no) : ")
s=requests.session() # starting a session to make use of coockies
req=requests.get(URL,cookies=cookies)
# need to add some code to detect img in html page 
# parser class is already coded in the file img_parser.html
img_data = base64.b64decode(img_coded)
f = open("img","w+")
f.write(img_data)
f.close()
image = Image.open("img")
image1 = image.convert("RGBA")
pixdata = image1.load()

#if noise then trying to clean it out
if noise=="yes":
	for y in xrange(image1.size[1]):
		for x in xrange(image1.size[0]):
			if pixdata[x, y] == (0, 0, 0, 255):
				pixdata[x, y] = (255, 255, 255, 255)
image1.save("result.gif","gif")
image_final = Image.open("result.gif")

captcha = pytesser.image_to_string(image_final).strip()
print "[*] captcha found is "+captcha

data = {
		"cametu":captcha
	}
#getting the cookies
result = requests.post(URL, data=data, cookies=cookies)
print result.text
res = open("results.html","w+")
res.write(result.text)
res.close()
print "[*] end with no errors"
