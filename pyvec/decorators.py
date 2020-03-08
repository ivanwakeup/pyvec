from pyvec.ops import VectorCopyError


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
