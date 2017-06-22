import re

nlog = '192.168.1.12 - - [23/Jun/2015:11:10:57 +0000] "GET /entry/how-create-configure-free-ssl-certificate-using-django-and-pythonanywhere HTTP/1.1" 302 5 "http://www.reddit.com/r/Python/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.18 Safari/537.36" "192.168.1.12"'

plog = '10.50.11.98 - - ads.ent.sessionm.com [21/Jan/2016:15:03:58 +0000] POST /v1/apps/test/session.json?z=1453388638 HTTP/1.1 "404" 162 "-" "Ruby" "unix:/tmp/thin.core.0.sock, unix:/tmp/thin.core.1.sock" "0.000, 0.000" "-" "-" "-"'

#r = re.search(r'(\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}) - - \[(.*)\] (\w{3,6}.* \w{0,4}/\d\.\d) \"(\d+)\" (\d+) \"-\" "(\S+)" ["](.*)["] ["](\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3})', plog)
r = re.search(r'(\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3})', plog)
r1 = re.search(r'\[(.*)\]', plog)
r2 = re.search(r'(\w{3,6}.* \w{0,4}/\d\.\d)', plog)
http_x_real_ip = r.groups()[0]
http_x_date = r1.groups()[0]
http_x_action = r2.groups()[0]
print(http_x_real_ip)
print(http_x_date)
print(http_x_action)
