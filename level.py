from eventBus import event_bus

class Level:
    def __init__(self, name):
        self.name = name

    def loadLevel(self, *args, **kwargs):
        event_bus.subscribe('game_update', self.update)
        print(f"Loading level {self.name}")

    def unloadLevel(self):
        event_bus.unsubscribe('game_update', self.update)
        event_bus.publish("clear_render_queue", True)
        print(f"Unloading level for {self.name}")

    def update(self):
        pass
    

