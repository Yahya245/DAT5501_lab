def generate_calendar(days_in_month, first_day_of_month):
    calendar = "S  M  T  W  T  F  S\n"

    # Create spacing before first day
    day = 1
    week = ["   "] * (first_day_of_month - 1)

    while day <= days_in_month:
        week.append(f"{day:2d} ")
        if len(week) == 7:
            calendar += "".join(week).rstrip() + "\n"
            week = []
        day += 1

    if week:
        calendar += "".join(week).rstrip()

    return calendar


def main():
    print('How many days are in this month?')
    days_in_month = int(input())

    print('What day of the week did this month start on?')
    print('Enter 1 Sunday, 2 Monday, 3 Tuesday, 4 Wednesday, 5 Thursday, 6 Friday, 7 Saturday')
    first_day_of_month = int(input())

    print(generate_calendar(days_in_month, first_day_of_month))


if __name__ == "__main__":
    main()


    