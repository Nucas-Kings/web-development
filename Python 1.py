# 3.1 Calculate the number of seconds in an hour
seconds_per_minute = 60
minutes_per_hour = 60
seconds_per_hour = seconds_per_minute * minutes_per_hour
print("Seconds in an hour:", seconds_per_hour)

# 3.2 Assign the result to a variable called seconds_per_hour
# (Already done above)

# 3.3 Calculate the number of seconds in a day using seconds_per_hour
hours_per_day = 24
seconds_per_day = seconds_per_hour * hours_per_day
print("Seconds in a day:", seconds_per_day)

# 3.4 Save the result in a variable called seconds_per_day
# (Already done above)

# 3.5 Divide seconds_per_day by seconds_per_hour using floating-point division
floating_point_division = seconds_per_day / seconds_per_hour
print("Floating-point division (seconds_per_day / seconds_per_hour):", floating_point_division)

# 3.6 Divide seconds_per_day by seconds_per_hour using integer division
integer_division = seconds_per_day // seconds_per_hour
print("Integer division (seconds_per_day // seconds_per_hour):", integer_division)
