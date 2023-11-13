from .generic_sprite import GenericSprite

class Marker(GenericSprite):
    def __init__(self, location, size=(60, 10)) -> None:
        super().__init__(location, size, color=(0, 200, 0))
