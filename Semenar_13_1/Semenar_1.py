def get_number(msg: str) -> int | float:
    while True:
        num = input(msg)
        try:
            return int(num)
        except ValueError as e:
            try:
                return float(num)
            except ValueError as e:
                print("Не верный ввод. Повторите")


print(get_number('Введите целое или вещественное число: '))
