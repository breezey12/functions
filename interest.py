def calculate_future_value_annual(principal, rate, number_of_years):
	principal * (1 + rate) ** number_of_years


def calculate_capital_gains(gains, tax_rate):
	gains * tax_rate

def calculate_after_tax_return(principal, rate, number_of_years, tax_rate):
	profits = calculate_future_value_annual(principal, rate, number_of_years)
	capital_gains = calculate_capital_gains(profits, tax_rate)
	return profits - capital_gains
