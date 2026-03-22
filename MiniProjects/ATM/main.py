from pathlib import Path
from exceptions import NegativeAmountError, InsufficientFundsError


class ATM:
    def __init__(self, atm_id):
        self.id: str = atm_id
        self.log: Path = Path(__file__).with_name("operations.log")
        self.balance: int = 0
    
    def withdraw(self, amount):
        status = "ERROR"
        error_msg = ""
        try:
            if type(amount) is not int:
                raise TypeError
            if amount <= 0:
                raise NegativeAmountError
            if amount > self.balance:
                raise InsufficientFundsError
            self.balance -= amount
        except (TypeError, NegativeAmountError, InsufficientFundsError) as e:
            error_msg = type(e).__name__
            return self._handle_error(e)
        else:
            status = "SUCCESS"
            return f"Withdrew {amount}, current balance: {self.balance}."
        finally:
            self._append_log(status, "Withdraw", amount, error_msg)

    def deposit(self, amount):
        status = "ERROR"
        error_msg = ""
        try:
            if type(amount) is not int:
                raise TypeError
            if amount <= 0:
                raise NegativeAmountError
            self.balance += amount
        except (TypeError, NegativeAmountError) as e:
            error_msg = type(e).__name__
            return self._handle_error(e)
        else:
            status = "SUCCESS"
            return f"Deposited {amount}, current balance: {self.balance}"
        finally:
            self._append_log(status, "Deposit", amount, error_msg)

    def show_balance(self):
        self._append_log("SUCCESS", "PrintBalance")
        return f"Balance: {self.balance}."

    def exit(self):
        self._append_log("SUCCESS", "Exit")
        return "Thanks for using our ATM, goodbye!"

    def _append_log(self, status, operation, amount="", error_msg=""):
        line = f"{status} - {self.id} - {operation}"
        if amount:
            line += f" - {amount}"
        if error_msg:
            line += f" - {error_msg}"
        with self.log.open("a", encoding="utf-8") as f:
            f.write(line + "\n")

    def _handle_error(self, error):
        if isinstance(error, TypeError):
            return "You must enter an integer."
        if isinstance(error, NegativeAmountError):
            return "Number must be positive."
        if isinstance(error, InsufficientFundsError):
            return "Insufficient funds."