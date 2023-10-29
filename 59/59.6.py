class Month:
    def __init__(self, month_num):
        if 1 <= month_num <= 12:
            self.month_num = month_num
        else:
            raise ValueError("Номер месяца должен быть от 1 до 12")

    def get_month_num(self):
        return self.month_num

    def get_month_name(self):
        months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
        return months[self.month_num - 1]

    def get_last_day_month(self):
        if self.month_num in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        elif self.month_num in {4, 6, 9, 11}:
            return 30
        else:
            return 29 if self.is_leap_year() else 28

    def get_first_day_month(self):
        days_in_month = {1: 31, 2: self.get_last_day_month(), 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        day_week = 0
        for month in range(1, self.month_num):
            day_week = (day_week + days_in_month[month]) % 7
        return day_week
