# объявление функции
def is_password_good(password):
    flag_num = 0
    for s in password:
        if s in [chr(v) for v in range(49, 58)]:
            flag_num = 1
            break
    flag_lower = 0
    for s in password:
        if s in [chr(v) for v in range(97, 123)]:
            flag_lower = 1
            break
    flag_upper = 0
    for s in password:
        if s in [chr(v) for v in range(65, 91)]:
            flag_upper = 1
            break
    flag = False
    if len(password) >= 8 and flag_num == 1 \
            and flag_lower == 1 and flag_upper == 1:
        flag = True
    return flag

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))