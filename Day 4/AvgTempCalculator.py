def calculate_average_temperature(temperatures):
    total = sum(temperatures)
    count = len(temperatures)
    average = total / count
    return average

# Example usage
daily_temperatures = [22, 24, 19, 23, 25, 18, 21]
average_temp = calculate_average_temperature(daily_temperatures)
print(f"The average temperature is: {average_temp:.2f} degrees")
