# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com

from CardBag import PokerCardJoker, PokerCardFault, CardBag

JOKER_SIDE_BET = 100
FAULT_SIDE_BET = 140


class Account(object):
    def __init__(self):
        self._balance = 5000

    def bet(self, amounts):
        if amounts > self._balance or amounts < 0:
            return False
        else:
            self._balance -= amounts

    def get_balance(self):
        return self._balance

    def reward(self, amounts):
        if amounts < 0:
            return False
        else:
            self._balance += amounts

if __name__ == '__main__':
    '''
    Game round.
    Each round has 10 times,
    If select fault side, should bet 200, another select should bet 50.
    Get one card from cardbag.
    If cardface is joker, again obtain a card
    If cardface is reverse, overturn the card, if cardface is joker, the one select
    joker_side will win 200
    If card overturn is fault, the one which select fault side will win 50
    '''
    account_joker = Account()
    account_fault = Account()
    joker_side_balance = []
    fault_side_balance = []
    cardbag = CardBag()
    n = 1000
    while n > 0 and (account_fault.get_balance() > 0 and account_joker.get_balance()) > 0:
        card = cardbag.get_card()
        card_face = card.get_card_face()
        if card_face != 1:
            card_face = card.overturn()
            if card_face == 1:
                account_fault.bet(FAULT_SIDE_BET)
                account_joker.reward(FAULT_SIDE_BET)
                fault_side_balance.append(-1*FAULT_SIDE_BET)
                joker_side_balance.append(FAULT_SIDE_BET)
            else:
                account_fault.reward(JOKER_SIDE_BET)
                account_joker.bet(JOKER_SIDE_BET)
                fault_side_balance.append(JOKER_SIDE_BET)
                joker_side_balance.append(-1*JOKER_SIDE_BET)
            n -= 1

    print 'Fault Profit'.center(50, '=')
    print fault_side_balance
    print 'Fault Balance : %s' % str(account_fault.get_balance())
    print 'Joker Profit'.center(50, '=')
    print joker_side_balance
    print 'Joker Balance : %s' % str(account_joker.get_balance())
    print 'Iteration : %s' % str(1000 - n)
