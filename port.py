
from socket import *
import time
import pyfiglet
startTime = time.time()
num=0

banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)

if __name__ == '__main__':
   target = input('Enter the host to be scanned: ')
   t_IP = gethostbyname(target)
   print ('Starting scan on host: ', t_IP)
   
   for i in range(1, 2000):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
       num+=1
       print ('Port %d: OPEN' % (i,))
      s.close()
print('\n*****2000 ports scan successful!*****\n')
print('Time taken:', time.time() - startTime, 'ms')
print('Number of ports closed: ', 2000-num)
