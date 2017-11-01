from bs4 import BeautifulSoup
import urllib.request
import threading
import time


def instancea(i,multiplicador):
    print('llamando al hilo'+str(i+1))
    my_list=llamada_request(i,multiplicador)
    for dato in my_list:
        print (dato)
        print ('*******************************************************************************')
#last = (len(my_list) - 1)
#print(my_list[-1])
    print ('done !!')
    return 
	
	
	
def llamada_request(i,multiplicador):
    my_list = list()
    iterador2=1
    try: 
        while ( (i*multiplicador) + iterador2<=multiplicador*  (i+1)   ):
            
            print('paso--->'+str(iterador2))
            url= 'http://offenders.sst.org.nz/offender/page/'+str(iterador2 * (multiplicador * (i+1) )   )+'/?orderby=post_title&order=ASC'
            req2 = urllib.request.Request(url)
            response2 = urllib.request.urlopen(req2)
            the_page2 = response2.read()
            iterador2=1+iterador2
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




hiloystich = list()

todo = list()
multiplicador=1


for i in range(2):
    t = threading.Thread(target=instancea, args=(i,multiplicador))
    hiloystich.append(t)
    t.start()
	
for i in range(2):
    t.join()	

time.sleep(2)
print('acabaron')	



