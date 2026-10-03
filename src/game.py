PHASES = ("draw_phase", "main_phase", "battle_phase", "end_phase")


class Game:
    def __init__(self):
        self.phase = PHASES[0]
    
    def next_phase(self):
        current_index = PHASES.index(self.phase)
        self.phase = PHASES[(current_index + 1) % len(PHASES)]
        return self.phase