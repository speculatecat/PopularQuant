# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com

"""
    本程序为简化版德州扑克胜率验算程序
"""
from enum import Enum,unique


class Poker(object):
    class PokerKind(Enum):
        DIAMONDS = 0
        CLUBS = 1
        HEARTS = 2
        SPADES = 3

    class PokerPoint(Enum):
        IX = 0      # 9
        X = 1       # 10
        XI = 2      # J
        XII = 3     # Q
        XIII = 4    # K
        A = 5       # A

    def __init__(self, poker_kind, poker_point):
        if not (type(poker_kind) is self.PokerKind):
            raise TypeError('poker_kind is a type of Poker.PokerKind.')
        if not (type(poker_point) is self.PokerPoint):
            raise TypeError('poker_point is a type of Poker.PokerPoint.')
        self.poker_kind = poker_kind
        self.poker_point = poker_point

    def __str__(self):
        poker_kind = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
        poker_point = ['9', '10', 'J', 'Q', 'K', 'A']
        poker_face = poker_kind[self.poker_kind.value] + ' - ' + poker_point[self.poker_point.value]
        return poker_face

    @staticmethod
    def poker_sort(poker_1, poker_2):
        if not((type(poker_1) is Poker) and (type(poker_2) is Poker)):
            raise TypeError('poker_1 and poker_2 must be type of Poker.')

        if poker_1.poker_kind.value == poker_2.poker_kind.value:
            if poker_1.poker_point.value > poker_2.poker_point.value:
                return [poker_1, poker_2]
            else:
                return [poker_2, poker_1]
        else:
            if poker_1.poker_kind.value > poker_2.poker_kind.value:
                return [poker_1, poker_2]
            else:
                return [poker_2, poker_1]


class PokerGroup(object):
    class GroupKind(Enum):
        ROYAL_FLUSH = 9
        STRAIGHT_FLUSH = 8
        FOUR_OF_A_KIND = 7
        FULL_HOUSE = 6
        Flush = 5
        STRAIGHT = 4
        THREE_OF_A_KIND = 3
        TWO_PAIR = 2
        ONE_PAIR = 1
        HIGH_CARD = 0

    def __init__(self, poker_group):
        if len(poker_group) < 5:
            raise TypeError('poker_group must be a list,length gt 5.')
        self.group_kind = None
        self.characteristic = {}
        # classify
        if self.is_flush(poker_group):
            if self.is_straight(poker_group):
                if poker_group[0].poker_kind == Poker.PokerKind.SPADES:
                    self.group_kind = PokerGroup.GroupKind.ROYAL_FLUSH
                else:
                    self.group_kind = PokerGroup.GroupKind.STRAIGHT_FLUSH
            else:
                self.group_kind = PokerGroup.GroupKind.Flush
        else:
            if self.is_straight(poker_group):
                self.group_kind = PokerGroup.GroupKind.STRAIGHT
            elif self.is_four_of_a_kind(poker_group):
                self.group_kind = PokerGroup.GroupKind.FOUR_OF_A_KIND
            else:
                if self.is_three_of_a_kind(poker_group):
                    # check if is full house
                    pg = poker_group[:]
                    pg_point = []
                    for i in range(len(pg)):
                        pg_point.append(pg[i].poker_point.value)
                    pg_point_filter = list(set(pg_point))
                    if len(pg_point_filter) == 2:
                        self.group_kind = PokerGroup.GroupKind.FULL_HOUSE
                    else:
                        self.group_kind = PokerGroup.GroupKind.THREE_OF_A_KIND
                else:
                    if self.is_two_pairs(poker_group):
                        self.group_kind = PokerGroup.GroupKind.TWO_PAIR
                    elif self.is_one_pairs(poker_group):
                        self.group_kind = PokerGroup.GroupKind.ONE_PAIR
                    else:
                        self.group_kind = PokerGroup.GroupKind.HIGH_CARD


    @staticmethod
    def is_royal_flush(poker_group):
        pg = poker_group[:]
        royal_flush = False
        poker_points = []
        royal_flush_points = [1, 2, 3, 4, 5] # 10 J Q K A
        while True:
            if len(pg) > 0:
                poker = pg.pop()
                poker_points.append(poker.poker_point.value)
                if poker.poker_kind != Poker.PokerKind.SPADES:
                    # 如果出现不是黑桃的牌,肯定不是皇家同花顺
                    break
            else:
                if sorted(poker_points) == royal_flush_points:
                    royal_flush = True
                break
        return royal_flush

    @staticmethod
    def is_straight(poker_group):
        pg_point = []
        straight = True
        for i in range(len(poker_group)):
            pg_point.append(poker_group[i].poker_point.value)
        pg_point.sort()
        _len = len(pg_point)
        for j in range(0, _len - 2):
            if pg_point[j+1] - pg_point[j] != pg_point[j+2] - pg_point[j+1]:
                print '%i'.center(15, '-') %j
                print 'break'.center(15, '=')
                straight = False
                break
        return straight

    @staticmethod
    def is_flush(poker_group):
        pg = poker_group[:]
        flush = False
        init_kind = pg.pop().poker_kind
        while True:
            if len(pg) > 0:
                poker = pg.pop()
                if poker.poker_kind != init_kind:
                    break
            else:
                flush = True
                break
        return flush

    @staticmethod
    def is_four_of_a_kind(poker_group):
        pg = poker_group[:]
        four_of_a_kind = False
        pg_point = []
        for i in range(len(pg)):
            pg_point.append(pg[i].poker_point.value)
        if len(set(pg_point)) == 2:
            pg_point_filter = list(set(pg_point))
            if (pg_point.count(pg_point_filter[0]) == 4) or (pg_point.count(pg_point_filter[1]) == 4):
                four_of_a_kind = True
        return four_of_a_kind

    @staticmethod
    def is_three_of_a_kind(poker_group):
        pg = poker_group[:]
        three_of_a_kind = False
        pg_point = []
        for i in range(len(pg)):
            pg_point.append(pg[i].poker_point.value)
        if len(set(pg_point)) == 2:
            pg_point_filter = list(set(pg_point))
            if (pg_point.count(pg_point_filter[0]) == 3) or (pg_point.count(pg_point_filter[1]) == 3):
                three_of_a_kind = True
        elif len(set(pg_point)) == 3:
            pg_point_filter = list(set(pg_point))
            if (pg_point.count(pg_point_filter[0]) == 3) or (pg_point.count(pg_point_filter[1]) == 3) or (pg_point.count(pg_point_filter[2]) == 3):
                three_of_a_kind = True
        return three_of_a_kind

    @staticmethod
    def is_two_pairs(poker_group):
        pg = poker_group[:]
        two_paris = False
        pg_point = []
        for i in range(len(pg)):
            pg_point.append(pg[i].poker_point.value)
        pg_point_filter = list(set(pg_point))
        pg_point_count = []
        for ppf in pg_point_filter:
            pg_point_count.append(pg_point.count(ppf))
        pg_point_count.sort()
        if pg_point_count == [1, 2, 2]:
            two_paris = True
        return two_paris

    @staticmethod
    def is_one_pairs(poker_group):
        pg = poker_group[:]
        one_pairs = False
        pg_point = []
        for i in range(len(pg)):
            pg_point.append(pg[i].poker_point.value)
        pg_point_filter = list(set(pg_point))
        if len(pg_point_filter) == 4:
            one_pairs = True
        return one_pairs


if __name__ == '__main__':
    pass
