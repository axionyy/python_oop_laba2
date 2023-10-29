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