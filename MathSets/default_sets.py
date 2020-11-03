try:
    from sets import Set
except:
    from MathSets.sets import Set

class DefaultSet(Set):
    def __init__(self, condition):
        self.condition = condition

    def __contains__(self, item):
        x = item
        if eval(self.condition):
            return True
        return False



N = DefaultSet("(type(item) == int or item == int(item)) and item >= 0")
Z = DefaultSet("(type(item) == int or item == int(item))")
R = DefaultSet("type(item) == int or type(item) == float")
