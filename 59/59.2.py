class Month:
    def __init__(self, month_num):
        if 1 <= month_num <= 12:
            self.month_num = month_num
        else:
            raise ValueError("Номер месяца должен быть от 1 до 12")

    class Month:
        def __init__(self, month_num):
            if 1 <= month_num <= 12:
                self.month_num = month_num
            else:
                raise ValueError("Номер месяца должен быть от 1 до 12")

        def get_month_num(self):
            return self.month_num
