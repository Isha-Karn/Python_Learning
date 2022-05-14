def game():
    return 85
score= game()

with open('highscore.txt') as f:
    highscoreSTR= f.read()

if highscoreSTR=='':
      with open('highscore.txt', 'w') as f:
       f.write(str(score))

elif int(highscoreSTR)<score:
    with open('highscore.txt', 'w') as f:
      f.write(str(score))
