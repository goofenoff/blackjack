import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 
        2, 3, 4, 5, 6, 7, 8, 9, 10, 
        2, 3, 4, 5, 6, 7, 8, 9, 10, 
        2, 3, 4, 5, 6, 7, 8, 9, 10, 
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
playerHand = []
dealerHand = []

class Blackjack:
    def dealCards(hand):
        cards = random.choice(deck)
        hand.append(cards)
        deck.remove(cards)
        
    def total(hand):
        total = 0
        aces = 0
        for card in hand:
            if card in range(1, 11):
                total += card
            elif card == 'J' or card == 'Q' or card == 'K':
                total += 10
            elif card == 'A':
                aces += 1
                total += 11
        while aces > 0 and total > 21:
            total -= 10
            aces -= 1
        return total

    def revealDealerHand():
        if len(dealerHand) == 2:
            return dealerHand[0]
        elif len(dealerHand) > 2:
            return dealerHand[0], dealerHand[1]

for _ in range(2):
    Blackjack.dealCards(playerHand)
    Blackjack.dealCards(dealerHand)

playerValue = Blackjack.total(playerHand)
dealerValue = Blackjack.total(dealerHand)

print(f"You have a hand of {playerHand} for a value of {playerValue}")
print(f"The dealer has a hand of {Blackjack.revealDealerHand()} and X")

while playerValue < 21:
    stayOrHit = input('stay or hit?\n')

    if stayOrHit == 'stay':
        while dealerValue < 16:
            Blackjack.dealCards(dealerHand)
            dealerValue = Blackjack.total(dealerHand)
        print(f"The dealer has a hand of {dealerHand} for a value of {dealerValue}")
        if dealerValue > 21:
            print('You win!')
        elif dealerValue > playerValue:
            print('You lose!')
        else:
            print('You win!')
        break

    elif stayOrHit == 'hit':
        Blackjack.dealCards(playerHand)
        playerValue = Blackjack.total(playerHand)
        print(f"You have a hand of {playerHand} for a value of {playerValue}")

if playerValue > 21:
    print('You lose!')