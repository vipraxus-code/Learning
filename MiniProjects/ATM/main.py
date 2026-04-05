from pathlib import Path
from exceptions import ATMError
import sqlite3
import re


class ATM:
    def __init__(self, atm_id):
        self.id = atm_id
        self.users_db = Path(__file__).with_name("users.db")
        self.log = Path(__file__).with_name("operations.log")
        self.current_user = None
        self.previous_user = None
        self.atm_balance = 0
        self.FORBIDDEN_LOGINS = frozenset({"none", "null", "false", "true"})
    
    def withdraw(self, amount):
        status = "ERROR"
        error_msg = None
        try:
            if type(amount) is not int:
                raise TypeError
            if amount <= 0:
                raise ATMError("NegativeAmountError", "Number must be positive.", f"Amount given by user is {amount} which is less than 0.",)
            if amount > self.balance:
                raise ATMError("InsufficientFundsError", "Insufficient funds.", "Insufficient funds on user balance.",)
            self.balance -= amount
        except (TypeError, NegativeAmountError, InsufficientFundsError, Exception) as e:
            error_msg = type(e).__name__
            return self._handle_error(e)
        else:
            status = "SUCCESS"
            return f"Withdrew {amount}, current balance: {self.balance}."
        finally:
            self._append_log(status=status, operation="Withdraw", value=amount, error_msg=error_msg)

    def deposit(self, amount):
        status = "ERROR"
        error_msg = None
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
            self._append_log(status=status, operation="Deposit", value=amount, error_msg=error_msg)

    def show_balance(self):
        status = "ERROR"
        error_msg = None
        try:
            if self.current_user is None:
                raise ATMError("SessionRequired", "You must be logged in to do that.", "Attempted to use a protected feature without an active session.")
            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                user_balance = cur.execute(
                    "SELECT balance FROM users WHERE login = ?",
                    (self.current_user,)
                ).fetchone()
            if user_balance is None:
                raise ATMError("BalanceNotFoundError", "Balance not found", f"The balance for the login {self.current_user} was not found.")
        except ATMError as e:
            error_msg = repr(e)
            return str(e)
        except Exception as e:
            error_msg = repr(e)
            return "Unknown error occurred."
        else:
            status = "SUCCESS"
            return f"Your balance is {user_balance[0]}."
        finally:
            self._append_log(status=status, operation="ShowBalance", user=self.current_user, value=user_balance[0] if status == "SUCCESS" else None, error_msg=error_msg)

    def login(self):
        status = "ERROR"
        error_msg = None
        try:
            inputed_login = input("Hello, please enter your login and password to continue.\nLogin: ")
            inputed_login = inputed_login.strip()
            if not inputed_login:
                raise ATMError("FieldIsEmptyError", "Please fill in the field.", "Input field was left empty.")
            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                cur.execute(
                    "SELECT 1 FROM users WHERE login = ?",
                    (inputed_login,)
                )
                if cur.fetchone() is None:
                    raise ATMError("UserDoesNotExistError", "User with such login does not exist.", f"Login {inputed_login} given by user does not exist.",)
            inputed_password = input("Password: ")
            inputed_password = inputed_password.strip()
            if not inputed_password:
                raise ATMError("FieldIsEmptyError", "Please fill in the field.", "Input field was left empty.")
            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                actual_password = cur.execute(
                    "SELECT password FROM users WHERE login = ?",
                    (inputed_login,)
                ).fetchone()
                if actual_password is None:
                    raise ATMError("PasswordNotFoundError", "Password not found", f"The password for the login {inputed_login} was not found.")
                if inputed_password != actual_password[0]:
                    raise ATMError("WrongPasswordError", "Wrong password.", "User inputed wrong password.")
        except ATMError as e:
            error_msg = repr(e)
            return str(e)
        except Exception as e:
            error_msg = repr(e)
            return "Unknown error occurred."
        else:
            if self.current_user is not None:
                self.logout()
            self.current_user = inputed_login
            status = "SUCCESS"
            return f"You're now using ATM as {inputed_login}."
        finally:
            self._append_log(status=status, operation="Login", user=self.current_user if status == "SUCCESS" else inputed_login, error_msg=error_msg)

    def register(self):
        status = "ERROR"
        error_msg = None
        try:
            inputed_login = input("Hello, thanks for choosing us! To continue enter following information.\nLogin(May contain only Latin letters and digits): ")
            if not inputed_login.strip():
                raise ATMError("FieldIsEmptyError", "Please fill in the field.", "Input field was left empty.")
            if len(inputed_login) < 6 or len(inputed_login) > 24:
                raise ATMError("InvalidLoginError", "Login length must be 5-16 characters.", f"Length of login {inputed_login} given by user is invalid.")
            if not re.fullmatch(r"[A-Za-z0-9]+", inputed_login):
                raise ATMError("InvalidLoginError", "Login may contain only Latin letters and digits.", f"Contants of login {inputed_login} given by user is invalid.")
            if inputed_login.lower() in self.FORBIDDEN_LOGINS:
                raise ATMError("InvalidLoginError", "The login is in forbidden list.", f"Login {inputed_login} given by user is in forbidden logins.")
            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                cur.execute(
                    "SELECT 1 FROM users WHERE login = ?",
                    (inputed_login,)
                )
                if cur.fetchone() is not None:
                    raise ATMError("UserAlreadyExistsError", "User with this login already exists.", f"Login {inputed_login} given by user already exists.",)
            inputed_password = input("Password(May contain only Latin letters and numbers): ")
            if not inputed_password.strip():
                raise ATMError("FieldIsEmptyError", "Please fill in the field.", "Input field was left empty.")


            # Validate login: length 12-24, characters A-Za-z0-9, check against forbidden list.


            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO users (login, password, balance) VALUES (?, ?, ?)",
                    (inputed_login, inputed_password, 0)
                )
        except ATMError as e:
            error_msg = repr(e)
            return str(e)
        except Exception as e:
            error_msg = repr(e)
            return "Unknown error occurred."
        else:
            if self.current_user is not None:
                self.logout()
            self.current_user = inputed_login
            status = "SUCCESS"
            return f"You're now using ATM as {inputed_login}."
        finally:
            self._append_log(status=status, operation="Registration", user=self.current_user if status == "SUCCESS" else inputed_login, error_msg=error_msg)

    def logout(self):
        status = "ERROR"
        error_msg = None
        try:
            if self.current_user is None:
                raise ATMError("SessionRequired", "No user is logged in.", "Attempted to logout while no active session.")
        except ATMError as e:
            error_msg = repr(e)
            return str(e)
        else:
            self.previous_user = self.current_user
            self.current_user = None
            status = "SUCCESS"
            return "Thanks for using our ATM, goodbye!"
        finally:
            self._append_log(status=status, operation="Logout", user=self.previous_user if status == "SUCCESS" else None, error_msg=error_msg)

    def _append_log(self, status, operation, user=None, value=None, error_msg=None):
        line = f"{status} - {self.id} - {operation}"
        if user:
            line += f" - {user}"
        if value is not None:
            line += f" - {value}"
        if error_msg:
            line += f" - {error_msg}"
        with self.log.open("a", encoding="utf-8") as f:
            f.write(line + "\n")




atm01 = ATM("atm_1")
print(atm01.login())
print(atm01.register())