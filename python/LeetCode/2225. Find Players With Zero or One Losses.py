def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
    # Player: {wins, losses}
    players = {}
    # Matches: [Winner, Loser]
    for match in matches:
        if match[0] not in players:
            players[match[0]] = 0
        if match[1] in players:
            players[match[1]] += 1
        else:
            players[match[1]] = 1
    
    one_or_more = sorted([player for player, losses in players.items() if losses == 0])
    exactly_one = sorted([player for player, losses in players.items() if losses == 1])

    return[one_or_more, exactly_one]