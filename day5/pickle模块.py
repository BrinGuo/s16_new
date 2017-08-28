

import pickle
account = {"id":234223455,
           "name":"BrinGuo",
           "credit":100000,
           "balance":80000,

           }
f = open("account.db","w")
f.write(str(account))
f.close()


f = open("account.db","r")
ac = f.read()

f.close()