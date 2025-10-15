class LSystem:
    def __init__(self, axiom, rules):
        self.axiom = axiom
        self.rules = rules

    def generate(self, iterations):
        result = self.axiom
        for _ in range(iterations):
            new_result = ""
            for ch in result:
                new_result += self.rules.get(ch, ch)
            result = new_result
        return result
