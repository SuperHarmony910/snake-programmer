print('What is 4 x 3?')
score = 0
firstInput = input()
q1ans = 4*3
if firstInput == str(q1ans):
    score = score + 1
    print('Correct! Your score so far is ' + str(score) +' out of 2.')
else:
    print('Incorrect! The correct answer was ' + str(q1ans) + '! Your answer was ' + firstInput + '!')

print('What is 6 x 3?')
secondInput = input()
q2ans = 6*3
if secondInput == str(q2ans):
    score = score + 1
    print('Correct! Your score so far is ' + str(score) +' out of 2.')
else:
    print('Incorrect! The correct answer was ' + str(q2ans) + '! Your answer was ' + secondInput + '!')