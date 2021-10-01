from swap_meet.item import Item


class Decor(Item):
    def __init__(self, condition=0.0):
        super().__init__(category="Decor", condition=condition)
    def __str__(self):
        return "Something to decorate your space."
    def condition_description(self):
        return super().condition_description(self.condition)