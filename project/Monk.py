import re
import datetime 
import calendar 

class Monk:
    
    @staticmethod
    def convert_h_to_s(h):
        if h is None:
            return -43320
        data = re.split(r':', h)
        return int(data[0])*3600 + int(data[1])*60 + int(data[2])


    @staticmethod
    def convert_s_to_h(s):
        h = str(int(s/3600))
        s %= 3600
        if int(h) < 0:
            return None
        if int(h) < 10:
            h = ('0' + h)
        m = str(int(s/60))
        if int(m) < 10:
            m = ('0' + m)
        s %= 60
        if s > 10:
            s = str(s)
        else:
            s = ('0%i' % s)
        return h+':'+m+':'+s


    @staticmethod
    def get_day_from_date(date):
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        return calendar.day_name[date.weekday()] 


