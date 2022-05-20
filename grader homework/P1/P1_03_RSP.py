round = int(input())
running = True
score1 = 0
score2 = 0
count_round = 0
while running:
    throw = input().split()
    if (throw[0] == 'P' and throw[1] == 'R') or (throw[0] == 'R' and throw[1] == 'S') or (throw[0] == 'S' and throw[1] == 'P'):
        score1 += 1
    elif (throw[1] == 'P' and throw[0] == 'R') or (throw[1] == 'R' and throw[0] == 'S') or (throw[1] == 'S' and throw[0] == 'P'):
        score2 += 1
    count_round += 1
    if score1 == round:
        print(score1,score2)
        print('Player 1 wins')
        break
    elif score2 == round:
        print(score1,score2)
        print('Player 2 wins')
        break
    elif round*3 == count_round:
        print(score1,score2)
        print('Tie')
        break