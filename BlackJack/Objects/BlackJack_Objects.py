#################Still haven't solved the Ace Problem

import random
from Exceptions import BlackJack_Exceptions

Suits = ["Spades","Clubs","Hearts","Diamonds"]
Ranks = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
Values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}

class Card:
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = Values[rank]

	def __str__(self):
		return self.rank + " of " + self.suit

class Deck:
	
	def __init__(self):
		self.all_cards = []

		for suit in Suits:
			for rank in Ranks:
				created_card = Card(suit,rank)
				self.all_cards.append(created_card)

	def shuffle(self):
		random.shuffle(self.all_cards)
		return

	def deal_one(self):
		return self.all_cards.pop()

	def take_back(self,new_cards):
		self.all_cards.extend(new_cards)
		return

class Bankroll:

	def __init__(self,balance):
		self.balance = balance

	def bet(self, betamount):
		if betamount > self.balance:
			raise BlackJack_Exceptions.OverBet
		elif betamount <= 0:
			raise BlackJack_Exceptions.NonPositiveBet
		else:
			print("\n\n*********************************************************************")
			print(f"\n\nYour bet for {betamount} is confirmed.")
			self.balance = self.balance - betamount
			print(f"Your remaining bankroll balance is {self.balance}.")

	def win(self, winamount):
		self.balance = self.balance + 1.5*(winamount)
		print(f"Congrats you won! Your new backroll balance is {self.balance}!")
		return

	def tie(self,betamount):
		self.balance = self.balance + betamount
		print(f"Tie hand! Your bet has been returned to your bankroll and your curent bankroll balance is {self.balance}.")
		return

	def __str__(self):
		return "Your current bankroll balance is $" + self.balance

class Player:
	def __init__(self,name):
		self.name = name
		self.hand = []
		self.ace = False

	def total_value(self):
		current_value = 0
		for card in self.hand:
			current_value += card.value
		return current_value

	def add_cards(self, new_card):
		self.hand.append(new_card)
		if new_card.rank == "Ace":
			self.ace = True
		else:
			pass
		while self.ace:
			for card in self.hand:
				if card.rank == "Ace":
					if ((self.total_value())-(card.value)) <= 10:
						card.value = 11
						return
					else:
						card.value = 1
						return
				else:
					pass
	def empty_hand(self):
		return self.hand.clear()

	def keep_playing(self):
		return input("\n/Keep playing? Type yes or no: ")

	def __str__(self):
		current_hand = f"\n{self.name}'s Current Hand:\n\n"
		for card in self.hand:
			current_hand += (card.__str__() + "\n")
		return current_hand




