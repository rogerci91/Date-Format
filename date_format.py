import datetime

class date_format:
    '''
    To parse a given date string and return in desired format
    Parameters
    ----------
    lower: lower boundary of difference between current year and year of given date
    upperr: upper boundary of difference between current year and year of given date
    date_format: output date format, default as 'dd/mm/yyyy', possible value 'dd-mm-yyyy', 'dd/mmm/yyyy'
    ''' 
    def __init__(self, s, lower=10, upper=100, date_format='dd/mm/yyyy'):
        self.s = s
        self.lower = lower
        self.upper = upper
        self.date_format = date_format
        
    def check_validity(self, y):
        # raise error due to anomaly in year
        today = datetime.datetime.now()
        if today.year - int(y) > self.upper or today.year - int(y) < self.lower:
            raise ValueError('Please check the year')
        # if only two digits in year
        elif int(y) < 100:
            return '19' + y
        else:
            return y

    def formatting(self, d, m, y):
        if d.isdigit() and int(d) > 31:
            y, d = d, y
        if int(y) > 31:
            y = self.check_validity(y)
            months = ['jan', 'feb', 'mar', 'apr',' may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
            if d.isalpha():
                d, m = m, str(months.index(d[:3].lower()) + 1)
            if m.isalpha():
                m = str(months.index(m[:3].lower()) + 1)
            if int(m) > 12:
                d, m = m, d
        
        # add more date_format if needed
        if self.date_format == 'dd/mm/yyyy':
            return d + '/' + m + '/' + y
        if self.date_format == 'dd-mm-yyyy':
            return d + '-' + m + '-' + y
        if self.date_format == 'dd/mmm/yyyy':
            return d + '/' + months[m-1] + '/' + y

    def date_parse(self):
        s = self.s
        if s.isdigit():
            if len(s) == 6:
                d, m, y = s[:2], s[2:4], s[4:]
            elif len(s) == 8:
                if int(s[:4]) > 1913:
                    y, m, d = s[:4], s[4:6], s[6:]
                else:
                    d, m, y = s[:2], s[2:4], s[4:]
            else:
                raise ValueError('Incorrect date')
            return self.formatting(d, m, y)   

        for c in ['/', '-', '.']:
            if c in s:
                d, m, y = map(str.strip, s.split(c))
                return self.formatting(d, m, y)
        raise ValueError('Incorrect date')





