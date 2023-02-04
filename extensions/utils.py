from . import jalali


def jalali_converter(date):
    jmonths = [
        'فروردین',
        'اردیبهشت',
        'خرداد',
        'تیر',
        'مرداد',
        'شهریور',
        'مهر',
        'آبان',
        'آذر',
        'دی',
        'بهمن',
        'اسفند',
    ]
    date_to_str = f'{date.year},{date.month},{date.day}'
    date_in_tuple = jalali.Gregorian(date_to_str).persian_tuple()
    date_to_list = list(date_in_tuple)
    for index, month in enumerate(jmonths):
        if date_to_list[1] == index + 1:
            date_to_list[1] = month
            break

    output = f'{date_to_list[2]} {date_to_list[1]} , {date_to_list[0]}'
    return output
