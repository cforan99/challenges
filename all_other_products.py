def all_other_products(nums):
	"""Given a list of integers, return a list of the products of all other integers in the list, without dividing."""
	products = [1]*len(nums)
	for i in range(len(nums)):
		products[:i] = [p*nums[i] for p in products[:i]]
		products[i+1:] = [p*nums[i] for p in products[i+1:]]
	return products

