try:
    from sets import Set
except:
    from MathSets.sets import Set

class DefaultSet(Set):
    def __init__(self, condition, string_form):
        self.condition = condition
        self.string_form = string_form

    def __contains__(self, item):
        x = item; x #to remove the not used dashes
        if eval(self.condition):
            return True
        return False

    def __str__(self):
        return self.string_form



N = DefaultSet("(type(item) == int or item == int(item)) and item >= 0", "ℕ")
Z = DefaultSet("(type(item) == int or item == int(item))", "ℤ")
R = DefaultSet("type(item) == int or type(item) == float", "ℝ")
