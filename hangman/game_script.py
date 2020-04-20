from hangman.game_cls import Game, GameStatus

game = Game(errors=5)
print("Welcome to hangman! The word was generated.\nUse cyrillic letters only.")

while game.status() == GameStatus.IN_PROGRESS:
    print(f"\n\"{game.get_state()}\"\nErrors left: {'|' * game.errors_left}")
    if game.letters_tried:
        print(f"You've tried: {game.letters_tried}")
    while True:
        letter = input('What letter you want to try? ').lower()
        try:
            list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя').index(letter)
        except ValueError:
            print("It's not a cyrillic letter.")
        else:
            if game.isduplicate(letter):
                print("You've tried it. Try another one")
            else:
                break
    game.try_letter(letter=letter)

if game.status() == GameStatus.IS_LOST:
    print(f'\nYou lost!\nThe word is "{game.show_word()}"')
elif game.status() == GameStatus.IS_WON:
    print(f'\nYou won! The word is "{game.show_word()}"')
