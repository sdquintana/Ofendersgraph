from bs4 import BeautifulSoup
import urllib.request
import threading
	
	
	
def llamada_request(iterador):
    my_list = list()
    try: 
        while (iterador<=1):
            
            print('paso--->'+str(iterador))
            url= 'http://offenders.sst.org.nz/offender/page/'+str(iterador)+'/?orderby=post_title&order=ASC'
            req2 = urllib.request.Request(url)
            response2 = urllib.request.urlopen(req2)
            the_page2 = response2.read()
            iterador=1+iterador
            encoding2 = response2.headers.get_content_charset('utf-8')
            decoded_html2 = the_page2.decode(encoding2)
            soup2 = BeautifulSoup(decoded_html2, 'html.parser')
            div_tag = soup2.find_all('div', {'class': 'post-entry-content'})
           
			
            for tag in div_tag:
                tag2 = tag
                my_list.append(tag2.get_text().splitlines()[3].strip())
    except urllib.error.URLError as e: 
        print(e.reason)
		
	
    return my_list	



iterador=1
my_list=llamada_request(iterador)
for dato in my_list:
    print (dato)
    print ('*******************************************************************************')
#last = (len(my_list) - 1)
print(my_list[-1])
print ('done !!')
