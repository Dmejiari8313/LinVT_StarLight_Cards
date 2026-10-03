class Player:
    def __init__(self, name):
        self.name = name
        self.life_points = 5000
        self.hand = []
        self.deck = []
        self.graveyard = []
        self.field = []
    
    def draw_card(self):
        """Roba y devuelve la carta superior, o ``None`` si no hay cartas."""
        if self.deck:
            card = self.deck.pop()
            self.hand.append(card)
            return card
        return None

    def receive_damage(self, amount):
        """Aplica daño sin permitir puntos de vida negativos."""
        if amount < 0:
            raise ValueError("El daño no puede ser negativo")
        self.life_points = max(0, self.life_points - amount)