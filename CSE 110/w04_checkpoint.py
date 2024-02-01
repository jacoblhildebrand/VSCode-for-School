temperature = input("Are you converting from Fahrenheit or Celcius? (Input 'F' or 'C') ")

if temperature.upper() not in ['F','C']:
    print("Invalid. Please enter 'F' for Fahrenheit or 'C' for Celcius. ")
else:
    temperature_value = float(input(f"What is the temperature in {temperature.upper()}? "))

    if temperature.upper() == 'F':
        celsius = (temperature_value -32) * 5/9
        print(f"The temperature in Celcius if {celsius:.1f} degrees.")
    else:
        fahrenheit = (temperature_value * 9/5) + 32
        print(f"The temperature in the Fahrenheit is {fahrenheit:.1f} degrees.")