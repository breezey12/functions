def calculate_future_value_annual(principal, rate, number_of_years):
	return principal * (1 + rate) ** number_of_years


def calculate_taxes_owed(gains, tax_rate):
	return gains * tax_rate

def calculate_after_tax_return(principal, rate, number_of_years, tax_rate):
	return calculate_future_value_annual(principal, rate, number_of_years) - (calculate_future_value_annual(principal, rate, number_of_years) * tax_rate)



