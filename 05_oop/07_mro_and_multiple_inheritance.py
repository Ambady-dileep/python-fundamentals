"""
This file demonstrates:
- Multiple inheritance
- Method Resolution Order (MRO)
- Diamond problem
- How super() works with MRO
"""

# -------------------------
# BASIC MULTIPLE INHERITANCE
# -------------------------
class A:
    def show(self):
        print("Class A")


class B:
    def show(self):
        print("Class B")


class C(A, B):
    pass


print("MRO of C:", C.mro())

c = C()
c.show()  # A is called first


# -------------------------
# DIAMOND PROBLEM
# -------------------------
class X:
    def show(self):
        print("Class X")


class Y(X):
    def show(self):
        print("Class Y")
        super().show()


class Z(X):
    def show(self):
        print("Class Z")
        super().show()


class D(Y, Z):
    def show(self):
        print("Class D")
        super().show()


print("\nMRO of D:", D.mro())

d = D()
d.show()

# Expected order:
# D -> Y -> Z -> X -> object


# -------------------------
# super() FOLLOWS MRO
# -------------------------
"""
Important rule:
super() does NOT call the parent class directly.
It calls the NEXT class in the MRO list.
"""

# Output explanation:
# Class D
# Class Y
# Class Z
# Class X


# -------------------------
# KEY TAKEAWAYS
# -------------------------
# - Python resolves methods using MRO
# - MRO can be inspected using ClassName.mro()
# - super() follows MRO, not parent-child assumption
# - Diamond problem is safely handled by Python
# - Use multiple inheritance carefully
