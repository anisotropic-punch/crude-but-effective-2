
# coding: utf-8

# In[2]:


import requests
import html2text
from bs4 import BeautifulSoup
page = requests.get('https://flightaware.com/live/findflight?origin=KORD&destination=KDCA')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
import re
findtag=soup.find_all("script", text=re.compile("flightDepartureTime"))
    #print(findtag)
#current = 1





print (findtag[2])

print("_AAAAAAA_____________________")
print("______________________")

findtime=findtag[2]
print(findtime)
print("________________repritn as text")

print(findtime.get_text)
findtimetext=findtime.get_text
print("_____________type")
print(type(findtimetext))
findtimestr=str(findtimetext)
print(type(findtimestr))


print (findtimestr.find("flightDepartureTime"))

starts = [match.start() for match in re.finditer(re.escape("flightDepartureTime"), findtimestr)]
print(starts)
print(type(starts))



print(starts[1])
print(len(starts))

count=0
timelist = []
print (type(timelist))
while True:
  spottime=starts[count]
  print(type(spottime))
  print(spottime)
  locn=spottime
  print (findtimestr[locn+22:locn+27])
  timelist.append(findtimestr[locn+22:locn+27])
  count +=1
  if count>30:
      break


print (type(timelist))
print(timelist)



count=0
flightlist = []
print (type(flightlist))
while True:
  spottime=starts[count]
  #print(type(spottime))
  #print(spottime)
  locn=spottime
  print (findtimestr[locn+150:locn+150+7])
  flightlist.append(findtimestr[locn+150:locn+150+7])
  count +=1
  if count>30:
      break


print (type(flightlist))
print(flightlist)

import numpy

print ("improt pandas")
import pandas as pd
print("ok panda")

flightnumtime = pd.DataFrame({
  "flightnum":flightlist,
  "time": timelist
  })
print(flightnumtime)



#for p in findtag:
   #print(p)
print("______________________")
print("______________________")

for r in findtag:
  nextsib=r.nextSibling
  print(nextsib)
    
print ("xxxxxxx")
#findtable=soup.find_all("script", type="text/javascript")
#for p in findtable:
     #print(p.prettify())
print("xxxxxx")
print("xxxxxx")
     
#findTOD=soup.find_all("div")
#print(findTOD)
#for p in findTOD:
        #print(p.prettify())
#TimeOfDeparture = findtable.find(title='\"').get_text
#print(TimeOfDeparture)
#print (findtable.prettify())
#for tag in soup.find_all(True):
# print(tag.name)
#hreffind=soup.find_all(href=re.compile(""))
#print(hreffind)
afindall=soup.find_all("a")
#print(afindall)


sourceFile = open('PYTHON PRETTIFY.odt', 'w')
import time
#time.sleep(60)

print(soup.prettify , file = sourceFile)
#print(soup.prettify())

#<div id="Col2-3-QuoteModule-Proxy"><div class="" data-test="quote-mdl"><section id="rec-by-symbol" class="My(25px) smartphone_Px(20px)"><p class="Fz(m) Lh(1) Fw(b) Mt(0) Mb(15px)"><span>People Also Watch</span></p><table class="Pos(r) Ta(end) Tbl(f) Va(m) W(100%) P(0) M(0) Bdcl(c) table-bordered Lh(1.2) table-resizable"><thead><tr class="Fz(xs) C($c-fuji-grey-j) Bxz(bb) Bdc($c-fuji-grey-c)"><th class="Pb(7px) Fw(n) Ta(start) W(60px)"><span>Symbol</span></th><th class="Pb(7px) Fw(n) "><span>Last Price</span></th><th class="Pb(7px) Fw(n) "><span>Change</span></th><th class="Pb(7px) Fw(n) "><span>% Change</span></th></tr></thead><tbody><tr class="Va(t) Bdc($c-fuji-grey-c) TapHc(h) Fw(500) Bgc($extraLightBlue):h H(44px) BdT" data-action="open-dialog"><td class="Ta(start) Fz(14px) Py(6px)"><a class="Fw(b) Ell D(b)" href="/quote/MXIM?p=MXIM" title="MXIM">MXIM</a><p class="Fz(xs) Pt(2px) M(0) C($c-fuji-grey-j) Pos(a) Fw(400)! Ell Maw(220px)">Maxim Integrated Products, Inc.</p></td><td class="Fz(14px) Py(6px)"><span class="Trsdu(0.3s) ">59.99</span></td><td class="Fz(14px) Py(6px)"><span class="Trsdu(0.3s)  C($dataRed)">-0.16</span></td><td class="Fz(14px) Py(6px)"><span class="Trsdu(0.3s)  C($dataRed)">-0.27%</span></td></tr><tr class="Va(t) Bdc($c-fuji-grey-c) TapHc(h) Fw(500) Bgc($extraLightBlue):h H(44px) BdT" data-action="open-dialog"><td class="Ta(start) Fz(14px) Py(6px)"><a class="Fw(b) Ell D(b)" href="/quote/XLNX?p=XLNX" title="XLNX">XLNX</a><p class="Fz(xs) Pt(2px) M(0) C($c-fuji-grey-j) Pos(a) Fw(400)! Ell Maw(220px)">Xilinx, Inc.</p></td><td class="Fz(14px) Py(6px)"><span class="Trsdu(0.3s) ">71.02</span></td><td class="Fz(14px) Py(6px)"><span class="Trsdu(0.3s)  C($dataGreen)">+0.41</span></td><td class="Fz(14px) Py(6px)"><span class="Trsdu(0.3s)  C($dataGreen)">+0.58%</span></td></tr><tr class="Va(t) Bdc($c-fuji-grey-c) TapHc(h) Fw(500) Bgc($extraLightBlue):h H(44px) BdT" data-action="open-dialog"><td class="Ta(start) Fz(14px) Py(6px)"><a class="Fw(b) Ell D(b)" href="/quote/LLTC?p=LLTC" title="LLTC">LLTC</a><p class="Fz(xs) Pt(2px) M(0) C($c-fuji-grey-j) Pos(a) Fw(400)! Ell Maw(220px)">LLTC</p></td><td class="Fz(14px) Py(6px)"><span class="Trsdu(0.3s) ">0.00</span></td><td class="Fz(14px) Py(6px)"><span class="Trsdu(0.3s) ">0.00</span></td><td class="Fz(14px) Py(6px)"><span class="Trsdu(0.3s) ">0.00%</span></td></tr><tr class="Va(t) Bdc($c-fuji-grey-c) TapHc(h) Fw(500) Bgc($extraLightBlue):h H(44px) BdT" data-action="open-dialog"><td class="Ta(start) Fz(14px) Py(6px)"><a class="Fw(b) Ell D(b)" href="/quote/TXN?p=TXN" title="TXN">TXN</a><p class="Fz(xs) Pt(2px) M(0) C($c-fuji-grey-j) Pos(a) Fw(400)! Ell Maw(220px)">Texas Instruments Incorporated</p></td><td class="Fz(14px) Py(6px)"><span class="Trsdu(0.3s) ">109.64</span></td><td class="Fz(14px) Py(6px)"><span class="Trsdu(0.3s)  C($dataGreen)">+0.24</span></td><td class="Fz(14px) Py(6px)"><span class="Trsdu(0.3s)  C($dataGreen)">+0.22%</span></td></tr><tr class="Va(t) Bdc($c-fuji-grey-c) TapHc(h) Fw(500) Bgc($extraLightBlue):h H(44px) BdY" data-action="open-dialog"><td class="Ta(start) Fz(14px) Py(6px)"><a class="Fw(b) Ell D(b)" href="/quote/NSM?p=NSM" title="NSM">NSM</a><p class="Fz(xs) Pt(2px) M(0) C($c-fuji-grey-j) Pos(a) Fw(400)! Ell Maw(220px)">Nationstar Mortgage Holdings In</p></td><td class="Fz(14px) Py(6px)"><span class="Trsdu(0.3s) ">18.26</span></td><td class="Fz(14px) Py(6px)"><span class="Trsdu(0.3s)  C($dataRed)">-0.31</span></td><td class="Fz(14px) Py(6px)"><span class="Trsdu(0.3s)  C($dataRed)">-1.67%</span></td></tr></tbody></table></section></div></div>
#




tagsStartWithHref=soup.find(re.compile('href'))
print (tagsStartWithHref.prettify())
RecBySymbol = soup.find('a', href="/live/$")

print(RecBySymbol)
print(RecBySymbol.prettify())


forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())

print (forecast_items[1].prettify())
print (forecast_items[2].prettify())
print (forecast_items[3].prettify())

