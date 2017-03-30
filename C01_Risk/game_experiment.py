# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com

from CardBag import PokerCardJoker, PokerCardFault, CardBag
import pandas as pd


JOKER_SIDE_BET = 100
FAULT_SIDE_BET = 180


class Account(object):
    def __init__(self, balance=5000):
        self._balance = balance

    def bet(self, amounts):
        if amounts > self._balance or amounts < 0:
            return False
        else:
            self._balance -= amounts

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        self._balance = balance

    def reward(self, amounts):
        if amounts < 0:
            return False
        else:
            self._balance += amounts


# Normal game
def normal_game(max_time=10, joker_bet=JOKER_SIDE_BET, fault_bet=FAULT_SIDE_BET):

    # Game round.
    # Each round has 10 times,
    # If select fault side, should bet 180(default), another select should bet 100(default).
    # Get one card from cardbag.
    # If cardface is joker, again obtain a card
    # If cardface is reverse, overturn the card, if cardface is joker, the one select
    # joker_side will win 180(default)
    # If card overturn is fault, the one which select fault side will win 100(default)

    game_time = 0
    account_joker = Account()
    account_fault = Account()
    joker_side_balance = []
    fault_side_balance = []
    res = []
    cardbag = CardBag()
    while game_time < max_time:
        res_iteration = []
        account_joker._balance = 5000
        account_fault._balance = 5000
        n = 1000
        while n > 0 and (account_fault.get_balance() > 0 and account_joker.get_balance()) > 0:
            card = cardbag.get_card()
            card_face = card.get_card_face()
            if card_face != 1:
                card_face = card.overturn()
                if card_face == 1:
                    account_fault.bet(FAULT_SIDE_BET)
                    account_joker.reward(FAULT_SIDE_BET)
                    fault_side_balance.append(-1 * FAULT_SIDE_BET)
                    joker_side_balance.append(FAULT_SIDE_BET)
                else:
                    account_fault.reward(JOKER_SIDE_BET)
                    account_joker.bet(JOKER_SIDE_BET)
                    fault_side_balance.append(JOKER_SIDE_BET)
                    joker_side_balance.append(-1 * JOKER_SIDE_BET)
                n -= 1
        if account_fault.get_balance() > account_joker.get_balance():
            res_iteration.append('Fault Side')
        else:
            res_iteration.append('Joker Side')
        res_iteration.append(account_joker.get_balance())
        res_iteration.append(account_fault.get_balance())
        res_iteration.append(1000 - n)
        res.append(res_iteration)
        game_time += 1

    res_df = pd.DataFrame(res, columns=['Winner', 'Joker Balance', 'Fault Balance', 'Round'])
    return res_df


# lever game
def lever_game(max_time=10, lever=2, joker_bet=JOKER_SIDE_BET, fault_bet=FAULT_SIDE_BET, commission=30):

    # In lever game, there are two roles, one is agent, another is player.
    # Agent does not play the game, but agent can offer chip to player
    # By default, player only can select joker_card, and each round, player only need 50
    # If player win, player should be paid 30 to agent, else, player margin account should be minus 100
    # If the margin account become 0, game over

    game_time = 0
    account_agent = Account(5000)
    account_player = Account(2000)
    carbag = CardBag()
    res = []

    while game_time < max_time:
        res_iteration = []
        account_agent.set_balance(5000)
        account_player.set_balance(2000)
        n = 1000
        while n > 0 and account_player.get_balance() > 0:
            card = carbag.get_card()
            card_face = card.get_card_face()
            if card_face != 1:
                card_face = card.overturn()
                if card_face == 1:
                    account_agent.reward(30)
                    account_player.reward(150)
                else:
                    account_player.bet(100)
                n -= 1
        res_iteration.append(account_agent.get_balance())
        res_iteration.append(account_player.get_balance())
        res_iteration.append(1000 - n)
        game_time += 1
        res.append(res_iteration)

    res_df = pd.DataFrame(res, columns=['Agent Balance', 'Player Balance', 'Round'])
    return res_df



if __name__ == '__main__':
    # Normal game, 10 times
    res = normal_game(10)
    # print res

    # Lever game, 10 times
    res_lever = lever_game(10)
    print res_lever