# Начнем с простейшей игры - крестики-нолики :)
# Реализуйте определение исхода игры на доске.
# Доска представлена кортежем.
# Крестик - 1, нолик - 0, пустые клетки обозначены None.
# Для визуализации я определил переменные с удобными именами.
# None я здесь именую _ (подчеркивание - валидное имя в Python).

X, O, _ = 1, 0, None
TEST_BOARD = (
    O, X, O,
    X, X, X,
    _, _, X
)

# Возможны четыре исхода, для них я тоже определил именованные константы.
O_WINS, X_WINS, UNDEFINED, DRAW = range(4)

# Первая подзадача и подсказка - реализуйте функцию,
# которая возвращает все возможные комбинации по 3 клетки в ряд:
# горизонтали, вертикали, диагонали. Таким образом эта часть
# задачи сводится к упражнению на слайсинг последовательности.
# Можете также попробовать реализовать как генератор.


def slice3(board):
    a = []
    t = 0
    k = 3
    n = 0
    while t <= 7:
        x = board[t:k:1]
        a.append(x)
        t += 3
        k += 3
    while n <= 2:
        x = board[n::3]
        n += 1
        a.append(x)
    hor = board[::4]
    diag = board[2:7:2]
    a.append(hor)
    a.append(diag)
    return a


def outcome(board):
    result = next((i for i in list(slice3(board)) if i == (1, 1, 1) or i == (0, 0, 0)), None)
    if result == (1, 1, 1):
        return print(X_WINS)
    elif result == (0, 0, 0):
        return print(O_WINS)

    result2 = next((i for i in list(slice3(board)) if i is not None and i != (1, 1, 1) and i != (0, 0, 0)), None)
    if result2 is not None or result2 != (1, 1, 1) or result2 != (0, 0, 0):
        return print(DRAW)

    for i in list(slice3(board)):
        if i[0] is None or i[1] is None or i[2] is None:
            return print(UNDEFINED)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
