vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

suits = ['spades', 'clubs', 'hearts', 'diamonds']

def deck_with_lambda_map_zip():
    return list(map(lambda x: '-'.join(x),sum(list(map(lambda x: [*list(zip(suits,[x, x, x, x]))], vals)),[])))

def deck_without_lambda_map_zip():
    '''This function will create a deck of 52 cards(13 each of spades, clubs, hearts, diamonds)'''
    return [x + "-" + y for x in suits for y in vals]

# function for playing pocker
def pocker(card_count: int, Player_A_cards: list, player_B_cards: list) -> "returns a string":
    '''This function should take input of card count and player A set of cards and player B set cards
    and it will check the rules of poker and decide who is the winner and will return winner player string'''

    deck = deck_without_lambda_map_zip(suits, vals)

    winner = []
    pocker_dict = {
        "royal_flush" : ["hearts-ace","hearts-king","hearts-queen","hearts-jack","hearts-10"],
        "straight_flush" : ["clubs-10","clubs-9","clubs-8","clubs-7","clubs-6"],
        "four_kind" : ["clubs-queen","hearts-queen","spades-queen","diamonds-queen","clubs-5"],
        "full_house" : ["hearts-ace","spades-ace","diamonds-ace","spades-king","hearts-king"],
        "flush" : ["hearts-king","hearts-8","hearts-6","hearts-4","hearts-2"],
        "straight" : ["hearts-8","clubs-7","diamonds-6","spades-5","hearts-4"],
        "three_kind" : ["clubs-queen","hearts-queen","spades-queen","hearts-7","clubs-2"],
        "two_pair" : ["diamonds-jack","hearts-jack","spades-9","diamonds-9","clubs-5"],
        "one_pair" : ["hearts-king","spades-king","diamonds-9","spades-8","hearts-4"],
        "high_card" : ["hearts-ace","clubs-queen","hearts-6","spades-4","diamonds-2"]
    }

    pocker_rule = ["royal_flush","straight_flush","four_kind","full_house","flush","straight","three_kind","two_pair","one_pair","high_card"]

    if not(card_count >= 3 and card_count <= 5):
        raise ValueError('card count must be grater than 3 and less than 5')
    elif not(bool(Player_A_cards) or bool(player_B_cards)):
        raise ValueError('Null set of cards. Please enter valid set of cards')
    elif len(Player_A_cards) != card_count or len(player_B_cards) != card_count:
        raise ValueError('Invalid set of cards. Count of Player A and Player B set of cards should be same as card count')
    elif not(all(item in deck for item in Player_A_cards) or all(item in deck for item in Player_A_cards)):
        raise ValueError('Invalid cards. Please enter valid card names')
    elif len(Player_A_cards) != len(set(Player_A_cards)) or len(player_B_cards) != len(set(player_B_cards)):
        raise ValueError('Repeated cards. Cards cannot repeat as we are using one deck of cards')
    else:
        Player_A_Rule = [i for indx,i in enumerate(pocker_rule) if list(map(lambda x: all(item in x[1] for item in Player_A_cards),pocker_dict.items()))[indx] == True]
        Player_B_Rule = [i for indx,i in enumerate(pocker_rule) if list(map(lambda x: all(item in x[1] for item in player_B_cards),pocker_dict.items()))[indx] == True]
        if not(bool(Player_A_Rule)) and not(bool(Player_B_Rule)):
            winner = "NA"
        elif not(bool(Player_A_Rule)) and bool(Player_B_Rule):
            winner = "B"
        elif bool(Player_A_Rule) and not(bool(Player_B_Rule)):
            winner = "A"
        elif Player_A_Rule != Player_B_Rule:
            if pocker_rule.index(Player_A_Rule) > pocker_rule.index(Player_B_Rule):
                winner = "A"
            else:
                winner ="B"

    return winner























