def check_password(password):
    errors = []
    has_upper = False
    has_lower = False
    has_digit = False
    has_space = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch == " ":
            has_space = True

    if len(password) < 8:
        errors.append("ən azı 8 simvol olmalıdır")
    if not has_upper:
        errors.append("ən azı 1 böyük hərf olmalıdır")
    if not has_lower:
        errors.append("ən azı 1 kiçik hərf olmalıdır")
    if not has_digit:
        errors.append("ən azı 1 rəqəm olmalıdır")
    if has_space:
        errors.append("boşluq olmamalıdır")
    return errors


accepted = False
for attempt in range(3):
    password = input("Şifrə daxil edin: ")
    errors = check_password(password)
    if not errors:
        print("Şifrə qəbul olundu")
        accepted = True
        break
    print("Pozulan qaydalar:")
    for error in errors:
        print("-", error)

if not accepted:
    print("Cəhdlər bitdi")
