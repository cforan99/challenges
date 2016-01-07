def get_max_profit(stock_prices_yesterday):
	lowest_price = (stock_prices_yesterday[0], 0)  #will hold a tuple with the min price and the index
	highest_price = (None, None) #will hold a tuple with the max price and the index

	for i in range(0, len(stock_prices_yesterday)):
		if stock_prices_yesterday[i] < lowest_price[0]:
			lowest_price = (stock_prices_yesterday[i], i)

	for i in range(0, len(stock_prices_yesterday)):
		if stock_prices_yesterday[i] > highest_price[0] and i > lowest_price[1]:
			highest_price = (stock_prices_yesterday[i], i)

	if highest_price == (None, None):
		lowest_index = lowest_price[1] - 1
		highest_price = lowest_price
		lowest_price = (stock_prices_yesterday[lowest_index], lowest_index)

	print "Buy at", lowest_price, "and sell at", highest_price

	return highest_price[0] - lowest_price[0]

