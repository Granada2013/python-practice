"""
Your task in order to complete this Kata is to write a function which formats a duration,
given as a number of seconds, in a human-friendly way.
The function must accept a non-negative integer. If it is zero, it just returns "now".
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
"""
def time_converter(sec):
    if not sec:
        return 'now'
    time = [('year', 3600*24*365), ('day', 3600*24), ('hour', 3600), ('minute', 60), ('second', 1)]
    date = []
    for t, num in time:
        n = sec // num
        if n:
            if n > 1:
                t += 's'
            date.append(str(n) + ' ' + t)
        sec = sec % num
    if len(date) > 1: date.insert(-1, 'and')
    return ' '.join([i + ',' if len(i) >= 4 and i in date[:len(date)-3] else i for i in date])
print(time_converter(155))
