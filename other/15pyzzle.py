import random

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    field = list(range(1, 17))
    field[-1] = EMPTY_MARK
    random.shuffle(field)

    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for i in range(0, 16, 4):
        print(field[i:i+4])
    print('\n')


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    ideal = list(range(1, 17))
    ideal[-1] = EMPTY_MARK
    return field == ideal


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    empty_index = field.index(EMPTY_MARK)
    delta = MOVES[key]

    message = 'wrong move'

    if key == 'w' and empty_index + delta < 0:
        raise IndexError(message)
    if key == 'a' and empty_index % 4 == 0:
        raise IndexError(message)
    if key == 'd' and empty_index % 4 == 3:
        raise IndexError(message)
    if key == 's' and empty_index + delta > 15:
        raise IndexError(message)

    to_change = empty_index + delta
    field[empty_index], field[to_change] = field[to_change], field[empty_index]
    return field


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right
    :return: <str> current move.
    """
    while True:
        move = input('Input your move:')
        if move not in MOVES.keys():
            print('Wrong move!')
        else:
            return move


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    field = shuffle_field()
    # field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, EMPTY_MARK, 15]

    steps = 0
    while not is_game_finished(field):
        try:
            print_field(field)
            move = handle_user_input()
            field = perform_move(field, move)
            steps += 1
        except IndexError as ex:
            print(ex)
        except KeyboardInterrupt:
            print('Shutting dowwn.')
            quit()
    print('You have completed the game in {} steps.'.format(steps))


if __name__ == '__main__':
    main()