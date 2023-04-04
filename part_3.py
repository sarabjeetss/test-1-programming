def convertSalary(salary, country):
    if country == "Canada":
        converted_salary = salary
        currency_name = "CAD"
    elif country == "USA":
        converted_salary = salary / 0.91 / 1.18
        currency_name = "USD"
    elif country == "Cambodia":
        converted_salary = salary / 0.91 / 4847.38
        currency_name = "Cambodian riel"
    elif country == "United Kingdom":
        converted_salary = salary / 0.91
        currency_name = "Pound Sterling"
    else:
        print("Invalid country name")
        return None
    
    if country == "Canada":
        avg_salary = 64000
    elif country == "USA":
        avg_salary = 56516 / 0.91
    elif country == "Cambodia":
        avg_salary = 5649856 / 0.91 / 4847.38
    elif country == "United Kingdom":
        avg_salary = 35423
    
    if converted_salary > avg_salary:
        message = "You will be rich in {} with a salary of {} {}".format(country, round(converted_salary, 2), currency_name)
    else:
        message = "You will be poor in {} with a salary of {} {}".format(country, round(converted_salary, 2), currency_name)
    
    return message


salary = float(input("Enter your salary per annum in Euros: "))
country = input("Enter the country you want to migrate to: ")

result = convertSalary(salary, country)
if result:
    print(result)