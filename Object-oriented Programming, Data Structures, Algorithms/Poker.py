#  Description: Demonstrates oop by simulating a game of poker.

import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
  SUITS = ('C', 'D', 'H', 'S')
  
  # Constructor. Default is  queen of spades
  def __init__(self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card
  def __str__(self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = self.rank
    return str(rank) + self.suit

  # equality tests
  def __eq__(self, other):
    return (self.rank == other.rank)

  def __lt__(self, other):
    return (self.rank < other.rank)

  def __gt__(self, other):
    return (self.rank > other.rank)

class Deck (object):
  # constructor
  def __init__(self):
    # a list of card objects
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card(rank, suit)
        self.deck.append(card)

  # shuffle the deck
  def shuffle(self):
    random.shuffle(self.deck)

  # deal a single card
  def deal(self):
    if (len(self.deck) == 0):
      return None              # None is used with objects to return nothing
    else:
      return self.deck.pop(0)
  
class Poker (object):
  def __init__(self, n_players):
    self.deck = Deck()
    self.deck.shuffle()
    self.hands = []
    numCards_in_Hand = 5
    total_cards_to_deal = numCards_in_Hand * n_players 

    # Deal the cards
    for i in range(n_players): # Create a list of empty hands for each player
      hand = []
      self.hands.append(hand)

    while(total_cards_to_deal > 0): # Deal a card to each player round robin style
      for i in range(len(self.hands)):
        self.hands[i].append(self.deck.deal())
        total_cards_to_deal -= 1

  def play(self):
    # sort the hands of each player and print and store
    sortedHands = []    
    for i in range(len(self.hands)):
      sortedHand = sorted(self.hands[i], reverse = True)
      hand = ''
      for card in sortedHand:
        hand += str(card) + ' '
      print('Player ' + str(i + 1) + ': ' + hand)
      sortedHands.append(sortedHand)

    # determine the type of each hand and print
    points_hand = []  # create list to store points for each hand
    for i in range(len(sortedHands)):
      score = self.check_points(sortedHands[i])
      points_hand.append(score)

    print()
    for i in range(len((points_hand))):
      print('Player ' + str(i + 1) + ': ' + self.check_hand(points_hand[i]))
    
    # determine winner and print
    winner_points = max(points_hand)
    index_winner = points_hand.index(winner_points)
    num_winners = points_hand.count(winner_points)
    if(num_winners == 1):
      # Print winner when there is no ties
      print()
      print("Player", index_winner + 1, "wins.")
    else:
      # Track the winners
      winners = []
      for i in range(len(points_hand)):
        if(max(points_hand) == points_hand[i]):
          winners.append(i)
      
      # Track points of the winners
      points_of_winners = []
      h = winner_points
      # If the tie is between "Four of a Kind" hands
      if(h == 8):
        for i in winners:
          if(sortedHands[i][0].rank != sortedHands[i][1].rank):
            c5 = sortedHands[i][0].rank
            c4 = sortedHands[i][1].rank
            c3 = c4
            c2 = c3
            c1 = c2
          else:
            c5 = sortedHands[i][-1].rank
            c4 = sortedHands[i][0].rank
            c3 = c4
            c2 = c3
            c1 = c2
          
          # Store the player number and total points they have
          total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
          points_of_winners.append(total_points)

      # If the tie is between "Full House" hands
      elif(h == 7):
        for i in winners:
          if(sortedHands[i][1].rank == sortedHands[i][2].rank):
            c5 = sortedHands[i][-1].rank
            c4 = c5
            c3 = sortedHands[i][0].rank
            c2 = c3
            c1 = c2
          else:
            c5 = sortedHands[i][0].rank
            c4 = c5
            c3 = sortedHands[i][-1].rank
            c2 = c3
            c1 = c2

          total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
          points_of_winners.append(total_points)
      
      # If the tie is between "three of a kind" hands
      elif(h == 4):
        for i in winners:
          if((sortedHands[i][0].rank == sortedHands[i][1].rank) and (sortedHands[i][1].rank == sortedHands[i][2].rank)):
            c5 = sortedHands[i][-1].rank
            c4 = c5
            c3 = sortedHands[i][0].rank
            c2 = c3
            c1 = c2

          elif((sortedHands[i][1].rank == sortedHands[i][2].rank) and (sortedHands[i][2].rank == sortedHands[i][3].rank)):
            c5 = sortedHands[i][-1].rank
            c4 = sortedHands[i][0].rank
            c3 = sortedHands[i][1].rank
            c2 = c3
            c1 = c2

          else:
            c5 = sortedHands[i][1].rank
            c4 = sortedHands[i][0].rank
            c3 = sortedHands[i][-1].rank
            c2 = c3
            c1 = c2

          total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
          points_of_winners.append(total_points)

      # If the tie is between "two pair" hands
      elif(h == 3):
        for i in winners:
          mock = []
          for j in range(5):
            mock.append(sortedHands[i][j].rank)

          # Find the card with no pair!
          for k in mock:
            if(mock.count(k) == 1):
              odd_one = k
          odd_index = mock.index(odd_one)

          if(odd_index == 0):
            c5 = mock[0]
            c4 = mock[-1]
            c3 = c4
            c2 = mock[1]
            c1 = c2

          elif(odd_index == 2):
            c5 = mock[2]
            c4 = mock[-1]
            c3 = c4
            c2 = mock[1]
            c1 = c2

          else:
            c5 = mock[-1]
            c4 = mock[-2]
            c3 = c4
            c2 = mock[1]
            c1 = c2           

          total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
          points_of_winners.append(total_points)

      # If the tie is between "one pair" hands
      elif(h == 2):
        for i in winners:
          if((sortedHands[i][0].rank == sortedHands[i][1].rank)):
            c5 = sortedHands[i][-1].rank
            c4 = sortedHands[i][-2].rank
            c3 = sortedHands[i][-3].rank
            c2 = sortedHands[i][0].rank
            c1 = c2

          elif((sortedHands[i][1].rank == sortedHands[i][2].rank)):
            c5 = sortedHands[i][-1].rank
            c4 = sortedHands[i][-2].rank
            c3 = sortedHands[i][0].rank
            c2 = sortedHands[i][1].rank
            c1 = c2
          
          elif((sortedHands[i][2].rank == sortedHands[i][3].rank)):
            c5 = sortedHands[i][-1].rank
            c4 = sortedHands[i][1].rank
            c3 = sortedHands[i][0].rank
            c2 = sortedHands[i][2].rank
            c1 = c2

          else:
            c5 = sortedHands[i][2].rank
            c4 = sortedHands[i][1].rank
            c3 = sortedHands[i][0].rank
            c2 = sortedHands[i][-1].rank
            c1 = c2

          total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
          points_of_winners.append(total_points)
          
      # All other ties
      else:
        for i in winners:  
          c5 = sortedHands[i][-1].rank
          c4 = sortedHands[i][-2].rank
          c3 = sortedHands[i][-3].rank
          c2 = sortedHands[i][-4].rank
          c1 = sortedHands[i][0].rank

          total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
          points_of_winners.append(total_points)

    # index order of victory
      order_index = []
      for i in range (len(winners)):
        n = points_of_winners.index(max(points_of_winners))
        order_index.append(n)
        points_of_winners[n] = 0

      # Print the winner followed by the ties in descending fashion
      print()
      print("Player", winners[order_index[0]] + 1, "wins.")
      print()
      for i in order_index[1:]:
        print("Player", winners[i] + 1, "ties.")





  # determine if a hand is a royal flush
  def is_royal(self, hand):
    same_suit = True
    # determine if the hand is all of the same of suit
    for i in range (len(hand) -1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if(not same_suit):
      return 0
    
    # determine if the hand is is made of 10, J, Q, K, A
    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)
    if(same_suit and rank_order):
      return 10
    else:
      return 0

  # determine if a hand is a straight flush
  def is_straight_flush (self, hand):
    same_suit = True
    # determine if the hand is all of the same of suit
    for i in range (len(hand) -1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if(not same_suit):
      return 0

    # determine if the 5 cards are in numerical sequence
    rank_order = True
    for i in range(len(hand)-1):
      rank_order = rank_order and (hand[i].rank == hand[i + 1].rank + 1)
    if(same_suit and rank_order):
      return 9
    else:
      return 0

  # determine if a hand is a four of a kind 
  def is_four_kind (self, hand):
    #  determine if four cards have the same numerical rank
    same_rank_counter = 3
    for i in range(len(hand)-1):
      if(hand[i].rank == hand[i +1].rank):
        same_rank_counter -= 1
        if(same_rank_counter == 0):
          break
      else:
        same_rank_counter = 3
    
    if(same_rank_counter == 0):
      return 8
    else:
      return 0

  # determine if a hand is full house
  def is_full_house (self,hand):
  	# check if first three cards are same rank and last two cards are same rank
    same_rank_1 = True
    for i in range (len(hand) -3):
      same_rank_1 = same_rank_1 and (hand[i].rank == hand[i + 1].rank)
    same_rank_1 = same_rank_1 and (hand[-1].rank == hand[-2].rank)

    # check if first two cards are some rank and last three cards are same rank
    same_rank_2 = (hand[0].rank == hand[1].rank)
    same_rank_2 = same_rank_2 and (hand[-1].rank == hand[-2].rank) and (hand[-2].rank == hand[-3].rank)
    
    if(same_rank_1 or same_rank_2):
      return 7
    else:
      return 0

  # determine if a hand is a flush
  def is_flush(self, hand):
    same_suit = True
    # determine if the hand is all of the same of suit
    for i in range (len(hand) -1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
    
    if(same_suit == True):
      return 6
    else:
      return 0

  # determine if a hand is a straight hand
  def is_straight(self, hand):
    # determine if the 5 cards are in numerical sequence
    rank_order = True
    for i in range(len(hand)-1):
      rank_order = rank_order and (hand[i].rank == hand[i + 1].rank + 1)

    if(rank_order == True):
      return 5
    else:
      return 0

  # determine if a hand is three of a kind
  def is_three_kind (self, hand):
    same_rank_counter = 2
    for i in range(len(hand)-1):
      if(hand[i].rank == hand[i +1].rank):
        same_rank_counter -= 1
        if(same_rank_counter == 0):
          break
      else:
        same_rank_counter = 2
    
    if(same_rank_counter == 0):
      return 4
    else:
      return 0

  # determine if a hand is two pair
  def is_two_pair(self,hand):
    skip = 0
    two_pair_counter = 0  
    for i in range (len(hand)-1):
      if(skip == 1):
        skip = 0
        continue
      if (hand[i].rank == hand[i + 1].rank):
        two_pair_counter +=1
        skip +=1
    
    if(two_pair_counter == 2):
      return 3
    else:
      return 0

  # determine if a hand is one pair
  def is_one_pair (self, hand):
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        return 2
    return 0
  
  # determine if a hand is a high card
  def is_high_card(self, hand):
    return 1

  # Systematically check if a hand meets the requirements from Royal Flush
  # to a High Card
  def check_points(self, hand):
    system = []
    system.append(self.is_royal(hand))
    system.append(self.is_straight_flush(hand))
    system.append(self.is_four_kind(hand))
    system.append(self.is_full_house(hand))
    system.append(self.is_flush(hand))
    system.append(self.is_straight(hand))
    system.append(self.is_three_kind(hand))
    system.append(self.is_two_pair(hand))
    system.append(self.is_one_pair(hand))
    system.append(self.is_high_card(hand))

    # return the value of the hand
    for i in system:
      if(i > 0):
        return i
    
    # Allotment for each hand 
  def check_hand(self, pts):
      if(pts == 10):
        return "Royal Flush"

      if(pts == 9):
        return "Straight Flush"

      if(pts == 8):
        return "Four of a Kind"

      if(pts == 7):
        return "Full House"

      if(pts == 6):
        return "Flush"

      if(pts == 5):
        return "Straight"

      if(pts == 4):
        return "Three of a Kind"

      if(pts == 3):
        return "Two Pair"

      if(pts == 2):
        return "One Pair"

      if(pts == 1):
        return "High Card"


def main():
  # Prompt for the number of players and check the input
  num_players = input('Enter number of players: ')
  while( num_players.isdigit() == False or (int(num_players) < 2 or int(num_players) > 6)):
    num_players = input('Enter number of players: ')
  num_players = int(num_players)
  print()

  # Create an instance of a poker object
  game = Poker(num_players)


  # Play the game
  game.play()

main()
