import requests
from bs4 import BeautifulSoup

pnr=input('Enter PNR number: ')#4589632578
url='https://www.makemytrip.com/railways/pnrsearch/?pnr='+'pnr'

src=requests.get(url)
soup=BeautifulSoup(src.content,'html.parser')

result=soup.find("p", attrs={"class":"font16 lightGreyText appendBottom30"})
#result=soup.find("data-cy"="pnrFlushedTxt")

result_final=result.string

print(result_final)

#result_final.strip()
#print(result_final)
