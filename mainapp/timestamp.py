import time
ts = time.time()
print(ts)
1355563265.81
import datetime
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print(st)