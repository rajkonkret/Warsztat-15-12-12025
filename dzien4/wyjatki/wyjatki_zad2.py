class MyError(Exception):
    def __init__(self, message, err_code):
        super().__init__(message)
        self.err_code = err_code


class MyValueError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=100)


class MyTypeError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=200)
