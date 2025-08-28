class SpriteManager:
    def __init__(self):
        self.sprite_list = []

    def add_sprite(self, sprite) -> None:
        self.sprite_list.append(sprite)

    def remove_sprite(self, sprite):
        if sprite in self.sprite_list:
            self.sprite_list.remove(sprite)

    def get_sprites(self):
        return self.sprite_list
