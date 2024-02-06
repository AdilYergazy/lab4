from datetime import date, timedelta
from time import strptime
from datetime import datetime
dt = date.today() + timedelta(5)
# 1
print('5 days after today is', dt)
# 2
dt = date.today() - timedelta(1)
print('yesterday:', dt)
dt = date.today()
print('today', dt)
dt = date.today() + timedelta(1)
print('tomorrow:', dt)
# 3
ms = str(datetime.now().strftime('%d.%m.%Y %H:%M:%S,%f'))
print(ms)
# 4
print((datetime.now() - datetime(1997, 2, 10)).total_seconds())
