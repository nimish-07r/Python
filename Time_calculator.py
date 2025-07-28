def add_time(start, duration, start_day = None):
    time, meridiem = start.split()

    hours, minutes = map(int, time.split(':'))

    dur_hour, dur_min = map(int, duration.split(':'))
    
    if meridiem == 'AM' and hours == 12:
        hours = 0
    elif meridiem == 'PM' and hours < 12:
        hours += 12
    
    total_minutes = minutes + dur_min
    final_minutes = total_minutes % 60
    extra_hour = total_minutes // 60

    total_hour = hours + dur_hour + extra_hour
    days_later = total_hour // 24
    final_hour_24 = total_hour % 24

    meridiem = 'PM' if final_hour_24 >= 12 else 'AM'

    final_hour = final_hour_24 % 12
    if final_hour == 0:
        final_hour = 12
    
    new_time = f"{final_hour}:{final_minutes:02d} {meridiem}"

    if start_day:
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day_index = (days.index(start_day.lower()) + days_later) % 7
        new_time += f', {days[day_index].capitalize()}'
    
    if days_later == 1:
        new_time += ' (next day)'
    elif days_later > 1:
        new_time += f' ({days_later} days later)'

    return new_time

print(add_time('6:30 PM', '205:12'))
print(add_time('11:43 PM', '24:20'))
print(add_time('10:10 PM', '3:30'))
print(add_time('11:43 AM', '00:20'))
print(add_time('11:30 AM', '2:32'))
print(add_time('3:00 PM', '3:10', 'Tuesday'))