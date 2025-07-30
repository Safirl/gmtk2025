from level import Level
from eventBus import event_bus

class ShoesLevel(Level):
    def __init__(self):
        super().__init__("shoes")

    def loadLevel(self):
        print(f"Loading {self.name} level")
        # S'abonner aux événements quand le niveau se charge
        event_bus.subscribe('mouse_moved', self.onMouseMoved)
        event_bus.subscribe('game_update', self.onUpdate)
        return super().loadLevel()

    def unloadLevel(self):
        print(f"Unloading {self.name} level")
        # Se désabonner quand le niveau se décharge
        event_bus.unsubscribe('mouse_moved', self.onMouseMoved)
        event_bus.unsubscribe('game_update', self.onUpdate)
        return super().unloadLevel()

    def onUpdate(self):
        # Logique de mise à jour du niveau
        super().update()

    def onMouseMoved(self, newPos):
        print(f"Mouse moved in shoes level: {newPos}")