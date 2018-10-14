import time
import datetime

birthdate = datetime.datetime(1970, 1, 1)
elapsed = datetime.datetime.now() - bithdate

print (elapsed.total_seconds())
print(birthdate + datetime.timedelta(days=20000))

while True:
    time.sleep(1)
    print "time now:", datetime.datetime.now()
    print "date today", datetime.date.today()
    print "time now (iso)", datetime.datetime.now().isoformat()
    print "running", time.time()  # seconds since 1970,1,1,00:00

print "finished"
