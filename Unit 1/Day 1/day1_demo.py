"""
ICD2O Day 1 demo: THE LAST TERMINAL (vertical slice, three rooms)
Kevin DesLauriers, Bayview Glen.

One file. No image files, no sound files, no internet, no installs beyond pygame.
Every sprite and every sound is generated in code at startup, so nothing can go
missing on the day.

Run:  python day1_demo.py
Keys: arrows or WASD to move, SPACE or E to talk and to advance dialogue,
      R to restart, ESC to quit, F to toggle fullscreen.

Rooms: 1 the hall (talk, find the key), 2 the vault corridor (three plates,
three drones, one timer), 3 the terminal.
"""

import math
import struct
import pygame

# ----------------------------------------------------------------- settings

TILE = 16
SCALE = 3
PX = TILE * SCALE
SCREEN_W = 960
SCREEN_H = 600
FPS = 60
PLATE_WINDOW = 11.0         # seconds to hit all three plates
DRONE_STUN = 0.9            # seconds of lockout after a drone hit

C_BG = (12, 12, 20)
C_UI = (240, 240, 245)
C_UI_DIM = (150, 150, 165)
C_BOX = (18, 20, 34)
C_BOX_EDGE = (120, 200, 255)
C_ALERT = (255, 95, 105)
C_GOOD = (90, 220, 150)

# ----------------------------------------------------------------- pixel art
# Each sprite is a list of strings. One character is one pixel.

PAL = {
    "k": (18, 18, 26),
    "s": (240, 200, 170),
    "h": (60, 40, 30),
    "j": (70, 130, 220),
    "J": (45, 95, 175),
    "p": (50, 55, 80),
    "b": (35, 38, 58),
    "r": (220, 80, 90),
    "R": (170, 55, 70),
    "w": (235, 235, 245),
    "y": (255, 205, 70),
    "Y": (205, 155, 35),
    "c": (120, 200, 255),
    "g": (90, 220, 150),
    "m": (120, 126, 150),
    "M": (78, 84, 108),
    "e": (255, 95, 105),
}

PLAYER_DOWN_A = [
    "                ",
    "     kkkkkk     ",
    "    khhhhhhk    ",
    "    khhhhhhk    ",
    "    ksssssssk   ",
    "    ksksskskk   ",
    "    ksssssssk   ",
    "     kssssk     ",
    "   kkjjjjjjkk   ",
    "   kjJjjjjJjk   ",
    "   kjJjjjjJjk   ",
    "   kkjjjjjjkk   ",
    "     kppppk     ",
    "     kppppk     ",
    "     kbk bk     ",
    "     kkk kk     ",
]

PLAYER_DOWN_B = [
    "                ",
    "     kkkkkk     ",
    "    khhhhhhk    ",
    "    khhhhhhk    ",
    "    ksssssssk   ",
    "    ksksskskk   ",
    "    ksssssssk   ",
    "     kssssk     ",
    "   kkjjjjjjkk   ",
    "   kjJjjjjJjk   ",
    "   kjJjjjjJjk   ",
    "   kkjjjjjjkk   ",
    "     kppppk     ",
    "    kppppppk    ",
    "   kbk    kbk   ",
    "   kkk    kkk   ",
]

PLAYER_UP_A = [
    "                ",
    "     kkkkkk     ",
    "    khhhhhhk    ",
    "    khhhhhhk    ",
    "    khhhhhhhk   ",
    "    khhhhhhhk   ",
    "    khhhhhhhk   ",
    "     khhhhk     ",
    "   kkjjjjjjkk   ",
    "   kjJjjjjJjk   ",
    "   kjJjjjjJjk   ",
    "   kkjjjjjjkk   ",
    "     kppppk     ",
    "     kppppk     ",
    "     kbk bk     ",
    "     kkk kk     ",
]

PLAYER_UP_B = [
    "                ",
    "     kkkkkk     ",
    "    khhhhhhk    ",
    "    khhhhhhk    ",
    "    khhhhhhhk   ",
    "    khhhhhhhk   ",
    "    khhhhhhhk   ",
    "     khhhhk     ",
    "   kkjjjjjjkk   ",
    "   kjJjjjjJjk   ",
    "   kjJjjjjJjk   ",
    "   kkjjjjjjkk   ",
    "     kppppk     ",
    "    kppppppk    ",
    "   kbk    kbk   ",
    "   kkk    kkk   ",
]

PLAYER_SIDE_A = [
    "                ",
    "     kkkkk      ",
    "    khhhhhk     ",
    "    khhhhhhk    ",
    "    khsssssk    ",
    "    khskssk     ",
    "    khssssk     ",
    "     ksssk      ",
    "    kkjjjjkk    ",
    "    kjjjjJjk    ",
    "    kjjjjJjk    ",
    "    kkjjjjkk    ",
    "     kpppk      ",
    "     kpppk      ",
    "     kbbk       ",
    "     kkkk       ",
]

PLAYER_SIDE_B = [
    "                ",
    "     kkkkk      ",
    "    khhhhhk     ",
    "    khhhhhhk    ",
    "    khsssssk    ",
    "    khskssk     ",
    "    khssssk     ",
    "     ksssk      ",
    "    kkjjjjkk    ",
    "    kjjjjJjk    ",
    "    kjjjjJjk    ",
    "    kkjjjjkk    ",
    "     kpppk      ",
    "    kppppk      ",
    "   kbk  kbk     ",
    "   kkk  kkk     ",
]

NPC_A = [
    "                ",
    "     kkkkkk     ",
    "    kwwwwwwk    ",
    "    kwwwwwwk    ",
    "    kssssssk    ",
    "    kskssksk    ",
    "    kssssssk    ",
    "     kssssk     ",
    "   kkrrrrrrkk   ",
    "   krRrrrrRrk   ",
    "   krrrrrrrrk   ",
    "   krRrrrrRrk   ",
    "   krrrrrrrrk   ",
    "   kkrrrrrrkk   ",
    "     kkkkkk     ",
    "                ",
]

NPC_B = [
    "                ",
    "     kkkkkk     ",
    "    kwwwwwwk    ",
    "    kwwwwwwk    ",
    "    kssssssk    ",
    "    kskssksk    ",
    "    kssssssk    ",
    "     kssssk     ",
    "   kkrrrrrrkk   ",
    "   krRrrrrRrk   ",
    "   krrrrrrrrk   ",
    "   krRrrrrRrk   ",
    "   krrrrrrrrk   ",
    "  kkrrrrrrrrkk  ",
    "    kkkkkkkk    ",
    "                ",
]

KEY_SPRITE = [
    "                ",
    "                ",
    "     kkkk       ",
    "    kyyyyk      ",
    "    kyYYyk      ",
    "    kyyyyk      ",
    "     kyyk       ",
    "     kyyk       ",
    "     kyyk       ",
    "     kyyk       ",
    "     kyykk      ",
    "     kyyYk      ",
    "     kyykk      ",
    "     kyyYk      ",
    "     kkkk       ",
    "                ",
]

TERMINAL_SPRITE = [
    "                ",
    "  kkkkkkkkkkkk  ",
    "  kppppppppppk  ",
    "  kpcccccccckp  ",
    "  kpcggggggckp  ",
    "  kpcgccccgckp  ",
    "  kpcgccccgckp  ",
    "  kpcggggggckp  ",
    "  kpcccccccckp  ",
    "  kppppppppppk  ",
    "  kkkkkkkkkkkk  ",
    "    kpppppppk   ",
    "    kpppppppk   ",
    "   kkkkkkkkkkk  ",
    "   kppppppppppk ",
    "   kkkkkkkkkkkk ",
]

DRONE_A = [
    "                ",
    "                ",
    "      kkkk      ",
    "    kkmmmmkk    ",
    "   kmmmmmmmmk   ",
    "  kmmMMMMMMmmk  ",
    "  kmMeeeeeeMmk  ",
    "  kmMeeeeeeMmk  ",
    "  kmmMMMMMMmmk  ",
    "   kmmmmmmmmk   ",
    "    kkmmmmkk    ",
    "      kkkk      ",
    "       ee       ",
    "                ",
    "                ",
    "                ",
]

DRONE_B = [
    "                ",
    "                ",
    "      kkkk      ",
    "    kkmmmmkk    ",
    "   kmmmmmmmmk   ",
    "  kmmMMMMMMmmk  ",
    "  kmMeeeeeeMmk  ",
    "  kmMeeeeeeMmk  ",
    "  kmmMMMMMMmmk  ",
    "   kmmmmmmmmk   ",
    "    kkmmmmkk    ",
    "      kkkk      ",
    "      eeee      ",
    "       ee       ",
    "                ",
    "                ",
]

NOTE_SPRITE = [
    "                ",
    "                ",
    "     kkkkkk     ",
    "    kwwwwwwk    ",
    "    kwkkkkwk    ",
    "    kwwwwwwk    ",
    "    kwkkkkwk    ",
    "    kwwwwwwk    ",
    "    kwkkkwwk    ",
    "    kwwwwwwk    ",
    "     kkkkkk     ",
    "                ",
    "                ",
    "                ",
    "                ",
    "                ",
]


def build_sprite(rows):
    surf = pygame.Surface((TILE, TILE), pygame.SRCALPHA)
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch != " " and ch in PAL:
                surf.set_at((x, y), PAL[ch])
    return pygame.transform.scale(surf, (PX, PX))


def flip_sprite(surf):
    return pygame.transform.flip(surf, True, False)


# ----------------------------------------------------------------- tiles

def build_tiles():
    tiles = {}

    floor = pygame.Surface((TILE, TILE))
    floor.fill((44, 48, 66))
    for x in range(TILE):
        for y in range(TILE):
            if (x * 7 + y * 13) % 23 == 0:
                floor.set_at((x, y), (52, 57, 78))
            if x == 0 or y == 0:
                floor.set_at((x, y), (38, 42, 58))
    tiles["."] = pygame.transform.scale(floor, (PX, PX))

    wall = pygame.Surface((TILE, TILE))
    wall.fill((78, 70, 92))
    for x in range(TILE):
        wall.set_at((x, 0), (108, 100, 126))
        wall.set_at((x, TILE - 1), (46, 42, 58))
    for y in range(TILE):
        wall.set_at((0, y), (58, 52, 70))
        wall.set_at((TILE - 1, y), (58, 52, 70))
    for x in range(2, TILE - 2):
        wall.set_at((x, 7), (58, 52, 70))
        wall.set_at((x, 8), (58, 52, 70))
    tiles["#"] = pygame.transform.scale(wall, (PX, PX))

    crate = pygame.Surface((TILE, TILE))
    crate.fill((44, 48, 66))
    pygame.draw.rect(crate, (140, 100, 60), (2, 2, 12, 12))
    pygame.draw.rect(crate, (95, 65, 38), (2, 2, 12, 12), 1)
    pygame.draw.line(crate, (95, 65, 38), (2, 2), (13, 13))
    pygame.draw.line(crate, (95, 65, 38), (13, 2), (2, 13))
    tiles["C"] = pygame.transform.scale(crate, (PX, PX))

    door = pygame.Surface((TILE, TILE))
    door.fill((44, 48, 66))
    pygame.draw.rect(door, (150, 60, 70), (1, 0, 14, 16))
    pygame.draw.rect(door, (70, 28, 34), (1, 0, 14, 16), 1)
    pygame.draw.rect(door, (255, 205, 70), (10, 7, 2, 3))
    tiles["D"] = pygame.transform.scale(door, (PX, PX))

    open_door = pygame.Surface((TILE, TILE))
    open_door.fill((26, 30, 44))
    pygame.draw.rect(open_door, (90, 220, 150), (1, 0, 14, 16), 1)
    tiles["O"] = pygame.transform.scale(open_door, (PX, PX))

    plate_off = pygame.Surface((TILE, TILE))
    plate_off.fill((44, 48, 66))
    pygame.draw.rect(plate_off, (86, 92, 118), (2, 2, 12, 12))
    pygame.draw.rect(plate_off, (30, 34, 50), (2, 2, 12, 12), 1)
    pygame.draw.rect(plate_off, (60, 66, 88), (5, 5, 6, 6))
    tiles["p"] = pygame.transform.scale(plate_off, (PX, PX))

    plate_on = pygame.Surface((TILE, TILE))
    plate_on.fill((44, 48, 66))
    pygame.draw.rect(plate_on, (60, 150, 110), (2, 2, 12, 12))
    pygame.draw.rect(plate_on, (30, 34, 50), (2, 2, 12, 12), 1)
    pygame.draw.rect(plate_on, (140, 255, 190), (5, 5, 6, 6))
    tiles["P"] = pygame.transform.scale(plate_on, (PX, PX))

    return tiles


# ----------------------------------------------------------------- sound

def make_tone(freq, ms, volume=0.25, kind="square", sweep=0.0):
    rate = 22050
    n = int(rate * ms / 1000.0)
    data = bytearray()
    for i in range(n):
        t = i / float(rate)
        f = freq + sweep * (i / float(max(n, 1)))
        phase = (t * f) % 1.0
        if kind == "square":
            v = 1.0 if phase < 0.5 else -1.0
        elif kind == "saw":
            v = 2.0 * phase - 1.0
        else:
            v = math.sin(2.0 * math.pi * phase)
        fade = min(1.0, (n - i) / float(rate * 0.03 + 1))
        attack = min(1.0, i / float(rate * 0.005 + 1))
        s = int(max(-1.0, min(1.0, v)) * volume * fade * attack * 32767)
        data.extend(struct.pack("<hh", s, s))
    return pygame.mixer.Sound(buffer=bytes(data))


class Audio:
    """Every sound is optional. If the mixer fails, the demo still runs."""

    def __init__(self):
        self.ok = False
        self.plates = []
        try:
            pygame.mixer.pre_init(22050, -16, 2, 512)
            pygame.mixer.init()
            self.blip = make_tone(620, 40, 0.18, "square")
            self.step = make_tone(150, 45, 0.10, "saw")
            self.pickup = make_tone(700, 180, 0.22, "square", sweep=500)
            self.unlock = make_tone(320, 300, 0.25, "square", sweep=260)
            self.deny = make_tone(200, 160, 0.20, "saw", sweep=-80)
            self.hit = make_tone(340, 220, 0.24, "saw", sweep=-220)
            self.timeout = make_tone(260, 420, 0.20, "square", sweep=-140)
            self.win = make_tone(440, 500, 0.24, "sine", sweep=440)
            self.plates = [
                make_tone(523, 150, 0.20, "square"),
                make_tone(659, 150, 0.20, "square"),
                make_tone(784, 260, 0.22, "square", sweep=120),
            ]
            self.ok = True
        except Exception as exc:
            print("Audio disabled:", exc)

    def play(self, name):
        if not self.ok:
            return
        snd = getattr(self, name, None)
        if snd is not None:
            snd.play()

    def play_plate(self, index):
        if not self.ok or index >= len(self.plates):
            return
        self.plates[index].play()


# ----------------------------------------------------------------- rooms

ROOM_ONE = [
    "########################",
    "#......................#",
    "#..CC..................#",
    "#..CC..................#",
    "#......................#",
    "#.............#####....#",
    "#.............#...#....#",
    "#.............#...#....#",
    "#......................#",
    "#..........#######.....#",
    "#......................#",
    "#......................#",
    "#......................#",
    "###########DD###########",
]

ROOM_TWO = [
    "########################",
    "#......................#",
    "#..p...................#",
    "#......#########.......#",
    "#......#.......#.......#",
    "#......#...p...#.......#",
    "#......#.......#.......#",
    "#......#####.###.......#",
    "#......................#",
    "#...........#####......#",
    "#..................p...#",
    "#......................#",
    "#......................#",
    "###########DD###########",
]

ROOM_THREE = [
    "########################",
    "#......................#",
    "#....########..........#",
    "#....#......#..........#",
    "#....#......#..........#",
    "#....#......#..........#",
    "#..............#####...#",
    "#..............#...#...#",
    "#..............#...#...#",
    "#......................#",
    "#......................#",
    "#......................#",
    "#......................#",
    "########################",
]

ROOM_ONE_KEY = (3, 4)
ROOM_ONE_NPC = (17, 4)
ROOM_ONE_NOTE = (19, 11)
ROOM_ONE_START = (11, 11)
ROOM_TWO_START = (11, 1)
ROOM_TWO_PLATES = [(3, 2), (11, 5), (19, 10)]
ROOM_THREE_START = (18, 2)
ROOM_THREE_TERMINAL = (8, 3)

# Drones: (start tile x, end tile x, tile y, speed in pixels per second, offset)
ROOM_TWO_DRONES = [
    (1, 22, 8, 165.0, 0.0),
    (22, 1, 11, 135.0, 0.4),
    (8, 14, 4, 115.0, 0.0),
]

DIALOGUE_LOCKED = [
    "You made it. Most people never get this far.",
    "The door south is locked, and I do not have the key.",
    "Look near the crates in the north west corner.",
    "Whoever left in a hurry left it behind.",
]

DIALOGUE_HAS_KEY = [
    "That is the one. Go south.",
    "Past that door is the vault corridor. Read the note first.",
    "Whatever is running down there has been running a long time.",
]

DIALOGUE_NOTE = [
    "A note, scratched in a hurry:",
    "THREE PLATES OPEN THE VAULT. ALL THREE, OR NONE.",
    "THEY GO DARK AGAIN IF YOU ARE SLOW.",
    "AND THE DRONES DO NOT LIKE COMPANY.",
]


class Particle:
    def __init__(self, x, y, vx, vy, life, colour):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.life = life
        self.max_life = life
        self.colour = colour

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.25
        self.life -= 1


class Drone:
    def __init__(self, x1, x2, ty, speed, offset):
        self.x1 = min(x1, x2) * PX
        self.x2 = max(x1, x2) * PX
        self.y = ty * PX
        self.speed = speed
        self.dir = 1 if x2 >= x1 else -1
        span = max(1.0, self.x2 - self.x1)
        self.x = self.x1 + span * offset
        self.frame = 0
        self.timer = 0.0

    def update(self, dt):
        self.x += self.speed * self.dir * dt
        if self.x < self.x1:
            self.x = self.x1
            self.dir = 1
        if self.x > self.x2:
            self.x = self.x2
            self.dir = -1
        self.timer += dt
        if self.timer > 0.12:
            self.timer = 0.0
            self.frame = 1 - self.frame

    def rect(self):
        return pygame.Rect(int(self.x) + 8, int(self.y) + 8, PX - 16, PX - 16)


# ----------------------------------------------------------------- game

class Game:

    def __init__(self, screen, audio, font, big_font, small_font):
        self.screen = screen
        self.audio = audio
        self.font = font
        self.big_font = big_font
        self.small_font = small_font
        self.tiles = build_tiles()

        self.player_frames = {
            "down": [build_sprite(PLAYER_DOWN_A), build_sprite(PLAYER_DOWN_B)],
            "up": [build_sprite(PLAYER_UP_A), build_sprite(PLAYER_UP_B)],
            "right": [build_sprite(PLAYER_SIDE_A), build_sprite(PLAYER_SIDE_B)],
        }
        self.player_frames["left"] = [flip_sprite(s) for s in self.player_frames["right"]]
        self.npc_frames = [build_sprite(NPC_A), build_sprite(NPC_B)]
        self.drone_frames = [build_sprite(DRONE_A), build_sprite(DRONE_B)]
        self.key_sprite = build_sprite(KEY_SPRITE)
        self.note_sprite = build_sprite(NOTE_SPRITE)
        self.terminal_sprite = build_sprite(TERMINAL_SPRITE)

        self.reset()

    # ------------------------------------------------------------- state

    def reset(self):
        self.state = "title"
        self.has_key = False
        self.read_note = False
        self.particles = []
        self.dialogue = None
        self.dialogue_line = 0
        self.typed = 0.0
        self.step_timer = 0.0
        self.shake = 0.0
        self.flash = 0.0
        self.stun = 0.0
        self.banner = ""
        self.banner_timer = 0.0
        self.win_timer = 0.0
        self.attempts = 0
        self.enter_room(1)

    def enter_room(self, number):
        self.room = number
        self.drones = []
        self.plates = {}
        self.plate_timer = 0.0
        self.door_open = False
        if number == 1:
            self.map = ROOM_ONE
            spawn = ROOM_ONE_START
            self.door_open = self.has_key
        elif number == 2:
            self.map = ROOM_TWO
            spawn = ROOM_TWO_START
            for tile in ROOM_TWO_PLATES:
                self.plates[tile] = False
            for d in ROOM_TWO_DRONES:
                self.drones.append(Drone(d[0], d[1], d[2], d[3], d[4]))
            self.set_banner("THREE PLATES. ONE TIMER. AVOID THE DRONES.")
        else:
            self.map = ROOM_THREE
            spawn = ROOM_THREE_START
        self.spawn = spawn
        self.px = spawn[0] * PX
        self.py = spawn[1] * PX
        self.facing = "down"
        self.walk_timer = 0.0
        self.frame = 0
        self.cam_x = 0.0
        self.cam_y = 0.0
        self.update_camera(1.0)

    def set_banner(self, text, seconds=4.5):
        self.banner = text
        self.banner_timer = seconds

    def map_w(self):
        return len(self.map[0]) * PX

    def map_h(self):
        return len(self.map) * PX

    def tile_at(self, tx, ty):
        if ty < 0 or ty >= len(self.map) or tx < 0 or tx >= len(self.map[0]):
            return "#"
        return self.map[ty][tx]

    def solid(self, tx, ty):
        ch = self.tile_at(tx, ty)
        if ch == "D":
            return not self.door_open
        return ch in "#C"

    def blocked(self, x, y):
        box = pygame.Rect(int(x) + 12, int(y) + 24, PX - 24, PX - 28)
        left = box.left // PX
        right = (box.right - 1) // PX
        top = box.top // PX
        bottom = (box.bottom - 1) // PX
        for ty in range(top, bottom + 1):
            for tx in range(left, right + 1):
                if self.solid(tx, ty):
                    return True
        return False

    def player_rect(self):
        return pygame.Rect(int(self.px), int(self.py), PX, PX)

    def foot_tile(self):
        return (int((self.px + PX / 2) // PX), int((self.py + PX * 0.75) // PX))

    # ------------------------------------------------------------- update

    def update(self, dt, keys):
        if self.state == "title":
            return
        if self.state == "win":
            self.win_timer += dt
            self.update_particles()
            return

        if self.banner_timer > 0.0:
            self.banner_timer -= dt
        if self.flash > 0.0:
            self.flash = max(0.0, self.flash - dt * 2.4)
        if self.shake > 0.0:
            self.shake = max(0.0, self.shake - dt * 28.0)
        if self.stun > 0.0:
            self.stun = max(0.0, self.stun - dt)

        for drone in self.drones:
            drone.update(dt)

        if self.dialogue is not None:
            self.typed += dt * 38.0
            self.update_particles()
            return

        self.update_plates(dt)

        if self.stun <= 0.0:
            self.move_player(dt, keys)

        self.check_pickup()
        self.check_drones()
        self.check_exit()
        self.update_camera(dt)
        self.update_particles()

    def move_player(self, dt, keys):
        speed = 200.0 * dt
        dx = 0.0
        dy = 0.0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= speed
            self.facing = "left"
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += speed
            self.facing = "right"
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= speed
            self.facing = "up"
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += speed
            self.facing = "down"

        moving = dx != 0.0 or dy != 0.0
        if not self.blocked(self.px + dx, self.py):
            self.px += dx
        if not self.blocked(self.px, self.py + dy):
            self.py += dy

        if moving:
            self.walk_timer += dt
            if self.walk_timer > 0.16:
                self.walk_timer = 0.0
                self.frame = 1 - self.frame
            self.step_timer -= dt
            if self.step_timer <= 0.0:
                self.step_timer = 0.32
                self.audio.play("step")
        else:
            self.frame = 0

    def update_plates(self, dt):
        if self.room != 2 or self.door_open:
            return

        lit = [t for t in self.plates if self.plates[t]]
        if lit and self.plate_timer > 0.0:
            self.plate_timer -= dt
            if self.plate_timer <= 0.0:
                self.reset_plates(timeout=True)
                return

        tile = self.foot_tile()
        if tile in self.plates and not self.plates[tile]:
            self.plates[tile] = True
            count = len([t for t in self.plates if self.plates[t]])
            self.audio.play_plate(count - 1)
            self.burst(tile[0] * PX + PX / 2, tile[1] * PX + PX / 2, C_GOOD, 12)
            if count == 1:
                self.plate_timer = PLATE_WINDOW
            if count == len(self.plates):
                self.door_open = True
                self.plate_timer = 0.0
                self.shake = 9.0
                self.audio.play("unlock")
                self.set_banner("VAULT OPEN. GO SOUTH.", 3.5)

    def reset_plates(self, timeout=False):
        for tile in self.plates:
            self.plates[tile] = False
        self.plate_timer = 0.0
        if timeout:
            self.audio.play("timeout")
            self.set_banner("TOO SLOW. PLATES RESET.", 2.5)

    def check_pickup(self):
        if self.room != 1 or self.has_key:
            return
        kx = ROOM_ONE_KEY[0] * PX
        ky = ROOM_ONE_KEY[1] * PX
        if self.player_rect().colliderect(pygame.Rect(kx, ky, PX, PX)):
            self.has_key = True
            self.door_open = True
            self.shake = 7.0
            self.audio.play("pickup")
            self.burst(kx + PX / 2, ky + PX / 2, (255, 205, 70))
            self.set_banner("KEY FOUND. THE SOUTH DOOR IS OPEN.", 3.5)

    def check_drones(self):
        if self.stun > 0.0:
            return
        box = self.player_rect().inflate(-16, -16)
        for drone in self.drones:
            if box.colliderect(drone.rect()):
                self.attempts += 1
                self.stun = DRONE_STUN
                self.flash = 1.0
                self.shake = 11.0
                self.audio.play("hit")
                self.burst(self.px + PX / 2, self.py + PX / 2, C_ALERT, 22)
                self.px = self.spawn[0] * PX
                self.py = self.spawn[1] * PX
                self.reset_plates()
                self.set_banner("SPOTTED. BACK TO THE ENTRANCE.", 2.5)
                return

    def check_exit(self):
        tx, ty = self.foot_tile()
        if self.tile_at(tx, ty) == "D" and self.door_open:
            if self.room == 1:
                self.audio.play("unlock")
                self.enter_room(2)
            elif self.room == 2:
                self.audio.play("unlock")
                self.enter_room(3)
            return
        if self.room == 3:
            term = pygame.Rect(ROOM_THREE_TERMINAL[0] * PX,
                               ROOM_THREE_TERMINAL[1] * PX, PX, PX + 20)
            if self.player_rect().colliderect(term):
                self.state = "win"
                self.shake = 10.0
                self.audio.play("win")
                self.burst(term.centerx, term.centery, C_GOOD, 40)

    def update_camera(self, dt):
        target_x = self.px + PX / 2 - SCREEN_W / 2
        target_y = self.py + PX / 2 - SCREEN_H / 2
        target_x = max(0, min(target_x, self.map_w() - SCREEN_W))
        target_y = max(0, min(target_y, self.map_h() - SCREEN_H))
        self.cam_x += (target_x - self.cam_x) * min(1.0, dt * 6.0)
        self.cam_y += (target_y - self.cam_y) * min(1.0, dt * 6.0)

    def update_particles(self):
        for p in self.particles:
            p.update()
        self.particles = [p for p in self.particles if p.life > 0]

    def burst(self, x, y, colour, count=18):
        for i in range(count):
            angle = (i / float(count)) * math.pi * 2.0
            speed = 1.6 + (i % 4) * 0.6
            self.particles.append(Particle(
                x, y,
                math.cos(angle) * speed,
                math.sin(angle) * speed - 1.4,
                26 + (i % 7) * 3,
                colour))

    # ------------------------------------------------------------- input

    def interact(self):
        if self.state == "title":
            self.state = "play"
            self.audio.play("blip")
            return
        if self.state == "win":
            return

        if self.dialogue is not None:
            full = self.dialogue[self.dialogue_line]
            if self.typed < len(full):
                self.typed = len(full)
                return
            self.dialogue_line += 1
            self.typed = 0.0
            self.audio.play("blip")
            if self.dialogue_line >= len(self.dialogue):
                self.dialogue = None
            return

        if self.room != 1:
            return

        nx = ROOM_ONE_NPC[0] * PX
        ny = ROOM_ONE_NPC[1] * PX
        if self.player_rect().colliderect(pygame.Rect(nx - 40, ny - 40, PX + 80, PX + 80)):
            self.start_dialogue(DIALOGUE_HAS_KEY if self.has_key else DIALOGUE_LOCKED)
            return

        ox = ROOM_ONE_NOTE[0] * PX
        oy = ROOM_ONE_NOTE[1] * PX
        if self.player_rect().colliderect(pygame.Rect(ox - 30, oy - 30, PX + 60, PX + 60)):
            self.read_note = True
            self.start_dialogue(DIALOGUE_NOTE)

    def start_dialogue(self, lines):
        self.dialogue = lines
        self.dialogue_line = 0
        self.typed = 0.0
        self.audio.play("blip")

    # ------------------------------------------------------------- draw

    def draw(self):
        self.screen.fill(C_BG)
        if self.state == "title":
            self.draw_title()
            return

        ox = int(self.cam_x)
        oy = int(self.cam_y)
        if self.shake > 0.0:
            ox += int(math.sin(pygame.time.get_ticks() * 0.09) * self.shake)
            oy += int(math.cos(pygame.time.get_ticks() * 0.11) * self.shake)

        first_x = max(0, ox // PX)
        last_x = min(len(self.map[0]) - 1, (ox + SCREEN_W) // PX)
        first_y = max(0, oy // PX)
        last_y = min(len(self.map) - 1, (oy + SCREEN_H) // PX)

        for ty in range(first_y, last_y + 1):
            for tx in range(first_x, last_x + 1):
                ch = self.map[ty][tx]
                if ch == "D":
                    art = self.tiles["O"] if self.door_open else self.tiles["D"]
                elif ch == "p":
                    art = self.tiles["P"] if self.plates.get((tx, ty)) else self.tiles["p"]
                elif ch in self.tiles:
                    art = self.tiles[ch]
                else:
                    art = self.tiles["."]
                self.screen.blit(art, (tx * PX - ox, ty * PX - oy))

        if self.room == 1:
            if not self.has_key:
                bob = math.sin(pygame.time.get_ticks() * 0.005) * 4
                self.screen.blit(self.key_sprite,
                                 (ROOM_ONE_KEY[0] * PX - ox, ROOM_ONE_KEY[1] * PX - oy + bob))
            idx = 1 if (pygame.time.get_ticks() // 500) % 2 == 0 else 0
            self.screen.blit(self.npc_frames[idx],
                             (ROOM_ONE_NPC[0] * PX - ox, ROOM_ONE_NPC[1] * PX - oy))
            self.screen.blit(self.note_sprite,
                             (ROOM_ONE_NOTE[0] * PX - ox, ROOM_ONE_NOTE[1] * PX - oy))

        if self.room == 3:
            glow = 40 + int(math.sin(pygame.time.get_ticks() * 0.004) * 25)
            gx = ROOM_THREE_TERMINAL[0] * PX - ox
            gy = ROOM_THREE_TERMINAL[1] * PX - oy
            halo = pygame.Surface((PX * 3, PX * 3), pygame.SRCALPHA)
            pygame.draw.circle(halo, (90, 220, 150, glow), (PX * 3 // 2, PX * 3 // 2), PX)
            self.screen.blit(halo, (gx - PX, gy - PX))
            self.screen.blit(self.terminal_sprite, (gx, gy))

        for drone in self.drones:
            beam = pygame.Surface((PX, PX * 2), pygame.SRCALPHA)
            pygame.draw.polygon(beam, (255, 95, 105, 40),
                                [(PX // 2, 0), (PX, PX * 2), (0, PX * 2)])
            self.screen.blit(beam, (int(drone.x) - ox, int(drone.y) - oy))
            self.screen.blit(self.drone_frames[drone.frame],
                             (int(drone.x) - ox, int(drone.y) - oy))

        if self.stun <= 0.0 or (pygame.time.get_ticks() // 80) % 2 == 0:
            art = self.player_frames[self.facing][self.frame]
            self.screen.blit(art, (int(self.px) - ox, int(self.py) - oy))

        for p in self.particles:
            alpha = max(0, int(255 * (p.life / float(p.max_life))))
            size = max(2, int(6 * (p.life / float(p.max_life))))
            surf = pygame.Surface((size, size), pygame.SRCALPHA)
            surf.fill((p.colour[0], p.colour[1], p.colour[2], alpha))
            self.screen.blit(surf, (int(p.x) - ox, int(p.y) - oy))

        if self.flash > 0.0:
            veil = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
            veil.fill((255, 60, 70, int(90 * self.flash)))
            self.screen.blit(veil, (0, 0))

        self.draw_hud()
        if self.banner_timer > 0.0:
            self.draw_banner()
        if self.dialogue is not None:
            self.draw_dialogue()
        if self.state == "win":
            self.draw_win()

    def draw_hud(self):
        label = "KEY: FOUND" if self.has_key else "KEY: MISSING"
        colour = (255, 205, 70) if self.has_key else C_UI_DIM
        self.screen.blit(self.small_font.render(label, True, colour), (16, 14))
        self.screen.blit(self.small_font.render("ROOM " + str(self.room) + " OF 3", True, C_UI_DIM), (16, 38))

        if self.room == 2:
            lit = len([t for t in self.plates if self.plates[t]])
            plate_colour = C_GOOD if self.door_open else C_UI
            self.screen.blit(self.small_font.render(
                "PLATES " + str(lit) + " OF 3", True, plate_colour), (16, 62))
            if self.plate_timer > 0.0:
                width = int(220 * (self.plate_timer / PLATE_WINDOW))
                pygame.draw.rect(self.screen, (40, 44, 62), (16, 88, 220, 12))
                bar_colour = C_ALERT if self.plate_timer < 3.0 else C_GOOD
                pygame.draw.rect(self.screen, bar_colour, (16, 88, width, 12))
                pygame.draw.rect(self.screen, (90, 96, 120), (16, 88, 220, 12), 1)

        hint = "ARROWS OR WASD TO MOVE     SPACE TO TALK AND READ"
        self.screen.blit(self.small_font.render(hint, True, (90, 95, 118)), (16, SCREEN_H - 30))

    def draw_banner(self):
        text = self.small_font.render(self.banner, True, C_UI)
        pad = 14
        box = pygame.Rect(SCREEN_W // 2 - text.get_width() // 2 - pad, 20,
                          text.get_width() + pad * 2, text.get_height() + pad)
        panel = pygame.Surface((box.width, box.height), pygame.SRCALPHA)
        panel.fill((C_BOX[0], C_BOX[1], C_BOX[2], 225))
        self.screen.blit(panel, box.topleft)
        pygame.draw.rect(self.screen, C_BOX_EDGE, box, 1)
        self.screen.blit(text, (box.left + pad, box.top + pad // 2))

    def draw_dialogue(self):
        box = pygame.Rect(40, SCREEN_H - 170, SCREEN_W - 80, 130)
        panel = pygame.Surface((box.width, box.height), pygame.SRCALPHA)
        panel.fill((C_BOX[0], C_BOX[1], C_BOX[2], 238))
        self.screen.blit(panel, box.topleft)
        pygame.draw.rect(self.screen, C_BOX_EDGE, box, 2)

        portrait = pygame.Rect(box.left + 16, box.top + 16, 74, 74)
        pygame.draw.rect(self.screen, (30, 34, 52), portrait)
        pygame.draw.rect(self.screen, C_BOX_EDGE, portrait, 1)
        is_note = self.dialogue is DIALOGUE_NOTE
        face = pygame.transform.scale(self.note_sprite if is_note else self.npc_frames[0], (66, 66))
        self.screen.blit(face, (portrait.left + 4, portrait.top + 4))

        name = self.small_font.render("NOTE" if is_note else "KEEPER", True, C_BOX_EDGE)
        self.screen.blit(name, (portrait.right + 18, box.top + 14))

        full = self.dialogue[self.dialogue_line]
        shown = full[:int(self.typed)]
        self.screen.blit(self.font.render(shown, True, C_UI), (portrait.right + 18, box.top + 46))

        if self.typed >= len(full) and (pygame.time.get_ticks() // 400) % 2 == 0:
            self.screen.blit(self.small_font.render("SPACE", True, C_UI_DIM),
                             (box.right - 90, box.bottom - 32))

    def draw_title(self):
        title = self.big_font.render("THE LAST TERMINAL", True, C_UI)
        self.screen.blit(title, (SCREEN_W // 2 - title.get_width() // 2, 160))
        sub = self.font.render("A peek of what is to come...", True, C_UI_DIM)
        self.screen.blit(sub, (SCREEN_W // 2 - sub.get_width() // 2, 226))

        self.screen.blit(self.font.render("BUILT FOR:", True, C_UI_DIM), (SCREEN_W // 2 - 170, 330))
        blank = pygame.Rect(SCREEN_W // 2 - 60, 326, 230, 34)
        # pygame.draw.rect(self.screen, (60, 66, 92), blank, 1)
        self.screen.blit(self.font.render("ICD2O @ BVG", True, (70, 78, 106)),
                          (blank.left + 12, blank.top + 4))

        if (pygame.time.get_ticks() // 500) % 2 == 0:
            start = self.font.render("PRESS SPACE", True, C_BOX_EDGE)
            self.screen.blit(start, (SCREEN_W // 2 - start.get_width() // 2, 430))

        foot = self.small_font.render("ICD2O    BAYVIEW GLEN    2026 TO 2027", True, (66, 72, 96))
        self.screen.blit(foot, (SCREEN_W // 2 - foot.get_width() // 2, SCREEN_H - 60))

    def draw_win(self):
        veil = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
        veil.fill((8, 10, 18, 210))
        self.screen.blit(veil, (0, 0))
        one = self.big_font.render("END OF THE SLICE", True, C_UI)
        self.screen.blit(one, (SCREEN_W // 2 - one.get_width() // 2, 190))
        two = self.font.render("Three rooms, two puzzles, three drones", True, C_UI_DIM)
        self.screen.blit(two, (SCREEN_W // 2 - two.get_width() // 2, 262))
        caught = "Caught " + str(self.attempts) + (" time" if self.attempts == 1 else " times")
        self.screen.blit(self.font.render(caught, True, C_UI_DIM),
                         (SCREEN_W // 2 - self.font.render(caught, True, C_UI_DIM).get_width() // 2, 300))
        three = self.font.render("Yours ships in May", True, C_BOX_EDGE)
        self.screen.blit(three, (SCREEN_W // 2 - three.get_width() // 2, 350))
        four = self.small_font.render("R TO PLAY AGAIN", True, (90, 95, 118))
        self.screen.blit(four, (SCREEN_W // 2 - four.get_width() // 2, 420))


# ----------------------------------------------------------------- main

def main():
    pygame.init()
    audio = Audio()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("The Last Terminal: ICD2O")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 30)
    big_font = pygame.font.Font(None, 64)
    small_font = pygame.font.Font(None, 24)

    game = Game(screen, audio, font, big_font, small_font)
    fullscreen = False

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        if dt > 0.05:
            dt = 0.05

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in (pygame.K_SPACE, pygame.K_e, pygame.K_RETURN):
                    game.interact()
                elif event.key == pygame.K_r:
                    game.reset()
                    game.state = "play"
                elif event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
                    game.screen = screen

        keys = pygame.key.get_pressed()
        game.update(dt, keys)
        game.draw()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()