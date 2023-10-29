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
