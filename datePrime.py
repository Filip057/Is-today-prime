from datetime import datetime


class Message:

    def __init__(self):
        self.year = int(datetime.now().strftime('%Y'))
        self.month = int(datetime.now().strftime('%m'))
        self.day = int(datetime.now().strftime('%d'))
        self.d_m = str(self.day) + str(self.month)
        self.d_m_y = str(self.day) + str(self.month) + str(self.year)

    def is_prime(self, num):
        if num == 1:
            return 'is not'

        check = [n for n in range(2, int(int(num) / 2) + 1) if int(num) % n == 0]
        if len(check) == 0:
            return 'is'
        else:
            return 'is not'




'''
day
month
year
day+m
d+m+y
m+d+y

num is/isnt a prime number. 

'''

