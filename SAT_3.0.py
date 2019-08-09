import requests
import os
from bs4 import BeautifulSoup


def getinfo_in_India(url,state,year,islm):

    temp = open("buffer.txt","a")

    if(islm==0):
        file_name = ("SATP_info_"+state+"_"+year+".txt")
    elif(islm==1):
        file_name = ("SATP_info_"+"islamic_conflicts_"+state+"_"+year+".txt")
        
    satp = open(file_name,"a")
    
    data = requests.get(url,'htmlparser').text
    soup=BeautifulSoup(data,'html5lib')
    tds = soup.find_all('td')

    for td in tds:
        temp.write(td.text)
    
    temp.close()
    temp = open("buffer.txt","r")
    flag=0

    for lines in temp:
        lines = lines.strip()

        if(lines==""):
            continue
    
        if lines.startswith(month):
            satp.write("\n\n"+lines+"\n")
        
        if lines=="Read more...":
            flag=1
            continue
        if lines=="Read less...":
            flag=0
            continue
        if flag==1:
            satp.write(lines)
          
    temp.close()
    os.remove('buffer.txt')
    satp.close()


def getinfo_out_India(url,counrty,year):

    file_name = ("SATP_info_"+counrty+"_"+year+".txt")

    satp = open(file_name,"a")

    data = requests.get(url,'htmlparser').text
    soup=BeautifulSoup(data,'html5lib')
    tds = soup.find_all('td')

    for td in tds:
        temp.write(td.text)
    
    temp.close()
    temp = open("buffer.txt","r")
    flag=0

    for lines in temp:
        lines = lines.strip()

        if(lines==""):
            continue
    
        if lines.startswith(month):
            satp.write("\n\n"+lines+"\n")
        
        if lines=="Read more...":
            flag=1
            continue
        if lines=="Read less...":
            flag=0
            continue
        if flag==1:
            satp.write(lines)
          
    temp.close()
    os.remove('buffer.txt')
    satp.close()
    
    

islm=0

northeast_states = {'assam','manipur','meghalaya',
                    'mizoram','nagaland','tripura'}

north_states = {'jammukashmir','punjab'}

other_states = {'andhrapradesh','bihar','chattisgarh',
                'goa','gujrat','haryana','jharkhand',
                'karnataka','kerela','madhyapradesh',
                'maharashtra','odisha','rajasthan',
                'tamilnadu','telangana','uttarpradesh',
                'uttarakhand','westbengal'}

islamic_states = {'andamanandnicoberislands','andhrapradesh','bihar',
                  'chandigarhut','dadraandnagarhavelli','damananddiu',
                  'delhi','goa','gujrat','haryana','jharkhand',
                'karnataka','kerela','himachalpradesh','lakshadweep',
                  'madhyapradesh','maharashtra','odisha','pondicherry',
                  'rajasthan','sikkim','tamilnadu','telangana',
                  'uttarpradesh','uttarakhand','westbengal'}

neighbouring_countries = {'southasia','afghanistan','bangladesh',
                          'bhutan','maldives','nepal','pakistan',
                          'srilanka'}

months={'Jan','Feb','Mar','Apr',
        'May','Jun','Jul','Aug',
        'Sep','Oct','Nov','Dec'}

urls = {"https://www.satp.org/terrorist-activity/india-",
        "https://www.satp.org/terrorist-activity/india-insurgencynortheast-",
        "https://www.satp.org/terrorist-activity/india-maoistinsurgency-",
        "https://www.satp.org/terrorist-activity/india-islamistotherconflicts-",
        "https://www.satp.org/terrorist-activity/southasia"}

year = input("Year: ")

for state in northeast_states:
    for month in months:
        url = ("https://www.satp.org/terrorist-activity/india-insurgencynortheast-"+state+"-"+month+"-"+year)
        getinfo_in_India(url,state,year,islm)

for state in north_states:
    for month in months:
        url = ("https://www.satp.org/terrorist-activity/india-"+state+"-"+month+"-"+year)
        getinfo_in_India(url,state,year,islm)

for state in other_states:
    for month in months:
        url = ("https://www.satp.org/terrorist-activity/india-maoistinsurgency-"+state+"-"+month+"-"+year)
        getinfo_in_India(url,state,year,islm)

islm=1
for state in islamic_states:
    for month in months:
        url = ("https://www.satp.org/terrorist-activity/india-islamistotherconflicts-"+state+"-"+month+"-"+year)
        getinfo_in_India(url,state,year,islm)
        
for countries in neighbouring_countries:
    for month in months:
        url = ("https://www.satp.org/terrorist-activity/"+countries+"-"+month+"-"+year)
        getinfo_out_India(url,country,year)



       



