from sympy.solvers import solve
from sympy import Symbol
import boolean


class Set:
    def set_in(self, set):
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
        return SymetricDifferenceSet(self, other)

    def __and__(self, other):
        return IntersectionSet(self, other)


class UnionSet(Set):
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def __contains__(self, item):
        if item in self.set1 or item in self.set2:
            return True
        return False

class IntersectionSet(Set):
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def __contains__(self, item):
        if item in self.set1 and item in self.set2:
            return True
        return False

class DifferenceSet(Set):
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def __contains__(self, item):
        if item in self.set1 and not item in self.set2:
            return True
        return False

class SymetricDifferenceSet(Set):
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def __contains__(self, item):
        if item in (self.set1 - self.set2) + (self.set2 - self.set1):
            return True
        return False

class InvertedSet(Set):
    def __init__(self, set):
        self.set = set

    def __contains__(self, item):
        if not item in self.set:
            return True
        return False




class SeperationSet(Set):
    def __init__(self, mother_set, condition):
        self.mother_set = mother_set
        self.condition = condition

    def __contains__(self, item):
        x = item
        if item in self.mother_set and eval(self.condition):
            return True
        return False

    


class ReplacementSet(Set):
    def __init__(self, func, mother_set):
        self.mother_set = mother_set
        self.func = func

    def __contains__(self, item):
        x = Symbol('x')
        sols = solve(eval(self.func + f" - {item}"), x)
        for sol in sols:
            if sol in self.mother_set:
                return True
        return False




if __name__ == "__main__":
    try:
        import MathSets.default_sets as default_sets
    except:
        import default_sets
    test_set0 = SeperationSet(default_sets.N, "x % 2 == 1")
    test_set1 = ReplacementSet("x**2", default_sets.N)
    test_set2 = SeperationSet(default_sets.N, "x ** 2 == x")
    test_set3 = ReplacementSet("x*2", default_sets.N)
    print(4 in test_set1+test_set3)
