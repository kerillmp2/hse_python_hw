from random import randrange

class TimeUtils():
    
    month_to_days = {
        "JANUARY": 31,
        "FEBRUARY": 28,
        "MARCH": 31,
        "APRIL": 30,
        "MAY": 31,
        "JUNE": 30,
        "JULY": 31,
        "AUGUST": 31,
        "SEPTEMBER": 30,
        "OCTOBER": 31,
        "NOVEMBER": 30,
        "DECEMBER": 31
    }
    
    
    @staticmethod
    def is_leap_year(year):
        assert year >= 0, "Year can't be negative! {} provided".format(year)
        return ((year % 400 == 0) or (year % 100 != 0 and year % 4 == 0))
    
    
    @staticmethod
    def days_in_month(year, month):
        month_upper = month.upper()
        if month_upper == "FEBRUARY" and TimeUtils.is_leap_year(year):
            return 29
        if month_upper in TimeUtils.month_to_days:
            return TimeUtils.month_to_days[month_upper]
        raise ValueError("No such month as " + month)  
        
    
    @staticmethod
    def get_holidays():
        # Будем считать, что в каждом месяце случайное кол-во выходных (от 7 до 10)
        return randrange(7, 11)
        
    
    @staticmethod
    def get_working_days(year, month):
        return TimeUtils.days_in_month(year, month) - TimeUtils.get_holidays()
