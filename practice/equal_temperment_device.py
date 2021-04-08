import sys

import pygame as pg
import pygame.midi as midi

class MidiPlayer:
    def __init__(self, key_mapping):
        midi.init()
        # Used to find the one for timidity
        print(midi.get_device_info(0))
        print(midi.get_device_info(1))
        print(midi.get_device_info(2))
        port = midi.get_default_output_id()
        port = 2
        self.out = midi.Output(port, 0)
        self.instrument = 0
        self.out.set_instrument(self.instrument)
        self.key_mapping = key_mapping

        
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                self.instrument += 1
                self.out.set_instrument(self.instrument)
            elif event.key == pg.K_DOWN:
                self.instrument -= 1        
                self.out.set_instrument(self.instrument)                
            else:
                try:
                    note = self.key_mapping[event.key]
                    self.out.note_on(note, 127)
                    print('on: ', event.key)
                except KeyError:
                    pass
        elif event.type == pg.KEYDOWN:
            try:
                note = self.key_mapping[event.key]
                self.out.note_off(note, 127)
            except KeyError:
                pass
                
                
class App(object):
    def __init__(self, screen_size):
        self.done = False
        self.screen = pg.display.set_mode(screen_size)
        self.clock = pg.time.Clock()
        self.fps = 60
        self.bg_color = pg.Color("gray5")
        self.player = MidiPlayer()
        
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
                self.player.out = None
                midi.quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.done = True                
            self.player.get_event(event)
            
    def update(self, dt):
        pass
        
    def draw(self):
        self.screen.fill(self.bg_color)
        
    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pg.display.update()
            
       
if __name__ == "__main__":

    vertical_snake_mapping = {
    pg.K_z: 0, pg.K_a: 1,pg.K_q: 2,pg.K_1: 3,pg.K_2: 4,pg.K_w: 5,pg.K_s: 6,pg.K_x: 7,pg.K_c: 8,pg.K_d: 9,pg.K_e: 10,pg.K_3: 11,
    pg.K_v: 12,pg.K_f: 13,pg.K_r: 14,pg.K_4: 15,pg.K_5: 16,pg.K_t: 17,pg.K_g: 18,pg.K_b: 19,pg.K_n: 20,pg.K_h: 21,pg.K_y: 22,pg.K_6: 23,
    pg.K_m: 24,pg.K_j: 25,pg.K_u: 26,pg.K_7: 27,pg.K_8: 28,pg.K_i: 29,pg.K_k: 30,pg.K_,: 31,pg.K_.: 32,pg.K_l: 33,pg.K_o: 34,pg.K_9: 35
    }

    pg.init()
    app = App((1280, 720))
    app.run()
    pg.quit()
    sys.exit()
