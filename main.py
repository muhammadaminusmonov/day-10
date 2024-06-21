# def format_name(name):
#     return name.title()
#
#
# formated_string = format_name("Muhammadamin ibn Xasan")
# print(formated_string)


# def leap_year(years):
#     """returns boolean of if the year is leap year"""
#     return years % 4 == 0
#
#
# def days_in_month(years, months):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if months == 2 and leap_year(years):
#         return month_days[months - 1] + 1
#     return month_days[months - 1]
#
#
# year = int(input("Enter the year "))
# month = int(input("Enter the month: "))
# result = days_in_month(year, month)
