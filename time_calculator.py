# 24-HOUR format: (AM: 0:00 - 11:59) | (PM: 12:00 - 23:59)
double_digit = lambda num: f'0{num}' if num in range(0, 10) else str(num)
to_meridiem = lambda hour: str(hour) + ' AM' if hour < 12 else str((hour - 12)) + ' PM'
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def to_24h(hour, period):
    if period == 'AM':
        return hour
    elif period == 'PM' and hour == 12:
        return 0
    else:
        return hour + 12


def add_time(start, duration, starting_day=''):
    # Initial Data
    period = start.split(' ')[1]  # AM - PM
    current_hour = to_24h(int(start.split(' ')[0].split(':')[0]), period)
    current_minute = int(start.split(' ')[0].split(':')[1])
    duration_hour = int(duration.split(':')[0])
    duration_minute = int(duration.split(':')[1])
    duration_day = 0

    # Calculations
    new_minute = current_minute + duration_minute
    new_hour = current_hour + duration_hour
    if new_minute > 59:
        new_hour += 1
        new_minute %= 60
    duration_day += int(new_hour / 24)
    new_hour %= 24

    # duration-day text formatting
    duration_day_text = ''
    if starting_day != '':
        if duration_day == 0:
            duration_day_text += f', {starting_day[0].upper()}{starting_day[1:]}'
        else:
            starting_day_index = weekdays.index(starting_day.lower())
            day = weekdays[(starting_day_index + duration_day) % 7]
            if duration_day == 1:
                duration_day_text += f', {day[0].upper()}{day[1:]} (next day)'
            else:
                duration_day_text += f', {day[0].upper()}{day[1:]} ({duration_day} days later)'
    else:
        if duration_day != 0:
            if duration_day == 1:
                duration_day_text += ' (next day)'
            else:
                duration_day_text += f' ({duration_day} days later)'

    # Preparing to return in '12h-format'
    meridiem_format = to_meridiem(new_hour).split(' ')
    new_hour = int(meridiem_format[0])
    period = meridiem_format[1]
    if new_hour == 0: new_hour += 12
    return f'{new_hour}:{double_digit(new_minute)} {period}{duration_day_text}'
