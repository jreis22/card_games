from core.card_games.bisca import Bisca
from core.cards.card import PlayingCard
from core.cards.card_enums import Rank, Suit
from core.player import CardPlayer
from core.game_state import GameStateEnum
from core.card_game import CardGame
from core.cards.card_hand import CardHand


def str_to_int(val):
    try:
        number = int(val)
        return number
    except ValueError:
        return None


def read_int(min, max) -> int:
    number = None
    while number is None:
        val = input("Choose a card by index\n")
        number = str_to_int(val)
        if not number is None:
            if number > max or number < min:
                print("index chosen is out of range")
                number = None
        else:
            print("input is invalid")

    print("excellent choice")
    return number


def print_player_cards(player):
    count = 0
    for card in game.players[player].show_hand():
        count += 1
        print(f"{count}: {card}")

def player_phase(player):
    valid_play = False
    while not valid_play:
        try:
            print_player_cards(player)
            val = read_int(1, game.players[player].number_of_cards_left()) - 1
            card = game.players[player].show_hand()[val]
            game.play_card(player, card)
        except Exception as e:
            print(str(e))
        else:
            print('valid play')
            valid_play = True


player1 = CardPlayer()
player2 = CardPlayer()
players_dict = {1: player1,
                2: player2}
player_order = [1, 2]

game = Bisca(players=players_dict,
             player_order=player_order)
# print(game.players[1].number_of_cards_left())
game.start_game()
# print(game.players[1].number_of_cards_left())
# print(game.players[2].number_of_cards_left())
# print(game.card_deck.list_size())

while not game.is_game_over():
    print(f"player {game.player_order[0]} : pick a card")
    # for i in range(0, game.players[1].number_of_cards_left()):
    #    print(f"{i}: {game.players[1].show_hand()[i]} : {game.players[2].show_hand()[i]}")
    player_phase(game.player_order[0])
    # print(f"picked: {card}")
    # print(f"player is_playing: {game.players[1].is_playing()}")
    # print(f"played cards {game.played_cards[0][0]} {game.played_cards[0][1]}")
    # game.game_state = GameStateEnum.GAME_END
    print(f"player1 points: {game.players[1].points}  player2 points: {game.players[2].points}")