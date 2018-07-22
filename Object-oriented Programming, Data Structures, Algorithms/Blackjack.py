  # Description: Uses the concepts of object oriented programming to simulate a game of blackjack.


import  random

class Card (object):
  RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

  SUITS = ('S', 'D', 'H', 'C')

  # Constructor. Default is  queen of spades
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card
  def __str__ (self):
    if self.rank == 1:
      rank = 'A'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 11:
      rank = 'J'
    else:
      rank = self.rank
    return str(rank) + self.suit

  # equality tests
  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)


class Deck (object):
  # constructor
  def __init__ (self):
    # a list of card objects
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append(card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a single card
  def deal (self):
    if len(self.deck) == 0:
      return None  # None is used with objects to return nothing
    else:
      return self.deck.pop(0)

class Player (object):
  # cards is a list of card objects. Each player will have a hand
  def __init__ (self, cards):
    self.cards = cards

  def hit (self, card):
    self.cards.append(card)

  def getPoints (self):
    count = 0
    for card in self.cards:
      if card.rank > 9:
        count += 10
      elif card.rank == 1:
        count += 11
      else:
        count += card.rank

    # deduct 10 if Ace is there and needed as 1
    for card in self.cards:
      if count <= 21:
        break
      elif card.rank == 1:
        count = count - 10
    
    return count

  # does the player have 21 points or not
  def hasBlackjack (self):
    return len (self.cards) == 2 and self.getPoints() == 21

  # string representation of cards and points
  def __str__ (self):
    hand = ''
    for card in self.cards:
      hand += str(card) + ' '
    hand += "- " + str(self.getPoints()) + " points"
    return hand
  
# Dealer class inherits from the Player class
class Dealer (Player):
  def __init__ (self, cards):
    Player.__init__ (self, cards)
    self.show_one_card = True

  # over-ride the hit() function in the parent class
  # add cards while points < 17, then allow all to be shown
  def hit (self, deck):
    self.show_one_card = False
    while self.getPoints() < 17:
      self.cards.append (deck.deal())

  # return just one card if not hit yet by over-riding the str function
  def __str__ (self):
    if self.show_one_card:
      return str(self.cards[0])
    else:
      return Player.__str__(self)

class Blackjack (object):
  def __init__ (self, numPlayers = 1):
    self.deck = Deck()
    self.deck.shuffle()

    self.numPlayers = numPlayers
    self.Players = []

    # create the number of players specified
    # each player gets two cards
    for i in range (self.numPlayers):
      self.Players.append (Player([self.deck.deal(), self.deck.deal()]))

    # create the dealer
    # dealer gets two cards
    self.dealer = Dealer ([self.deck.deal(), self.deck.deal()])

  def play (self):
    # Print the cards that each player has
    for i in range (self.numPlayers):
      print ('Player ' + str(i + 1) + ': ' + (str(self.Players[i])))

    # Print the cards that the dealer has
    print ('Dealer: ' + str(self.dealer))

    # Each player hits until he says no
    playerPoints = []
    for i in range (self.numPlayers):
      if((self.Players[i]).getPoints() == 21):
        playerPoints.append ((self.Players[i]).getPoints())
        continue
      while True:
        print()
        choice = input ('Player %d do you want to hit? [y / n]: ' % (i + 1))
        if choice in ('y', 'Y'):
          (self.Players[i]).hit (self.deck.deal())
          points = (self.Players[i]).getPoints()
          print ('Player ' + str(i + 1) + ': ' + str(self.Players[i]))
          if points >= 21:
            break
        else:
          break
      playerPoints.append ((self.Players[i]).getPoints())

    # Dealer's turn to hit
    print()
    self.dealer.hit (self.deck)
    dealerPoints = self.dealer.getPoints()
    print ('Dealer: ' + str(self.dealer))

    # determines the outcome
    print()
    for i in range(len(playerPoints)):
      if playerPoints[i] > 21:
        print ('Player %d loses' % (i + 1))
      elif dealerPoints > 21:
        print ('Player %d wins' % (i + 1))
      elif dealerPoints > playerPoints[i]:
        print ('Player %d loses' % (i + 1))
      elif (dealerPoints < playerPoints[i] and playerPoints[i] <= 21):
        print ('Player %d wins' % (i + 1))
      elif dealerPoints == playerPoints[i]:
        if self.Players[i].hasBlackjack() and not self.dealer.hasBlackjack():
          print ('Player %d wins' % (i + 1))
        elif not self.Players[i].hasBlackjack() and self.dealer.hasBlackjack():
          print ('Player %d loses' % (i + 1))
        else:
          print ('Player %d ties' % (i + 1))

def main ():
  numPlayers = eval (input ('Enter number of players: '))
  while (numPlayers < 1 or numPlayers > 6):
    numPlayers = eval (input ('Enter number of players: '))
  print()
  game = Blackjack (numPlayers)
  game.play()

main()


