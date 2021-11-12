SUITS = ['heart', 'deamonds', 'club', 'spade']
tmp = [str(x) for x in range(2, 11)] + ['jack', 'queen', 'king', 'ace']
POINTS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 11]
RANKS = {}
for i in range(len(tmp)):
    RANKS[tmp[i]] = POINTS[i]