class NegativeAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class FieldIsEmptyError(Exception):
    pass

class UserAlreadyExistsError(Exception):
    pass

class UserDoesNotExistError(Exception):
    pass

class WrongPasswordError(Exception):
    pass