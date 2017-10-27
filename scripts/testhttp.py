import urllib.request

req = urllib.request.Request(('http://offenders.sst.org.nz/offender/?orderby=post_title&order=ASC'))
response = urllib.request.urlopen(req)
the_page = response.read()

encoding = response.headers.get_content_charset('utf-8')
decoded_html = the_page.decode(encoding)

file = open('testfile.html','w') 
 
file.write(decoded_html) 

 
file.close() 


print ('done !!')
