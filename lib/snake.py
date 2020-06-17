# Самая простая функция
#   принимает первым параметром элементы змейки
#   принимает вторым парамтером текущую длину змейки
#
# Если количество элементов змейки больше указанной,
#   возвращает только первые size элементов
#   в противном случае возвращает весь trail целиком
#
def limit(trail, size):
    return(trail[:size])


def grow(trail, side):
    new = move(trail[0],side)
    trail.insert(0, new)
    return(trail)


def move(head, side):
    [x, y] = head
    if side == 'L':
        x -= 1
    elif side == 'R':
        x += 1
    elif side == 'U':
        y -= 1
    elif side == 'D':
        y += 1
    return([x, y])

 