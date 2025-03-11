def count_older_than(people, min_age):
    return count(people, lambda person: person.age > min_age)

def indices_of_cards_with_suit(cards, suit):
    return indices_of(cards, lambda card: card.suit == suit)