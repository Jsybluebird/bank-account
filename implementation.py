import tkinter as tk
from bank_account import SavingsAccount

class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bank App")
        self.geometry("400x400")

        self.account = SavingsAccount()

        self.balance_label = tk.Label(self, text=f'Account balance: {self.account.account_balance} dollars')
        self.balance_label.pack(pady=10)

        self.deposit_label = tk.Label(self, text="Enter deposit amount:")
        self.deposit_label.pack()

        self.deposit_entry = tk.Entry(self)
        self.deposit_entry.pack()

        self.deposit_button = tk.Button(self, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=10)

        self.withdraw_label = tk.Label(self, text="Enter withdrawal amount:")
        self.withdraw_label.pack()

        self.withdraw_entry = tk.Entry(self)
        self.withdraw_entry.pack()

        self.withdraw_button = tk.Button(self, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(pady=10)

        self.interest_button = tk.Button(self, text="Calculate Interest", command=self.calculate_interest)
        self.interest_button.pack(pady=10)

        self.reset_button = tk.Button(self, text="Reset Withdrawal Count", command=self.reset_withdraw_count)
        self.reset_button.pack(pady=10)

    def deposit(self):
        amount = float(self.deposit_entry.get())
        self.account.deposit(amount)
        self.update_balance_label()

    def withdraw(self):
        amount = float(self.withdraw_entry.get())
        self.account.withdraw(amount)
        self.update_balance_label()

    def calculate_interest(self):
        self.account.calculate_interest()
        self.update_balance_label()

    def reset_withdraw_count(self):
        self.account.reset_withdraw_count()
        self.update_balance_label()

    def update_balance_label(self):
        self.balance_label.config(text=f'Account balance: {self.account.account_balance:.2f} dollars')

if __name__ == "__main__":
    app = BankApp()
    app.mainloop()