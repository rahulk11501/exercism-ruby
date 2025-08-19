"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in ['J', 'K', 'Q']:
        return 10
    if card == 'A':
        return 1
    return int(card)
    


def higher_card(card_one: str, card_two: str) -> tuple | str:
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    card_one_val = value_of_card(card_one)
    card_two_val = value_of_card(card_two)
    if card_one_val == card_two_val:
        return (card_one, card_two)
    if card_one_val > card_two_val:
        return card_one
    return card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    card_one_val = value_of_card(card_one)
    card_two_val = value_of_card(card_two)
    if 'A' in [card_one, card_two]:
        return 1
    if card_one_val + card_two_val + 11 > 21:
        return 1
    return 11
    


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    card_one_val = value_of_card(card_one)
    card_two_val = value_of_card(card_two)
    if card_one == 'A':
        total = 11 + card_two_val
    elif card_two == 'A':
        total = 11 + card_one_val
    else:
        total = card_one_val + card_two_val

    return total == 21


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    card_one_val = value_of_card(card_one)
    card_two_val = value_of_card(card_two)
    return card_one_val == card_two_val


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    total = value_of_card(card_one) + value_of_card(card_two)
    return total in [9, 10, 11]
