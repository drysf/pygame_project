"""
Gestionnaire d'états pour les différentes scènes du jeu
"""


class StateManager:
    """Gère la transition entre états du jeu (menu, jeu, pause)"""
    
    def __init__(self):
        self.states = {}
        self.current_state = None
        self.previous_state = None
    
    def add_state(self, name, state):
        """Ajoute un état au gestionnaire"""
        self.states[name] = state
    
    def set_state(self, name):
        """Change l'état actuel"""
        if name in self.states:
            self.previous_state = self.current_state
            self.current_state = name
    
    def get_current(self):
        """Retourne l'objet de l'état actuel"""
        return self.states.get(self.current_state)
    
    def get_previous(self):
        """Retourne l'objet de l'état précédent"""
        return self.states.get(self.previous_state)
    
    def update(self, dt):
        """Met à jour l'état actuel"""
        current = self.get_current()
        if current and hasattr(current, 'update'):
            current.update(dt)
    
    def draw(self):
        """Affiche l'état actuel"""
        current = self.get_current()
        if current and hasattr(current, 'draw'):
            current.draw()
    
    def handle_event(self, event):
        """Gère les événements de l'état actuel"""
        current = self.get_current()
        if current and hasattr(current, 'handle_event'):
            current.handle_event(event)
