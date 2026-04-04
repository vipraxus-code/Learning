from pathlib import Path
from exceptions import FieldIsEmptyError, NegativeAmountError, InsufficientFundsError, UserAlreadyExistsError, UserDoesNotExistError, WrongPasswordError
import sqlite3


class ATM:
    def __init__(self, atm_id):
        self.id = atm_id
        self.users_db = Path(__file__).with_name("users.db")
        self.log = Path(__file__).with_name("operations.log")
        self.current_user = None
        self.atm_balance = 0
    
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
        except (TypeError, NegativeAmountError, InsufficientFundsError, Exception) as e:
            error_msg = type(e).__name__
            return self._handle_error(e)
        else:
            status = "SUCCESS"
            return f"Withdrew {amount}, current balance: {self.balance}."
        finally:
            self._append_log(status, "Withdraw", amount, error_msg=error_msg)

    def deposit(self, amount):
        status = "ERROR"
        error_msg = ""
        try:
            if type(amount) is not int:
                raise TypeError
            if amount <= 0:
                raise NegativeAmountError
            self.balance += amount
        except (TypeError, NegativeAmountError, Exception) as e:
            error_msg = type(e).__name__
            return self._handle_error(e)
        else:
            status = "SUCCESS"
            return f"Deposited {amount}, current balance: {self.balance}"
        finally:
            self._append_log(status, "Deposit", amount, error_msg=error_msg)

    def show_balance(self):
        self._append_log("SUCCESS", "PrintBalance")
        return f"Balance: {self.balance}."

    def login(self):
        status = "ERROR"
        error_msg = ""
        try:
            inputed_login = input("Hello, please enter your login and password to continue.\nLogin: ")
            inputed_login = inputed_login.strip()
            if not inputed_login:
                raise FieldIsEmptyError
            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                cur.execute(
                    "SELECT 1 FROM users WHERE login = ?",
                    (inputed_login,)
                )
                if cur.fetchone() is None:
                    raise UserDoesNotExistError
            inputed_password = input("Password: ")
            inputed_password = inputed_password.strip()
            if not inputed_password:
                raise FieldIsEmptyError
            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                actual_password = cur.execute(
                    "SELECT password FROM users WHERE login = ?",
                    (inputed_login,)
                ).fetchone()
                if actual_password is None:
                    raise UserDoesNotExistError
                if inputed_password != actual_password[0]:
                    raise WrongPasswordError
        except (FieldIsEmptyError, UserDoesNotExistError, WrongPasswordError, Exception) as e:
            error_msg = type(e).__name__
            return self._handle_error(e)
        else:
            self.current_user = inputed_login
            status = "SUCCESS"
            return f"Success! You're using ATM as {inputed_login}."
        finally:
            self._append_log(status, "Login", error_msg=error_msg)

    def register(self):
        status = "ERROR"
        error_msg = ""
        try:
            inputed_login = input("Hello, thanks for choosing us! To continue enter following information.\nLogin: ")
            inputed_login = inputed_login.strip()
            if not inputed_login:
                raise FieldIsEmptyError
            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                cur.execute(
                    "SELECT 1 FROM users WHERE login = ?",
                    (inputed_login,)
                )
                if cur.fetchone() is not None:
                    raise UserAlreadyExistsError
            inputed_password = input("Password: ")
            inputed_password = inputed_password.strip()
            if not inputed_password:
                raise FieldIsEmptyError
            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO users (login, password, balance) VALUES (?, ?, ?)",
                    (inputed_login, inputed_password, 0)
                )
        except (FieldIsEmptyError, UserAlreadyExistsError, Exception) as e:
            error_msg = type(e).__name__
            return self._handle_error(e)
        else:
            self.current_user = inputed_login
            status = "SUCCESS"
            return f"Success! You're using ATM as {inputed_login}."
        finally:
            self._append_log(status, "Registration", error_msg=error_msg)

    def logout(self):
        self.current_user = None
        self._append_log("SUCCESS", "Logout")
        return "Thanks for using our ATM, goodbye!"

    def _append_log(self, status, operation, amount="", error_msg=""):
        line = f"{status} - {self.id} - {operation}"
        if self.current_user:
            line += f" - {self.current_user}"
        if amount:
            line += f" - {amount}"
        if error_msg:
            line += f" - {error_msg}"
        with self.log.open("a", encoding="utf-8") as f:
            f.write(line + "\n")

    def _handle_error(self, error):
        if isinstance(error, TypeError):
            return "You must enter an integer."
        elif isinstance(error, NegativeAmountError):
            return "Number must be positive."
        elif isinstance(error, InsufficientFundsError):
            return "Insufficient funds."
        elif isinstance(error, UserAlreadyExistsError):
            return "User with this login already exists."
        elif isinstance(error, UserDoesNotExistError):
            return "User with this login does not exist."
        elif isinstance(error, FieldIsEmptyError):
            return "Please fill in the field."
        elif isinstance(error, WrongPasswordError):
            return "Wrong password."
        return "Unknown error."





atm01 = ATM("01")
print(atm01.login())