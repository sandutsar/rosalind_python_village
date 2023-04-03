SIGNS = ('<', '>', '<=', '>=', '=')


class InvalidSignError(Exception):
    def __init__(self, sign, message=None):
        if message is None:
            message = f'Your sign = {sign} must be one of {SIGNS}!'
        super().__init__(message)


class NumberValueError(Exception):
    def __init__(self, num, sign, value, message=None):
        if sign not in SIGNS:
            raise InvalidSignError(sign)
        if message is None:
            variable = [name for name, i in locals().items() if i == num][0]
            message = f'Error: {variable} = {num}  must be {sign} {value}!'
        super().__init__(message)


class IterableLengthError(Exception):
    def __init__(self, iterable, sign, value, message=None):
        if sign not in SIGNS:
            raise InvalidSignError(sign)
        if message is None:
            variable = [name for name, i in locals().items() if i == iterable][0]
            message = f'Error: len({variable}) = {len(iterable)} must be {sign} {value}!'
        super().__init__(message)
