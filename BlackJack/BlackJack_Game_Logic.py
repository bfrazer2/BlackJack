from Objects import BlackJack_Objects
from Exceptions import BlackJack_Exceptions

class Game:

	dealer = BlackJack_Objects.Player("Dealer")
	player_one = BlackJack_Objects.Player("Player One")

	player_one_bankroll = BlackJack_Objects.Bankroll(500)

	new_deck = BlackJack_Objects.Deck()
	new_deck.shuffle()

	game_on = True

	while game_on:
		betting = True
		while betting:
			try:
				currentbet = int(input("Please enter your bet as a whole integer value: "))
				player_one_bankroll.bet(currentbet)
				betting = False
				break
			except ValueError:
				print("Your bet must be entered as a whole integer value, in numeric form.")
			except BlackJack_Exceptions.OverBet:
				print(f"Your bet must be lower than or equal to your current bankroll balance of {player_one_bankroll.balance}.")
			except BlackJack_Exceptions.NonPositiveBet:
				print("Your bet must be greater than zero.")

		player_one.add_cards(new_deck.deal_one())

		dealer.add_cards(new_deck.deal_one())

		player_one.add_cards(new_deck.deal_one())

		dealer.add_cards(new_deck.deal_one())


		print("\n\n---------------------------------------------------------------------")
		print(f"\nYou have the {player_one.hand[0]} and the {player_one.hand[1]}.")
		print(f"\nThe dealer has the {dealer.hand[0]} and a facedown card.\n")
		print("\n\n*********************************************************************")


		player_turn = True
		player_bust = False
		while player_turn:

			if player_one.total_value == 21:
				print("\n*********************************************************************")
				print("You hit 21! Dealer's turn; good luck!.")
				print("\n\n\n*********************************************************************")
				player_turn = False
				break
			
			else:
				player_hitting = True
				while player_hitting:
					hit_or_stay = input("Please choose to Hit or Stay: ")

					if hit_or_stay.lower() != "hit" and hit_or_stay.lower() != "stay":
						print("Please enter either Hit or Stay")

					elif hit_or_stay.lower() == "stay":

						print("\n*********************************************************************")
						print(f"You are staying on {player_one.total_value()}")
						print("\n*********************************************************************")
						player_hitting = False
						player_turn = False
						player_one.ace = False
						break

					elif hit_or_stay.lower() == "hit":
						player_one.add_cards(new_deck.deal_one())
						print("\n*********************************************************************")
						print(player_one)

						
						if player_one.total_value() > 21:
							print(f"\nBust! Remaining balance is {player_one_bankroll.balance}.")
							print("\n*********************************************************************")
							player_hitting = False
							player_turn = False
							player_bust = True
							break
						else:
							print(f"\nThe dealer has a {dealer.hand[0]} showing.")
							print("\n*********************************************************************")
		
		dealer_turn = True

		while dealer_turn:

			

			if player_bust:
				dealer_turn = False
				break

			else:
				print(dealer)
				dealer_hitting = True
				while dealer_hitting:
					
					if dealer.total_value() > player_one.total_value():
						print(f"Dealer wins! Reamining balance is {player_one_bankroll.balance}.")
						print("\n*********************************************************************")
						dealer_hitting = False
						dealer_turn = False
						break
					elif dealer.total_value() == player_one.total_value():
						player_one_bankroll.tie(currentbet)
						dealer_turn = False
						break
					else:
						dealer.add_cards(new_deck.deal_one())
						print(dealer)
						if dealer.total_value() > 21:
							print("Dealer bust!\n")
							player_one_bankroll.win(currentbet)
							print("\n*********************************************************************")
							dealer_hitting = False
							dealer_turn = False
							break
						else:
							pass

		new_deck.take_back(player_one.hand)
		new_deck.take_back(dealer.hand)
		player_one.empty_hand()
		dealer.empty_hand()
		new_deck.shuffle()

		if player_one_bankroll.balance == 0:
			print("You're out of money to bet! Better luck next time.")
			print("\n*********************************************************************")
			game_on = False
			break
		
		next_hand = True
		while next_hand:
			new_hand = player_one.keep_playing()
			if new_hand.lower() != "yes" and new_hand.lower() != "no":
				print ("Please enter either yes or no.")
			elif new_hand.lower() == "yes":
				game_on = True
				print("\n*********************************************************************")
				break
			elif new_hand.lower() == "no":
				print(f"Nice session! Your ending bankroll balance is {player_one_bankroll.balance}.")
				print("\n*********************************************************************")
				game_on = False
				break

if __name__ == "__main__":
	Game()


		


