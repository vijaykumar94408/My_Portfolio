# here i used custome exception
class UnitError_exception(Exception):
    pass

print(" This program is to temperature Conversion Tool")
print("Convertion between Celsius (C), Fahrenheit (F), and Kelvin (K)")

while True:
    try: #entering input from user and selecting the type of conversion to convert 
        unit_from = input("Specify the current unit (C, F, K): ").upper()
        temp = float(input("Enter the temperature value: "))
        unit_to = input("Specify the target unit (C, F, K): ").upper()
#if invalid conversion is selected showing error to user to select a valid conversion
        if unit_from not in ['C', 'F', 'K'] or unit_to not in ['C', 'F', 'K']:
            raise UnitError("Invalid unit provided. Please use C, F, or K.")
# coversion 
        if unit_from == unit_to:
            converted_temp = temp
        elif unit_from == 'C':
            if unit_to == 'F':
                converted_temp = (temp * 9/5) + 32
            elif unit_to == 'K':
                converted_temp = temp + 273.15
        elif unit_from == 'F':
            if unit_to == 'C':
                converted_temp = (temp - 32) * 5/9
            elif unit_to == 'K':
                converted_temp = (temp - 32) * 5/9 + 273.15
        elif unit_from == 'K':
            if unit_to == 'C':
                converted_temp = temp - 273.15
            elif unit_to == 'F':
                converted_temp = (temp - 273.15) * 9/5 + 32

        print(f"{temp} {unit_from} is equal to {converted_temp:.2f} {unit_to}")
        break
    
    except UnitError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter a numeric value for the temperature.")
