class VectorCopyError(Exception):
    pass


def check_vector_sizes(func):
    '''
    a decorator that ensures all argument vectors are the same size, to support operations like vector addition
    :param func:
    :return:
    '''
    def check_size_wrapper(*args):
        prev = None
        for arg in args:
            if prev and len(arg) != len(prev):
                raise VectorCopyError("Vectors aren't equal size, can't perform operation")
            else:
                prev = arg
        return func(*args)

    return check_size_wrapper


def transpose(vector):
    '''
    transposes a vector and returns the resultant vector
    :param vector:
    :return:
    '''
    if not vector:
        return
    if isinstance(vector[0], list):
        return [list(x) for x in zip(*vector)]
    else:
        return [[x] for x in vector]


@check_vector_sizes
def add(vector1, vector2, mutate=False):
    '''
    adds two vectors together by modifying vector1 such that vector1[i] = vector2[i] + vector1[i]
    :param vector1:
    :param vector2:
    :return:
    '''
    return sum(vector2) + sum(vector1)


def copy(vector1, vector2):
    '''
    copies vector2 into vector1. If the shape of the vectors don't match, vec2 is first transposed to match the shape
    of vec1. This is useful for the case of copying a column vector (list of 1-element lists) into a row vector (list).
    :return:
    '''
    if not vector1 or not vector2:
        return

    if type(vector2[0]) != type(vector1[0]):
        if isinstance(vector2[0], list):
            vec2t = [list(x) for x in zip(*vector2)]
            vec2t = [item for sublist in vec2t for item in sublist]
        else:
            vec2t = [[x] for x in vector2]
        vector2 = vec2t

    if len(vector2) != len(vector1):
        raise VectorCopyError("vectors must have the same size to support copying!!")

    if isinstance(vector2[0], list):
        for i in range(len(vector2)):
            for j in range(len(vector2[0])):
                vector1[i][j] = vector2[i][j]
    elif isinstance(vector2[0], int):
        for i in range(len(vector2)):
            vector1[i] = vector2[i]

    return


def scale(vector, scalar):
    '''
    scales a vector by the given scalar value. row-based (list) and column-based (list of lists) vectors are accepted.
    :param vector:
    :param scalar:
    :return:
    '''
    if not vector:
        return
    if not vector[0]:
        return
    if isinstance(vector[0], int):
        for i in range(len(vector)):
            vector[i] = vector[i]*scalar
    else:
        for i in range(len(vector)):
            vector[i][0] = vector[i][0]*scalar
    return


def axpy(scalar, vec1, vec2):
    '''
    performs the axpy operation: scalar*vec1 + vec2 for the given scalar and vectors. returns a new vector with the result
    of the axpy operation.
    :param scalar:
    :param vec1:
    :param vec2:
    :return:
    '''
    scale(vec1, scalar)
    return add(vec1, vec2)




