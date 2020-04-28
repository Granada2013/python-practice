from true_false_game.game_cls import Game, GameStatus

print("Welcome to the Yes-No game!")
g = Game('questions.csv', errors=2)
while g.game_status() != GameStatus.GAME_OVER:
    q = g.next_question()
    print(q.text)
    while True:
        ans = input("Type y for 'yes' or n for 'no': ")
        try:
            assert ans in ('y', 'n')
        except AssertionError:
            print('no such option. Try again')
        else:
            print("{}\n".format(f'Wrong! {q.comment}' if not g.isrightanswer(ans) else 'Right!'))
            break
print(g.game_result())
