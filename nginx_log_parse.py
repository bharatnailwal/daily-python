import re
from collections import Counter
import csv
filename="nginx-logs.txt"
newfile="nginx-latest.csv"
logreg="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
#apiname="/downloads/product_\d{1}"
with open(filename) as f:
   log = f.read()
   iplist = re.findall(logreg,log)
   with open(newfile,"w") as f:
       lognew = csv.writer(f)
       lognew.writerow(["IPAddress","Count"])
       for k,v in Counter(iplist).items():
           lognew.writerow([k,v])

    #print(Counter(iplist))
    ## As its in dict format, print it like this below
    #for k,v in Counter(iplist).items():
        #print("IPADDRESS " + k + "\t Count", v)


# with open(filename) as f:
#     log = f.read()
#     iplist = re.findall(logreg,log)
#     apilist=re.findall(apiname,log)
#     for i,j in Counter(apilist).items():
#             print(i,j)
