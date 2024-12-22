class Car:
    def __init__(self, model: str, vin:int, numbers:str):
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers
        self.model = model

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber(reason='type')
        elif vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber(reason='len')
        else:
            return True
    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers(reason='type')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers(reason='len')
        else:
            return True
class  IncorrectVinNumber(Exception):
    def __init__(self, reason):
        if reason == 'type':
            self.message = 'Некорректный тип vin номер'
        elif reason == 'len':
            self.message = 'Неверный диапазон для vin номера'

class IncorrectCarNumbers(Exception):
    def __init__(self, reason):
        if reason == 'type':
            self.message = 'Некорректный тип данных для номеров'
        elif reason == 'len':
            self.message = 'Неверная длина номера'

if __name__ == '__main__':
    cars_table = [('Model1', 1000000, 'f123dj'),
            ('Model2', 300, 'т001тр'),
            ('Model3', 2020202, 'нет номера')
    ]
    cars_list = []
    for row in cars_table:
        try:
            cars_list.append(Car(*row))
        except IncorrectVinNumber as exc:
            print(exc.message)
        except IncorrectCarNumbers as exc:
            print(exc.message)
        else:
            print(f'{cars_list[len(cars_list) - 1].model} успешно создан')