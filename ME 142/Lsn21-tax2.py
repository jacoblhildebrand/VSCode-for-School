

# Define the tax rates by province/state
tax_rates = {
    "Alberta": 0.05,
    "Nunavut": 0.05,
    "Yukon": 0.05,
    "Ontario": 0.13,
    "Any other": 0.15
}

# Get the country and province/state from the user
country = input("What country do you live in? ")
province = input("What province/state do you live in? ")

# Check if the country is Canada and the province/state is in the tax_rates dictionary
if country.lower() == "canada" and province.title() in tax_rates:
    tax_rate = tax_rates[province.title()]
elif country.lower() == "canada":
    tax_rate = 0.0
else:
    tax_rate = None

# Print out the tax rate, or an error message if it couldn't be determined
if tax_rate is not None:
    print("Your tax rate is {:.2f}".format(tax_rate))
else:
    print("Tax rate could not be determined for your country and province/state.")