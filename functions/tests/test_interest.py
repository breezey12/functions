from interest import *


def test_calculate_future_value_annual():
	assert calculate_future_value_annual(principal=100, 
										 rate=.01, 
										 number_of_years=1) == 101

	assert calculate_future_value_annual(principal=100, 
										 rate=.05, 
										 number_of_years=10) == 162.8894626777442


def test_after_tax_return():
	assert calculate_after_tax_return(principal=100, 
								      rate=.05, 
									  number_of_years=10,
									  tax_rate=.10) == 146.60051640996977



