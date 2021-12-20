class Result:
    def __init__(self, is_successful: bool, status_code: int, result: object = None):
        self.is_successful = is_successful
        self.result = result
        self.status_code = status_code
