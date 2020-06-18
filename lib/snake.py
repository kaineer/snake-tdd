# Определяет, есть ли в указанном направлении
#   часть змейки или нет
#   Возвращает False, если такой элемент найден
#   Возвращает True в противном случае
#
def can_move(trail, side):
    t2 = grow(trail, side)
    for i in trail:
        if t2[0] == trail[i]:
            return False
            
    else:
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
