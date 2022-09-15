class Error(Exception):
	"""Base error class"""
	pass

class OverBet(Error):
	"""Player has entered a bet amount greater than their bankroll balance"""
	pass

class NonPositiveBet(Error):
	"""Player has entered a negative or zero bet amount"""
	pass