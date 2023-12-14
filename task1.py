class ChessKnight:
    def __init__(self, horizontal: str, vertical: int, color: str) -> None:
        """
        Создает экземпляр класса ChessKnight с указанными координатами и цветом.

        :param horizontal: координата коня по горизонтальной оси
        :param vertical: координата коля по вертикальной оси
        :param color: цвет коня

        Пример использования:
        >>> knight = ChessKnight('d', 4, 'white')
        >>> knight.horizontal, knight.vertical, knight.color
        ('d', 4, 'white')
        """
        self.vertical = None
        self.horizontal = None
        self.color = None
        self.horizontal_init(horizontal)
        self.vertical_init(vertical)
        self.color_init(color)

    @staticmethod
    def check_horizontal_arg(horizontal: str) -> bool:
        """
        Проверяет валидность буквенной координаты.

        :param horizontal: координата коня по горизонтальной оси
        :return: Является ли координата корректной

        :raise ValueError: Если координата не лежит в отрезке [a;h], вызываем ошибку
        :raise TypeError: Если координата не строка, вызываем ошибку

        Пример использования:
        >>> ChessKnight.check_horizontal_arg('a')
        True
        >>> ChessKnight.check_horizontal_arg('i')
        Traceback (most recent call last):
        ...
        ValueError
        """
        if not isinstance(horizontal, str):
            raise TypeError
        elif not 'a' <= horizontal <= 'h':
            raise ValueError
        return True

    @staticmethod
    def check_vertical_arg(vertical: int) -> bool:
        """
        Проверяет валидность числовой координаты.

        :param vertical: координата коля по вертикальной оси
        :return: Является ли координата корректной
        :raise ValueError: Если координата не лежит в отрезке [1;8], вызываем ошибку
        :raise TypeError: Если координата не число, вызываем ошибку


        Пример использования:
        >>> ChessKnight.check_vertical_arg(4)
        True
        >>> ChessKnight.check_vertical_arg(9)
        Traceback (most recent call last):
        ...
        ValueError
        """
        if not isinstance(vertical, int):
            raise TypeError
        elif not 1 <= vertical <= 8:
            raise ValueError
        return True

    def horizontal_init(self, horizontal: str) -> None:
        """
        Устанавливает горизонтальную координату.

        :param horizontal: координата коня по горизонтальной оси


        Пример использования:
        >>> knight = ChessKnight('d', 4, 'white')
        >>> knight.horizontal_init('e')
        >>> knight.horizontal
        'e'
        """
        if self.check_horizontal_arg(horizontal):
            self.horizontal = horizontal

    def vertical_init(self, vertical: int) -> None:
        """
        Устанавливает вертикальную координату.
        :param vertical: координата коля по вертикальной оси

        Пример использования:
        >>> knight = ChessKnight('d', 4, 'white')
        >>> knight.vertical_init(6)
        >>> knight.vertical
        6
        """
        if self.check_vertical_arg(vertical):
            self.vertical = vertical

    def color_init(self, color: str) -> None:
        """
        Устанавливает цвет фигуры.

        :param color: цвет коня
        :raise ValueError: Если цвет не лежит в списке [white, black], вызываем ошибку

        Пример использования:
        >>> knight = ChessKnight('d', 4, 'white')
        >>> knight.color_init('black')
        Traceback (most recent call last):
        ...
        ValueError
        """
        if color not in ['white', 'black']:
            raise ValueError
        self.color = color

    def move_to(self, x: str, y: int) -> None:
        """
        Метод, заменяющий текущие координаты коня на переданные. Если конь не может перейти на новую координату,
        оставить атрибуты без изменения

        :param x: координата коня по горизонтальной оси
        :param y: координата коля по вертикальной оси


        Пример использования:
        >>> knight = ChessKnight('d', 4)
        >>> knight.move_to('e', 6)
        >>> knight.horizontal, knight.vertical
        ('e', 6)
        """
        ...

    def draw_board(self) -> None:
        """
        Метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки, на которые может переместиться конь.
        Пример использования:
        >>> knight = ChessKnight('c', 3, 'white')
        >>> knight.draw_board()
        ........
        ........
        ........
        .*.*....
        *...*...
        ..N.....
        *...*...
        .*.*....
        """
        ...


class House:
    @staticmethod
    def check_color_arg(color: str) -> bool:
        """
        Проверка валидности строкового аргумента color
        :param color: цвет дома
        :return: Является ли цвет дома строкой

        :raise TypeError: Если цвет не строка, вызываем ошибку
        >>> House.check_color_arg("желтый")
        True
        >>> House.check_color_arg(123)
        Traceback (most recent call last):
        ...
        TypeError
        """
        if not isinstance(color, str):
            raise TypeError
        return True

    @staticmethod
    def check_rooms_arg(rooms: int) -> bool:
        """
        Проверка валидности целочисленного аргумента rooms

        :param rooms: число комнат
        :return: Является ли число комнат положительным числом

        :raise TypeError: Если rooms не число, вызываем ошибку
        :raise ValueError: Если rooms <= 0, вызываем ошибку

        >>> House.check_rooms_arg(3)
        True
        >>> House.check_rooms_arg('пять')
        Traceback (most recent call last):
        ...
        TypeError
        >>> House.check_rooms_arg(0)
        Traceback (most recent call last):
        ...
        ValueError
        """
        if not isinstance(rooms, int):
            raise TypeError
        elif rooms <= 0:
            raise ValueError
        return True

    def __init__(self, color: str, rooms: int) -> None:

        """
        Создает экземпляр класса House с указанным цветом и количеством комнат.

        :param color: цвет дома
        :param rooms: количество комнат

        Пример использования:
        >>> house = House('white', 4)
        >>> house.color, house.rooms
        ('white', 4)
        """
        self.color = None
        self.rooms = None
        self.color_init(color)
        self.rooms_init(rooms)

    def rooms_init(self, rooms: int) -> None:
        """
        Метод, инициализирующий количество комнат rooms

        :param rooms: количество комнат

        >>> h = House()
        >>> h.rooms_init(3)
        True
        >>> h.rooms
        3
        """
        if self.check_rooms_arg(rooms):
            self.rooms = rooms

    def color_init(self, color: str) -> None:
        """
        Метод, устанавливающий цвет дома таким, каким он указан в строковом аргументе color
        :param color: цвет дома

        >>> h = House()
        >>> h.color_init("синий")
        True
        >>> h.color
        'синий'
        """
        if self.check_color_arg(color):
            self.color = color

    def paint(self, new_color: str) -> None:
        """
        Метод, меняющий цвет дома на new_color
        :param new_color: новый цвет

        >>> h = House()
        >>> h.color_init("синий")
        True
        >>> h.paint("красный")
        >>> h.color
        'красный'
        """
        ...

    def add_rooms(self, n: int) -> None:
        """
        Метод, увеличивающий количество комнат на число n
        :param n: количество комнат

        >>> h = House()
        >>> h.rooms_init(3)
        True
        >>> h.add_rooms(2)
        >>> h.rooms
        5
        """
        ...


class User:
    def name_init(self, name: str) -> None:
        """
        Проверка валидности строкового аргумента name

        :param name: имя пользователя
        :raise TypeError: Если имя не строка, вызываем ошибку


        >>> u = User()
        >>> u.name_init("Alice")
        >>> u.name
        'Alice'
        >>> u.name_init(123)
        Traceback (most recent call last):
        ...
        TypeError
        """
        if not isinstance(name, str):
            raise TypeError
        self.name = name

    def __init__(self, name: str) -> None:
        """
        Инициализация пользователя

        :param name: имя пользователя

        >>> u = User('Bob')
        >>> u.name
        'Bob'
        >>> u.friends
        0
        """
        self.name = None
        self.name_init(name)
        self.friends = 0

    def add_friends(self, n: int) -> None:
        """
        Добавление друзей
        :param n: количество друзей
        >>> u = User('Alice')
        >>> u.add_friends(5)
        >>> u.friends
        5
        """
        ...

    def delete_friend(self) -> None:
        """
        Удаление друга. Если у пользователя нет друзей, ничего не делать.

        >>> u = User('Alice')
        >>> u.add_friends(5)
        >>> u.delete_friend()
        >>> u.friends
        4
        """
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()
