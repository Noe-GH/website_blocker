# IMPORTANT. You have to edit your hosts file, adding, at the end of it, the websites you want to block.
# For example:
#27.0.0.1    www.facebook.com
#27.0.0.1    facebook.com
#27.0.0.1    www.twitter.com
#27.0.0.1    twitter.com

# Keep in mind that the host file can be modify only with admin rights.


# The file extension is .pyw and not .py so it's able to run in the background.
# Con esto, al darle doble clic al ícono el programa se ejecutará al fondo.

# To run the program automatically on Windows you have to add it to the Task Scheduler.

import time
from datetime import datetime as dt

# Write your hosts file name with it's absolute path here:
# *Usually it's in C:\\Windows\\System32\\drivers\\etc
hosts_path= ''

redirect = '27.0.0.1'

# Write here the urls of the websites you want to block:
websites = ['',]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 6) <= dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 9):
        with open(hosts_path, "r+") as file_h:
            c = file_h.read()            
            for ws in websites:
                if ws not in c:
                    file_h.write(redirect + "    " + ws + "\n")
                    
    else:
        with open(hosts_path, "r+") as file_h:
            c = file_h.readlines()
            file_h.seek(0)
            for lines in c:
                if not any(i in lines for i in websites):
                    file_h.write(lines)
            file_h.truncate()    
                                                                                       
    time.sleep(5)

