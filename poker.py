'''
  File: poker.py
  Description: This program simulates a game of poker and demontrates
  the use of classes and inheritance.
  Student: Thomas Welborn
  Date Created: 09/26/18
'''
import random


class Card (object):
  # ace = 14, king = 13, queen = 12, etc.
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12
    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object 
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str(self.rank)
    return rank + self.suit

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank


class Deck (object):
  # constructor
  # n is the number of decks
  # 9This parameter is useful if you are playing a large game and need
  # two or more decks shuffled together.)
  def __init__ (self, n = 1):
    self.deck = []
    for i in range(n):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card(rank, suit)
          self.deck.append(card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      # treats the deck like a stack
      return self.deck.pop(0)


class Poker (object):
  def __init__ (self, num_players = 2, num_cards = 5):
    # make the deck and shuffle it
    self.deck = Deck()
    self.deck.shuffle()
    # hold hands in a list holding lists of card objects
    self.all_hands = []
    self.numCards_in_Hand = num_cards

    # deal all the hands
    for i in range (num_players):
      hand = []
      for j in range (self.numCards_in_Hand):
        hand.append (self.deck.deal())
      self.all_hands.append (hand)

  # simulates playing a game of poker
  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.all_hands)):
      sorted_hand = sorted (self.all_hands[i], reverse = True)
      self.all_hands[i] = sorted_hand
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str(card) + ' '
      print ('Player ' + str(i + 1) + ' : ' + hand_str)
    print(' ')
  
    # determine the type of each hand and print
    # also determine points/type for each hand and store in lists
    # the points as calculated with the formula, will be ints
    points_hand = []
    # hand types will be strings
    hand_types = []
    # hand type values will be numbers 1-10 as in the key
    hand_types_vals = []  

    for i in range (len(self.all_hands)):
      point_count = 0
      type_str = ' '

      point_count = self.is_royal(self.all_hands[i])
      if (point_count != 0):
        type_str = 'Royal Flush'
        points_hand.append(point_count)
        hand_types.append(type_str)
        hand_types_vals.append(10)
        print ('Player ' + str(i + 1) + ' : ' + type_str)
        continue

      point_count = self.is_straight_flush(self.all_hands[i])
      if (point_count != 0):
        type_str = 'Straight Flush'
        points_hand.append(point_count)
        hand_types.append(type_str)
        hand_types_vals.append(9)
        print ('Player ' + str(i + 1) + ' : ' + type_str)
        continue

      point_count = self.is_four_kind(self.all_hands[i])
      if (point_count != 0):
        type_str = 'Four of a Kind'
        points_hand.append(point_count)
        hand_types.append(type_str)
        hand_types_vals.append(8)
        print ('Player ' + str(i + 1) + ' : ' + type_str)
        continue

      point_count = self.is_full_house(self.all_hands[i])
      if (point_count != 0):
        type_str = 'Full House'
        points_hand.append(point_count)
        hand_types.append(type_str)
        hand_types_vals.append(7)
        print ('Player ' + str(i + 1) + ' : ' + type_str)
        continue

      point_count = self.is_flush(self.all_hands[i])
      if (point_count != 0):
        type_str = 'Flush'
        points_hand.append(point_count)
        hand_types.append(type_str)
        hand_types_vals.append(6)
        print ('Player ' + str(i + 1) + ' : ' + type_str)
        continue

      point_count = self.is_straight(self.all_hands[i])
      if (point_count != 0):
        type_str = 'Straight'
        points_hand.append(point_count)
        hand_types.append(type_str)
        hand_types_vals.append(5)
        print ('Player ' + str(i + 1) + ' : ' + type_str)
        continue

      point_count = self.is_three_kind(self.all_hands[i])
      if (point_count != 0):
        type_str = 'Three of a Kind'
        points_hand.append(point_count)
        hand_types.append(type_str)
        hand_types_vals.append(4)
        print ('Player ' + str(i + 1) + ' : ' + type_str)
        continue

      point_count = self.is_two_pair(self.all_hands[i])
      if (point_count != 0):
        type_str = 'Two Pair'
        points_hand.append(point_count)
        hand_types.append(type_str)
        hand_types_vals.append(3)
        print ('Player ' + str(i + 1) + ' : ' + type_str)
        continue

      point_count = self.is_one_pair(self.all_hands[i])
      if (point_count != 0):
        type_str = 'One Pair'
        points_hand.append(point_count)
        hand_types.append(type_str)
        hand_types_vals.append(2)
        print ('Player ' + str(i + 1) + ' : ' + type_str)
        continue

      point_count = self.is_high_card(self.all_hands[i])
      if (point_count != 0):
        type_str = 'High Card'
        points_hand.append(point_count)
        hand_types.append(type_str)
        hand_types_vals.append(1)
        print ('Player ' + str(i + 1) + ' : ' + type_str)
        continue     
 



    # determine winner and print
    highest_player = 0
    for i in range (len(hand_types_vals) - 1):
      if (hand_types_vals[i] < hand_types_vals[i+1]):
        highest_player = i+1

    # determine if there are any ties
    # since the ties are very low chance, it will only take into account winners.
    tie_count = 0
    tie_players = []
    highest_hand_type = hand_types_vals[highest_player]
    for i in range (len(hand_types_vals)):
      if (hand_types_vals[i] == highest_hand_type):
        tie_count += 1
        tie_players.append(i)

    if (tie_count == 1):
      print(' ')
      print ('Player ' + str(highest_player + 1) + ' wins.')
      return
    else:
      print(' ')
      # need a list to keep track of the points of tie_players
      tie_players_highest_index = tie_players[0]
      for j in range (len(tie_players) - 1):
        if ( (points_hand[tie_players[j]]) < (points_hand[tie_players[j + 1]]) ):
          tie_players_highest_index = j+1
      print ('Player ' + str(tie_players_highest_index + 1) + ' wins.')
      return
        
        


  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return 0

    points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points


  
  def is_straight_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0

    rank_order = True
    for i in range (len(hand) - 1):
      rank_order = rank_order and (hand[i].rank == (hand[i+1].rank + 1))

    if (not rank_order):
      return 0

    points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points
  


  # determines if first four or last four are the same and sums points
  def is_four_kind (self, hand): 
    flag = True
    same_count_first_four = 0
    same_count_last_four = 0
    for i in range (len(hand) - 2):
      if (hand[i].rank == hand[i+1].rank):
        same_count_first_four += 1
    for i in range (1, (len(hand) - 1)):
      if (hand[i].rank == hand[i+1].rank):
        same_count_last_four += 1

    if (same_count_first_four == 3) or (same_count_last_four == 3):
      flag = True
    else:
      flag = False

    if (not flag):
      return 0

    if (same_count_first_four == 3):
      points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)
      return points

    else:
      points = 8 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3
      points = points + (hand[3].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1
      points = points + (hand[0].rank)
      return points  



  def is_full_house (self, hand):
    same_count_first_three = 0
    same_count_last_three = 0
    for i in range (len(hand) - 3):
      if (hand[i].rank == hand[i+1].rank):
        same_count_first_three += 1
    for i in range (2, (len(hand) - 1)):
      if (hand[i].rank == hand[i+1].rank):
        same_count_last_three += 1

    if (same_count_first_three == 2) and (hand[3].rank == hand[4].rank):
      points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)
      return points
    elif (same_count_last_three == 2) and (hand[0].rank == hand[1].rank):
      points = 7 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3
      points = points + (hand[4].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
      points = points + (hand[1].rank)
      return points
    else:
      return 0



  def is_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0

    points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points



  def is_straight (self, hand):
    rank_order = True
    for i in range (len(hand) - 1):
      rank_order = rank_order and (hand[i].rank == (hand[i+1].rank + 1))

    if (not rank_order):
      return 0

    points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points



  def is_three_kind (self, hand):
    same_count_first_three = 0
    same_count_mid_three = 0
    same_count_last_three = 0

    for i in range (len(hand) - 3):
      if (hand[i].rank == hand[i+1].rank):
        same_count_first_three += 1
    for i in range (1, len(hand) - 2):
      if (hand[i].rank == hand[i+1].rank):
        same_count_mid_three += 1
    for i in range (2, (len(hand) - 1)):
      if (hand[i].rank == hand[i+1].rank):
        same_count_last_three += 1

    if (same_count_first_three == 2):
      points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)
      return points
    elif (same_count_last_three == 2):
      points = 7 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3
      points = points + (hand[4].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
      points = points + (hand[1].rank)
      return points
    elif (same_count_mid_three == 2):
      points = 7 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3
      points = points + (hand[3].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
      points = points + (hand[4].rank)
      return points
    else:
      return 0



  def is_two_pair (self, hand):
    if ((hand[0].rank == hand[1].rank) and (hand[2].rank == hand[3].rank)):
      points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)
      return points
    elif ((hand[1].rank == hand[2].rank) and (hand[3].rank == hand[4].rank)):
      points = 3 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3
      points = points + (hand[3].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1
      points = points + (hand[0].rank)
      return points
    else:
      return 0
 

  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_one_pair (self, hand):
    one_pair = False
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        one_pair = True
        break
    if (not one_pair):
      return 0

    points = 2 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points


  def is_high_card (self, hand):
    points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    return points

  

def main():
  player_count = 1
  while ((player_count < 2) or (player_count > 6)):
    try:
    # prompt the user to enter the number of players
      player_count = int (input ('Enter number of players: '))
    except:
    # prompt the user to enter the number of players
      player_count = int (input ('Enter number of players: '))


  # create the Poker object
  game = Poker(num_players = player_count)

  # play the game - poker
  game.play()

# do not remove this line above main()
if __name__ == '__main__':
  main()


