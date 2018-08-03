# https://www.reddit.com/r/dailyprogrammer/comments/8jcffg/20180514_challenge_361_easy_tally_program/
def lowerUpper(char):
    if char.isupper():
        return -1
    else:
        return 1
s = 'EbAAdbBEaBaaBBdAccbeebaec'
team = {}
# scoring system and commands
for x in range(len(s)):
    scores = lowerUpper(s[x])
    player = s[x].lower()
    if scores == 1:
        team[player] = team.get(player, 0) + 1
    else:
        team[player] = team.get(player, 0) - 1
for player, value in sorted(team.items(), key=lambda x: x[1], reverse=True):
    print(f'{player} : {value}')