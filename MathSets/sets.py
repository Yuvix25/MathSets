from sympy.solvers import solve
from sympy import Symbol
try:
    import MathSets.default_sets as default_sets
except:
    import default_sets


class Set:
    """Root set for all sets"""
    def contains_subset(self, set):
        for item in set:
            if not (item in self):
                return False
        return True

    def __invert__(self):
        return InvertedSet(self)
    
    def __add__(self, other):
        return UnionSet(self, other)

    def __or__(self, other):
        return UnionSet(self, other)

    def __sub__(self, other):
        return DifferenceSet(self, other)

    def __xor__(self, other):
        return SymmetricDifferenceSet(self, other)

    def __and__(self, other):
        return IntersectionSet(self, other)

    def __contains__(self, item):
        return False


class UnionSet(Set):
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def __contains__(self, item):
        if item in self.set1 or item in self.set2:
            return True
        return False

    def __str__(self):
        return "{x | x ∈ " + str(self.set1) + " ∨ x ∈ " + str(self.set2) + "}"

class IntersectionSet(Set):
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def __contains__(self, item):
        if item in self.set1 and item in self.set2:
            return True
        return False

    def __str__(self):
        return "{x | x ∈ " + str(self.set1) + " ∧ x ∈ " + str(self.set2) + "}"

class DifferenceSet(Set):
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def __contains__(self, item):
        if item in self.set1 and not item in self.set2:
            return True
        return False

    def __str__(self):
        return "{x | x ∈ " + str(self.set1) + " ∧ x ∉ " + str(self.set2) + "}"

class SymmetricDifferenceSet(Set):
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def __contains__(self, item):
        if item in (self.set1 - self.set2) + (self.set2 - self.set1):
            return True
        return False

    def __str__(self):
        return "{x | x ∈ " + str(self.set1) + " ∆ " + str(self.set2) + "}"

class InvertedSet(Set):
    def __init__(self, set):
        self.set = set

    def __contains__(self, item):
        if not item in self.set:
            return True
        return False

    def __str__(self):
        return "{x | x ∉ " + str(self.set) + "}"


class SetBuilder(Set):
    """Default Set-Builder.
    left - if is for a separation set, then it is the base set (N for instance, and can be None), if is for a replacement set, then it is the function that you apply on x.
    right - if is for a separation set, then it is the condition (for instance x > 5), if is for a replacement set, then it is the base set (N for instance, and can be None).
    set_type - type of set, 0 for Separation, 1 for replacement"""
    def __init__(self, left, right, set_type=0):
        pass
    def __new__(self, left, right, set_type=0):
        if set_type == 0:
            return SeparationSet(right, left)
        elif set_type == 1:
            return ReplacementSet(left, right)


class SeparationSet(Set): # like: {n∈ℕ|n>5}
    def __init__(self, condition, base_set=None):
        self.base_set = base_set
        self.condition = condition

    def __contains__(self, item):
        x = item; x # to remove the not used dashes
        cond_eval = eval(self.condition)
        if self.base_set == None:
            if cond_eval:
                return True
        elif item in self.base_set and cond_eval:
            return True
        return False

    def __str__(self):
        return "{x ∈ " + str(self.base_set) + " | " + self.condition + "}"

    


class ReplacementSet(Set): # like: {n*2|n∈ℕ}
    def __init__(self, func, base_set=None):
        self.base_set = base_set
        self.func = func

    def __contains__(self, item):
        x = Symbol('x')
        sols = solve(eval(self.func + f" - {item}"), x)
        if self.base_set == None and len(sols) > 0:
            return True
        else:
            for sol in sols:
                if sol in self.base_set:
                    return True
        return False

    def __str__(self):
        return "{" + self.func + " | x ∈ " + str(self.base_set) + "}"




if __name__ == "__main__": #example
    test_set0 = SeparationSet("x % 2 == 1", default_sets.N)  # currently can only use x as the variable.
    test_set1 = ReplacementSet("x**2", default_sets.N)  # currently can only use x as the variable.
    test_set2 = SeparationSet("x ** 2 == x", default_sets.N)
    test_set3 = ReplacementSet("x*2", default_sets.N)
    print(4 in test_set1 + test_set3)
    print(str(test_set0 ^ test_set2))

    print(SetBuilder("x*2", "N", 1))

    # Union: (set1 | set2), (set1 + set2)
    # Difference: set1 - set2
    # Symmetric Difference: set1 ^ set2
    # Intersection: set1 & set2
    # Invert (all that not belongs to): ~set
