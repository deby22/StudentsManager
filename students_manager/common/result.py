class Result:
    def __init__(self, is_successful: bool, errors: dict = None, result: object = None):
        self.is_successful = is_successful
        self.errors = errors
        self.result = result
