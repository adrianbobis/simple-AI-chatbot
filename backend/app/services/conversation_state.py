class ConversationState:
    def __init__(self):
        self.store={}
    def get(self, player):
        return self.store.setdefault(player,{})
    def update(self, player, **kwargs):
        self.get(player).update(kwargs)
