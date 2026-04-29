class Payment:
    def __init__(self, student_name, amount):
        self.student_name = student_name
        self.amount = amount
        self._is_processed = False

    def process(self):
        status = "Processed" if self._is_processed else "Pending"
        return f"Payment of ${self.amount} for {self.student_name} is {status}."

class CreditCard(Payment):
    def __init__(self, student_name, amount, card_last_four):
        super().__init__(student_name, amount)
        self.card_last_four = card_last_four

    def process(self):
        base_status = super().process()
        return f"{base_status} Charged to card ending in {self.card_last_four}."

class MealPlan(Payment):
    def __init__(self, student_name, amount, plan_type):
        super().__init__(student_name, amount)
        self.plan_type = plan_type

    def process(self):
        self._is_processed = True
        return f"Deducted ${self.amount} from {self.student_name}'s {self.plan_type} Meal Plan."

class FinancialAid(Payment):
    def __init__(self, student_name, amount, aid_source):
        super().__init__(student_name, amount)
        self.aid_source = aid_source

    def process(self):
        self._is_processed = True
        return f"Applied ${self.amount} from {self.aid_source} Financial Aid for {self.student_name}."

def exercise_3_polymorphism():
    print("\n--- Exercise 3: Polymorphism (Duck Typing) ---")

    cc = CreditCard("Alice", 150.00, "1234")
    meal = MealPlan("Bob", 12.50, "Flex")
    aid = FinancialAid("Charlie", 2500.00, "Pell Grant")

    entities = [cc, meal, aid]

    for entity in entities:
        print(entity.process())

if __name__ == "__main__":
    print("--- Exercise 1 & 2: Classes and Inheritance ---")

    payment1 = Payment("John Doe", 500.0)
    payment2 = CreditCard("Jane Smith", 1200.0, "9876")

    print(payment1.process())
    print(payment2.process())

    exercise_3_polymorphism()