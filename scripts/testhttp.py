from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.Request('http://offenders.sst.org.nz/offender/?orderby=post_title&order=ASC')
response = urllib.request.urlopen(req)
the_page = response.read()

encoding = response.headers.get_content_charset('utf-8')
decoded_html = the_page.decode(encoding)

#file = open('C:\\python\\Scripts\\oferders\\Ofendersgraph\\scripts\\Ofender.html','w') 
#file.write(decoded_html) 
#file.close() 

my_list = list()

soup = BeautifulSoup(decoded_html, 'html.parser')
div_tag = soup.find_all('div', {'class': 'post-entry-content'})

iterador=2

try: 
    while (True):
        for tag in div_tag:
            tag2 = tag
            my_list.append(tag2.get_text().splitlines()[3].strip())
            #print ('********************************************************************************************')
            #print(tag2.get_text().splitlines()[3].strip())
        url= 'http://offenders.sst.org.nz/offender/page/'+str(iterador)+'/?orderby=post_title&order=ASC'
        req2 = urllib.request.Request(url)
        response2 = urllib.request.urlopen(req2)
        the_page2 = response2.read()
        iterador=1+iterador
        encoding2 = response2.headers.get_content_charset('utf-8')
        decoded_html2 = the_page2.decode(encoding2)
        soup2 = BeautifulSoup(decoded_html2, 'html.parser')
        div_tag = soup2.find_all('div', {'class': 'post-entry-content'})
        print(iterador)
except urllib.error.URLError as e: 
    print(e.reason)
	
	

    


	
#for dato in my_list:
#    print (dato)
#    print ('*******************************************************************************')
#last = (len(my_list) - 1)
print(my_list[-1])
print ('done !!')
