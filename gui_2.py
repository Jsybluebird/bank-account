import tkinter as tk
from bank_account import SavingsAccount

class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bank App")
        self.geometry("400x500")
        self.resizable(False, False)
        self.config(bg="#F5F5F5")

        self.account = SavingsAccount()

        title_label = tk.Label(self, text="My Bank Account", font=("Helvetica", 20, "bold"), fg="#333333", bg="#F5F5F5")
        title_label.pack(pady=20)

        balance_frame = tk.Frame(self, bg="#FFFFFF", padx=20, pady=20)
        balance_frame.pack()

        balance_label = tk.Label(balance_frame, text=f'Account balance: {self.account.account_balance:.2f} dollars', font=("Helvetica", 14), fg="#333333", bg="#FFFFFF")
        balance_label.pack(side=tk.LEFT)

        refresh_button = tk.Button(balance_frame, text="Refresh", font=("Helvetica", 12), fg="#FFFFFF", bg="#0077FF", activebackground="#0055FF", activeforeground="#FFFFFF", bd=0, padx=10, pady=5, command=self.update_balance_label)
        refresh_button.pack(side=tk.RIGHT)

        deposit_frame = tk.Frame(self, bg="#FFFFFF", padx=20, pady=20)
        deposit_frame.pack()

        deposit_label = tk.Label(deposit_frame, text="Enter deposit amount:", font=("Helvetica", 14), fg="#333333", bg="#FFFFFF")
        deposit_label.pack(side=tk.LEFT)

        self.deposit_entry = tk.Entry(deposit_frame, font=("Helvetica", 14), fg="#333333", bg="#F5F5F5", bd=0, highlightthickness=2, highlightcolor="#0077FF", highlightbackground="#FFFFFF")
        self.deposit_entry.pack(side=tk.LEFT, padx=10)

        deposit_button = tk.Button(deposit_frame, text="Deposit", font=("Helvetica", 12), fg="#FFFFFF", bg="#0077FF", activebackground="#0055FF", activeforeground="#FFFFFF", bd=0, padx=10, pady=5, command=self.deposit)
        deposit_button.pack(side=tk.RIGHT)

        withdraw_frame = tk.Frame(self, bg="#FFFFFF", padx=20, pady=20)
        withdraw_frame.pack()

        withdraw_label = tk.Label(withdraw_frame, text="Enter withdrawal amount:", font=("Helvetica", 14), fg="#333333", bg="#FFFFFF")
        withdraw_label.pack(side=tk.LEFT)

        self.withdraw_entry = tk.Entry(withdraw_frame, font=("Helvetica", 14), fg="#333333", bg="#F5F5F5", bd=0, highlightthickness=2, highlightcolor="#0077FF", highlightbackground="#FFFFFF")
        self.withdraw_entry.pack(side=tk.LEFT, padx=10)

        withdraw_button = tk.Button(withdraw_frame, text="Withdraw", font=("Helvetica", 12), fg="#FFFFFF", bg="#0077FF", activebackground="#0055FF", activeforeground="#FFFFFF", bd=0, padx=10, pady=5, command=self.withdraw)
        withdraw_button.pack(side=tk.RIGHT)

        interest_button = tk.Button(self, text="Calculate Interest", font=("Helvetica", 12), fg="#FFFFFF", bg="#0077FF", activebackground="#0055FF", activeforeground="#FFFFFF", bd=0, padx=10, pady=5, command=self.calculate_interest)
        interest_button.pack(pady=10)

        reset_button = tk.Button(self, text="Reset Account", font=("Helvetica", 12),
##