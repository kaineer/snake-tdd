# Функция принимает первым параметром - head
#   список из двух чисел вида [x, y]
#   где x - координата по горизонтали
#     а y - координата по вертикали
# вторым параметром - строку 'L', 'R', 'D', 'U'
#
#   L соответствует движению влево
#   R соответствует движению вправо
#   D соответствует движению вниз
#   U соответствует движению вверх
#
# и должна возвращать список вида [x, y],
# в которую должна передвинуться голова змеи
# после движения по указанному направлению
#
def move(head, side):
    if side == 'L':
        head[0] -= 1
    elif side == 'R':
        head[0] += 1
    elif side == 'U':
        head[1] -= 1
    elif side == 'D':
        head[1] += 1
    return(head)