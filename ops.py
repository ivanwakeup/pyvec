class VectorCopyError(Exception):
    pass


def copy(vec1, vec2):
    '''
    copies vec2 into vec1. If the shape of the vectors don't match, vec2 is first transposed to match the shape
    of vec1. This is useful for the case of copying a column vector (list of 1-element lists) into a row vector (list).
    :return:
    '''
    if not vec1 or not vec2:
        return 0

    if type(vec2[0]) != type(vec1[0]):
        vec2t = [list(x) for x in zip(*vec2)]
        vec2 = vec2t

    if len(vec2) != len(vec1):
        raise VectorCopyError

    for i in range(len(vec2)):
        for j in range(len(vec2[0])):
            vec1[i][j] = vec2[i][j]

    return 0


vec1 = [1,2,3]
vec2 = [[2],[3], [1]]

copy(vec1, vec2)
print(vec1)







