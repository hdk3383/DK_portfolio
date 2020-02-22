
import datetime, time

class Unixtime:
    def getTodayUnixtime(self):
        int_type = int(datetime.datetime.today().timestamp())
        str_type = str(int_type)
        return str_type
    def get180beforeUnixtime(self):
        int_type = int((datetime.datetime.today() - datetime.timedelta(days=180)).timestamp())
        str_type = str(int_type)
        return str_type
unixtime = Unixtime()