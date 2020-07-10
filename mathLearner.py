print('What is 4 x 3?')
score = 0
firstInput = input()
q1ans = 4*3
if firstInput == str(q1ans):
    score = score + 1
    print('Correct! Your score is ' + str(score) +' out of 3.')
else:
    print('Incorrect! The correct answer was ' + str(q1ans) + '! Your answer was ' + firstInput + '!')

print('What is 6 x 3?')
secondInput = input()
q2ans = 6*3
if secondInput == str(q2ans):
    score = score + 1
    print('Correct! Your score is ' + str(score) +' out of 3.')
else:
    print('Incorrect! The correct answer was ' + str(q2ans) + '! Your answer was ' + secondInput + '!')

print('If y = 4, what is 9y?')
thirdInput = input()
y = 4
q3ans = 9*y
if thirdInput == str(q3ans):
    score = score + 1
    print('Correct! Your total score is ' + str(score) +' out of 3.')
else:
    print('Incorrect! The correct answer was ' + str(q3ans) + '! Your answer was ' + thirdInput + '!')
    print("Your total score is " + str(score) + " out of 3!")