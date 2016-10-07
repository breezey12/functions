from interest import *


def test_calculate_future_value_annual():
	assert calculate_future_value_annual(principal=100, 
										 rate=.01, 
										 number_of_years=1) == 101

	assert calculate_future_value_annual(principal=100, 
										 rate=.05, 
										 number_of_years=10) == 162.8894626777442

	

