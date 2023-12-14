from Event.Interfaces.IEventComponent import IEventComponent
class Button(IEventComponent):
    def __init__(self, text, width, height, font_size, font_color, bg_color, position_x, position_y, event_type):
        self.bg_color = bg_color.value
        self.font_color = font_color.value
        self.font_size = font_size
        self.text = text
        self.width = width
        self.height = height
        self.position_x = position_x
        self.position_y = position_y
        self.event_area = [position_x * width, position_y * height]
        self.event_type = event_type

    def get_event_area(self):
        return [[self.position_x, self.position_x + self.width], [self.position_y, self.position_y + self.height]]

    def get_event_type(self):
        return self.event_type
