investment = float(input("Enter yearly investment amount: "))
age = int(input("Enter girl's age: "))
duration = int(input("Enter investment duration (in years): "))
start_year = int(input("Enter starting year: "))
maturity_year = int(input("Enter maturity year: "))

# calculating maturity amount
r = 7.6 / 100  # rate of interest for SSY
n = 1  # compounded annually
t = maturity_year - start_year + 1
P = investment
A = P * ((1 + r / n) ** (n * t) - 1) / (r / n)

# printing the result
print(f"Maturity amount for girl's age {age} at maturity year {maturity_year} is: {round(A, 2)}")