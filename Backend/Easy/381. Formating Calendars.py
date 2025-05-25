import sys


def main():
    weekDay = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    days, week = input().split()

    calendar = []
    first_week = [".." for i in range(weekDay[week])]

    calendar_week = first_week
    for day in range(1, int(days)+1):
        if len(calendar_week) < 7:
            if day < 10:
                calendar_week.append("." + str(day))
            else:
                calendar_week.append(str(day))
        elif len(calendar_week) == 7:
            calendar.append(calendar_week)
            calendar_week = []
            if day < 10:
                calendar_week.append("." + str(day))
            else:
                calendar_week.append(str(day))
        else:
            calendar.append(calendar_week)

    if calendar_week not in calendar:
        calendar.append(calendar_week)

    for i in calendar:
        print(' '.join(i))


if __name__ == '__main__':
    main()
