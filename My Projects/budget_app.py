class Category:
    """
    A budget category that tracks deposits, withdrawals, and transfers.
    """

    def __init__(self, name):
        """
        Initialize a budget category.

        Parameters:
            name (str): Name of the budget category.
        """
        self.name = name
        self.ledger = []
        self.total_amount = 0
        self.withdraw_amount = 0

    # ------------------------------------------------
    # Utility methods
    # ------------------------------------------------
    def check_funds(self, amount):
        """
        Check if there are sufficient funds for a transaction.

        Parameters:
            amount (float): Amount to be checked.

        Returns:
            bool: True if enough funds are available, otherwise False.
        """
        return amount <= self.total_amount

    # ------------------------------------------------
    # Transaction methods
    # ------------------------------------------------
    def deposit(self, amount, description=None):
        """
        Deposit money into the category.

        Parameters:
            amount (float): Amount to deposit.
            description (str, optional): Description of the transaction.
        """
        entry = {
            "amount": amount,
            "description": description if description is not None else ""
        }

        self.ledger.append(entry)
        self.total_amount += amount

    def withdraw(self, amount, description=None):
        """
        Withdraw money from the category if sufficient funds exist.

        Parameters:
            amount (float): Amount to withdraw.
            description (str, optional): Description of the transaction.

        Returns:
            bool: True if withdrawal was successful, otherwise False.
        """
        if not self.check_funds(amount):
            return False

        entry = {
            "amount": -amount,
            "description": description if description is not None else ""
        }

        self.ledger.append(entry)
        self.total_amount -= amount
        self.withdraw_amount += amount
        return True

    def transfer(self, amount, category):
        """
        Transfer money from this category to another category.

        Parameters:
            amount (float): Amount to transfer.
            category (Category): Target category.

        Returns:
            bool: True if transfer was successful, otherwise False.
        """
        if not self.check_funds(amount):
            return False

        # Record withdrawal from current category
        self.ledger.append({
            "amount": -amount,
            "description": f"Transfer to {category.name.capitalize()}"
        })
        self.total_amount -= amount
        self.withdraw_amount += amount

        # Record deposit into target category
        category.ledger.append({
            "amount": amount,
            "description": f"Transfer from {self.name.capitalize()}"
        })
        category.total_amount += amount

        return True

    # ------------------------------------------------
    # Accessors and string representation
    # ------------------------------------------------
    def get_balance(self):
        """
        Return the current balance of the category.
        """
        return self.total_amount

    def __str__(self):
        """
        Return a formatted string representation of the ledger.
        """
        title = f"{self.name.capitalize():*^30}\n"
        body = ""

        for item in self.ledger:
            description = item["description"][:23]
            amount = item["amount"]

            # Align amount to the right with two decimal places
            body += f"{description:<23}{amount:>7.2f}\n"

        total = f"Total: {self.get_balance():.2f}"
        return title + body + total


def create_spend_chart(categories):
    """
    Create a bar chart showing the percentage spent by each category.

    Parameters:
        categories (list): A list of Category objects.

    Returns:
        str: A formatted percentage spend chart.
    """

    # Chart title
    chart = "Percentage spent by category\n"

    # ------------------------------------------------
    # Calculate total withdrawals
    # ------------------------------------------------
    total_withdrawals = sum(cat.withdraw_amount for cat in categories)

    # Calculate percentage spent for each category (rounded down to nearest 10)
    percentages = [
        int((cat.withdraw_amount / total_withdrawals) * 100) // 10 * 10
        for cat in categories
    ]

    # ------------------------------------------------
    # Build vertical bar chart
    # ------------------------------------------------
    for level in range(100, -1, -10):
        chart += f"{level:>3}| "
        for pct in percentages:
            chart += "o  " if pct >= level else "   "
        chart += "\n"

    # ------------------------------------------------
    # Add horizontal divider
    # ------------------------------------------------
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # ------------------------------------------------
    # Add category labels vertically
    # ------------------------------------------------
    names = [cat.name.capitalize() for cat in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += f"{name[i] if i < len(name) else ' '}  "
        chart += "\n"

    return chart.rstrip("\n")
