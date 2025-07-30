class EventBus:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_type, callback):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(callback)

    def unsubscribe(self, event_type, callback):
        if event_type in self.listeners and callback in self.listeners[event_type]:
            self.listeners[event_type].remove(callback)

    def publish(self, event_type, *args, **kwargs):
        if event_type in self.listeners:
            for callback in self.listeners[event_type]:
                try:
                    callback(*args, **kwargs)
                except Exception as e:
                    print(f"Error in event callback for {event_type}: {e}")

# Instance globale du bus d'événements
event_bus = EventBus()