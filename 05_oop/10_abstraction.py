"""
10_abstraction.py

This file demonstrates:
- What abstraction is
- Abstract Base Classes (ABC)
- abstractmethod
- Enforcing contracts
- Real-world abstraction example
"""

from abc import ABC, abstractmethod


# -------------------------
# ABSTRACT BASE CLASS
# -------------------------
class Payment(ABC):
    """
    Abstract class:
    - Cannot be instantiated
    - Forces child classes to implement required methods
    """

    @abstractmethod
    def pay(self, amount):
        pass


# -------------------------
# CONCRETE IMPLEMENTATIONS
# -------------------------
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


# -------------------------
# USING ABSTRACTION
# -------------------------
def process_payment(payment_method: Payment, amount):
    """
    This function does NOT care how payment happens.
    It only knows that payment_method has a pay() method.
    """
    payment_method.pay(amount)


print("=== Abstraction Example ===")
process_payment(CreditCardPayment(), 500)
process_payment(UPIPayment(), 1000)


# -------------------------
# WHAT HAPPENS IF METHOD IS NOT IMPLEMENTED
# -------------------------
class CashPayment(Payment):
    pass   # ❌ Missing pay()


# Uncommenting below will raise TypeError
# cash = CashPayment()


# -------------------------
# WHY ABSTRACTION MATTERS
# -------------------------
"""
Key idea:
- process_payment() works with ANY payment type
- New payment methods can be added WITHOUT changing existing code
- This follows Open/Closed Principle
"""


# -------------------------
# KEY TAKEAWAYS
# -------------------------
# - Abstraction exposes WHAT, hides HOW
# - Abstract classes define contracts
# - Child classes MUST implement abstract methods
# - Abstraction reduces coupling
# - Widely used in frameworks like Django & DRF
