from tidal import *
from app import App
import vga2_8x16 as font

class Wednesday(App):
    
    def on_activate(self):
        super().on_activate()
        self.draw_frog()
    
    def draw_frog(self):
        display.fill(WHITE)
        display.text(font, 'IT IS WEDNESDAY', 8, 60, BLACK, WHITE)
        display.jpg('apps/Wednesday/WednesdayFrog.jpg', 17, 80)
        display.text(font, 'MY DUDES', 37, 170, BLACK, WHITE)


main = Wednesday
