try:
    import sets
except:
    import MathSets.sets as sets

class DefaultSet(sets.Set):
    def __init__(self, condition):
        self.condition = condition

    def __invert__(self):
        return DefaultSet(f"not ({self.condition})")

    def __add__(self, other):
        return DefaultSet(f"({self.condition}) or ({other.condition})")

    def __sub__(self, other):
        return DefaultSet(f"({self.condition}) and not ({other.condition})")

    def __contains__(self, item):
        x = item
        if eval(self.condition):
            return True
        return False



N = DefaultSet("(type(item) == int or item == int(item)) and item >= 0")
Z = DefaultSet("(type(item) == int or item == int(item))")
R = DefaultSet("type(item) == int or type(item) == float")
