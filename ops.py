class VectorCopyError(Exception):
    pass


def copy(vec1, vec2):
    '''
    copies vec2 into vec1. If the shape of the vectors don't match, vec2 is first transposed to match the shape
    of vec1. This is useful for the case of copying a column vector (list of 1-element lists) into a row vector (list).
    :return:
    '''
    if not vec1 or not vec2:
        return

    if type(vec2[0]) != type(vec1[0]):
        if isinstance(vec2[0], list):
            vec2t = [list(x) for x in zip(*vec2)]
            vec2t = [item for sublist in vec2t for item in sublist]
        else:
            vec2t = [[x] for x in vec2]
        vec2 = vec2t

    if len(vec2) != len(vec1):
        raise VectorCopyError("vectors must have the same size to support copying!!")

    if isinstance(vec2[0], list):
        for i in range(len(vec2)):
            for j in range(len(vec2[0])):
                vec1[i][j] = vec2[i][j]
    elif isinstance(vec2[0], int):
        for i in range(len(vec2)):
            vec1[i] = vec2[i]

    return







