from datetime import datetime

print('{}-{}-{}'.format(datetime.today().year, datetime.today().month, datetime.today().day))
print(str(datetime.now())[:10])
print(str(datetime.now()))
print(str(datetime.today())[:10])
print(str(datetime.today()))
d = datetime.today()
print(d.isoformat())

'''
from datetime import datetime
datetime.today()            # 현재 날짜 가져오기
datetime.today().year       # 현재 연도 가져오기
datetime.today().month      # 현재 월 가져오기
datetime.today().day        # 현재 일 가져오기
datetime.today().hour       # 현재 시간 가져오기
'''