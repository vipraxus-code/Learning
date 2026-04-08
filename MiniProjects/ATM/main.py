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
        self.FORBIDDEN_LOGINS = frozenset({"none", "null", "false", "true"})
    
    def withdraw(self):
        status = "ERROR"
        error_msg = None
        try:
            if self.current_user is None:
                raise ATMError("SessionRequired", "You must be logged in to do that.", "Attempted to use a protected feature without an active session.")
            input_amount = input("Enter the amount to withdraw: ")
            if not input_amount.strip():
                raise ATMError("FieldIsEmptyError", "Please fill in the field.", "Input field was left empty.")
            amount = int(input_amount)
            if amount <= 0:
                raise ATMError("InvalidAmountError", "Amount must be greater than zero.", f"User entered invalid withdraw amount: {input_amount}.")
            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                user_balance = cur.execute(
                    "SELECT balance FROM users WHERE login = ?",
                    (self.current_user,)
                ).fetchone()[0]
            if amount > user_balance:
                raise ATMError("InsufficientFundsError", "Insufficient funds for this operation.", f"Withdraw denied: requested {input_amount}, available {user_balance}.")
        except ATMError as e:
            error_msg = repr(e)
            return str(e)
        except ValueError as e:
            error_msg = repr(e)
            return "Invalid input. Please enter numbers only."
        except Exception as e:
            error_msg = repr(e)
            return "Unknown error occurred."
        else:
            new_balance = user_balance - amount
            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                cur.execute(
                    "UPDATE users SET balance = ? WHERE login = ?",
                    (new_balance, self.current_user)
                )
            status = "SUCCESS"
            return f"Withdrawn {input_amount}, current balance: {new_balance}"
        finally:
            self._append_log(status=status, operation="WITHDRAW", user=self.current_user, value=amount if status == "SUCCESS" else None, error_msg=error_msg)

    def deposit(self):
        status = "ERROR"
        error_msg = None
        try:
            if self.current_user is None:
                raise ATMError("SessionRequired", "You must be logged in to do that.", "Attempted to use a protected feature without an active session.")
            input_amount = input("Enter the amount to deposit: ")
            if not input_amount.strip():
                raise ATMError("FieldIsEmptyError", "Please fill in the field.", "Input field was left empty.")
            amount = int(input_amount)
            if amount <= 0:
                raise ATMError("InvalidAmountError", "Amount must be greater than zero.", f"User entered invalid deposit amount: {input_amount}.")
            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                user_balance = cur.execute(
                    "SELECT balance FROM users WHERE login = ?",
                    (self.current_user,)
                ).fetchone()[0]
        except ATMError as e:
            error_msg = repr(e)
            return str(e)
        except ValueError as e:
            error_msg = repr(e)
            return "Invalid input. Please enter numbers only."
        except Exception as e:
            error_msg = repr(e)
            return "Unknown error occurred."
        else:
            new_balance = user_balance + amount
            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                cur.execute(
                    "UPDATE users SET balance = ? WHERE login = ?",
                    (new_balance, self.current_user)
                )
            status = "SUCCESS"
            return f"Deposited {input_amount}, current balance: {new_balance}"
        finally:
            self._append_log(status=status, operation="DEPOSIT", user=self.current_user, value=amount if status == "SUCCESS" else None, error_msg=error_msg)

    def show_balance(self):
        status = "ERROR"
        error_msg = None
        try:
            if self.current_user is None:
                raise ATMError("SessionRequired", "You must be logged in to do that.", "Attempted to use a protected feature without an active session.")
        except ATMError as e:
            error_msg = repr(e)
            return str(e)
        except Exception as e:
            error_msg = repr(e)
            return "Unknown error occurred."
        else:
            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                user_balance = cur.execute(
                    "SELECT balance FROM users WHERE login = ?",
                    (self.current_user,)
                ).fetchone()[0]
            status = "SUCCESS"
            return f"Your balance is {user_balance}."
        finally:
            self._append_log(status=status, operation="SHOWBALANCE", user=self.current_user, value=user_balance if status == "SUCCESS" else None, error_msg=error_msg)

    def login(self):
        status = "ERROR"
        error_msg = None
        try:
            input_login = input("Hello, please enter your login and password to continue.\nLogin: ")
            input_login = input_login.strip()
            if not input_login:
                raise ATMError("FieldIsEmptyError", "Please fill in the field.", "Input field was left empty.")
            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                cur.execute(
                    "SELECT 1 FROM users WHERE login = ?",
                    (input_login,)
                )
                if cur.fetchone() is None:
                    raise ATMError("UserNotFoundError", "User with such login was not found.", f"Login {input_login} given by user does was not found.",)
            input_password = input("Password: ")
            input_password = input_password.strip()
            if not input_password:
                raise ATMError("FieldIsEmptyError", "Please fill in the field.", "Input field was left empty.")
            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                actual_password = cur.execute(
                    "SELECT password FROM users WHERE login = ?",
                    (input_login,)
                ).fetchone()[0]
                if input_password != actual_password:
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
            self.current_user = input_login
            status = "SUCCESS"
            return f"You're now using ATM as {input_login}."
        finally:
            self._append_log(status=status, operation="LOGIN", user=self.current_user if status == "SUCCESS" else input_login, error_msg=error_msg)

    def register(self):
        status = "ERROR"
        error_msg = None
        try:
            input_login = input("Hello, thanks for choosing us! To continue enter following information.\nLogin(May contain only Latin letters and digits): ")
            if not input_login.strip():
                raise ATMError("FieldIsEmptyError", "Please fill in the field.", "Input field was left empty.")
            if len(input_login) < 6 or len(input_login) > 24:
                raise ATMError("InvalidLoginError", "Login length must be 5-16 characters.", f"Length of login {input_login} given by user is invalid.")
            if not re.fullmatch(r"[A-Za-z0-9]+", input_login):
                raise ATMError("InvalidLoginError", "Login may contain only Latin letters and digits.", f"Contants of login {input_login} given by user is invalid.")
            if input_login.lower() in self.FORBIDDEN_LOGINS:
                raise ATMError("InvalidLoginError", "The login is in forbidden list.", f"Login {input_login} given by user is in forbidden logins.")
            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                cur.execute(
                    "SELECT 1 FROM users WHERE login = ?",
                    (input_login,)
                )
                if cur.fetchone() is not None:
                    raise ATMError("UserAlreadyExistsError", "User with this login already exists.", f"Login {input_login} given by user already exists.",)
            input_password = input("Password(May contain only Latin letters and numbers): ")
            if not input_password.strip():
                raise ATMError("FieldIsEmptyError", "Please fill in the field.", "Input field was left empty.")


            # Validate login: length 12-24, characters A-Za-z0-9, check against forbidden list.


            with sqlite3.connect(self.users_db) as conn:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO users (login, password, balance) VALUES (?, ?, ?)",
                    (input_login, input_password, 0)
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
            self.current_user = input_login
            status = "SUCCESS"
            return f"You're now using ATM as {input_login}."
        finally:
            self._append_log(status=status, operation="REGISTRATION", user=self.current_user if status == "SUCCESS" else input_login, error_msg=error_msg)

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
print(atm01.deposit())