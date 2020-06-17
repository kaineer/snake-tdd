# Определяет, есть ли в указанном направлении
#   часть змейки или нет
#   Возвращает True, если такой элемент найден
#   Возвращает False в противном случае
#
def can_move(trail, side):
    return True

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
