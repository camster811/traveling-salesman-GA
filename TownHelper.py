import random
from collections import namedtuple

Vector2f = namedtuple('Vector2f', ['x', 'y'])

class TownHelper:
    LINETHICKNESS = 4
    PATH_OFFSET_FROM_TOWN = 180
    town_id = 0

    @staticmethod
    def normalize(to_town, from_town):
        dx = to_town.x - from_town.x
        dy = to_town.y - from_town.y
        length = (dx ** 2 + dy ** 2) ** 0.5
        return Vector2f(dx / length, dy / length)

    @staticmethod
    def get_town_id():
        TownHelper.town_id += 1
        return TownHelper.town_id

    TOWN_POSITIONS = [
        Vector2f(3060, 1300),
        Vector2f(1050, 450),
        Vector2f(450, 750),
        Vector2f(690, 1890),
        Vector2f(1410, 1830),
        Vector2f(2070, 1560),
        Vector2f(1725, 1080),
        Vector2f(3360, 810),
        Vector2f(3450, 1770),
        Vector2f(2460, 240),
    ]