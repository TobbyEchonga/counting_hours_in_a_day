calculation_to_hours = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f'{num_of_days} days have {num_of_days * calculation_to_hours} {name_of_unit}'


user_input = input(f'Enter a value for number of days and i will convert it to {name_of_unit}\n')
user_input_number = int(user_input)
calculated_value = days_to_units(user_input_number)
print(calculated_value)


//Enter a value for number of days and i will convert it to hours
//40
//40 days have 960 hours
