import os
import threading
import pygame
import random
from appdirs import system


# Ensure relative paths to resources
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = system._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Dictionary to track server statuses
status_dict = {}

# Function to ping a server and update its status
def ping_server_os(host):
    response = os.system(f"ping -c 4 {host}")
    if response == 0:
        print(f"{host} is up")
        status_dict[host] = ["up"]
    else:
        print(f"{host} is down")
        status_dict[host] = ["down"]

# Call a function periodically
def call_function_periodically(interval, func, *args):
    func(*args)
    timer = threading.Timer(interval, call_function_periodically, [interval, func] + list(args))
    timer.start()
    print(status_dict)

#call_function_periodically(2600, ping_server_os, "orleansda.com")
#call_function_periodically(2600, ping_server_os, "opso.us")

#test organizations
ping_server_os("orleansda.com")
ping_server_os("opso.us")

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Setup screen
screen = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()
running = True

# Player initial position
dt = 0
x = 750
y = 765

# Load images using resource_path
CDC = pygame.image.load(resource_path('CDC.png'))
CDC_b = pygame.image.load(resource_path('CDC b.png'))
CITY_ITI = pygame.image.load(resource_path('CIITY ITI.png'))
CITY_ITI_b = pygame.image.load(resource_path('CITY ITI b.png'))
JJIC = pygame.image.load(resource_path('JJIC.png'))
JJIC_b = pygame.image.load(resource_path('JJIC b.png'))
JUVI = pygame.image.load(resource_path('JUVI.png'))
JUVI_b = pygame.image.load(resource_path('JUVI b.png'))
NOPD = pygame.image.load(resource_path('NOPD.png'))
NOPD_b = pygame.image.load(resource_path('NOPD b.png'))
OCJC = pygame.image.load(resource_path('OCJC.png'))
OCJC_b = pygame.image.load(resource_path('OCJC b.png'))
OPDA = pygame.image.load(resource_path('OPDA.png'))
OPDA_b = pygame.image.load(resource_path('OPDA b.png'))
OPSO = pygame.image.load(resource_path('OPSO.png'))
OPSO_b = pygame.image.load(resource_path('OPSO b.png'))
OPD = pygame.image.load(resource_path('OPD.png'))
OPD_b = pygame.image.load(resource_path('OPD b.png'))
MUNC = pygame.image.load(resource_path('MUNC.png'))
MUNC_b = pygame.image.load(resource_path('MUNC b.png'))
b2 = pygame.image.load(resource_path('b2.png'))
b3 = pygame.image.load(resource_path('b3.png'))
green1 = pygame.image.load(resource_path("green1.png"))

badguy = pygame.image.load(resource_path("badguy.png")).convert_alpha()
ghost = pygame.image.load(resource_path("logo.png")).convert_alpha()
slimer_sprite = [pygame.image.load(resource_path(f"slimer{i}.png")).convert_alpha() for i in range(1, 7)]
grey_sprite = [pygame.image.load(resource_path(f"grey{i}.png")).convert_alpha() for i in range(1, 9)]
blue_sprite = [pygame.image.load(resource_path(f"blue{i}.png")).convert_alpha() for i in range(1, 11)]

slimer_death = [pygame.image.load(resource_path("slimer d1.png")).convert_alpha(), pygame.image.load(resource_path("slimer d2.png")).convert_alpha(),
                pygame.image.load(resource_path("slimer d3.png")).convert_alpha(), pygame.image.load(resource_path("slimer d4.png")).convert_alpha(),
                pygame.image.load(resource_path("last.png")).convert_alpha()]
grey_death = [pygame.image.load(resource_path("grey d1.png")).convert_alpha(), pygame.image.load(resource_path("grey d2.png")).convert_alpha(),
              pygame.image.load(resource_path("last.png")).convert_alpha()]
blue_death = [pygame.image.load(resource_path("blue d1.png")), pygame.image.load(resource_path("blue d2.png")), pygame.image.load(resource_path("blue d3.png")),pygame.image.load(resource_path("blue d4.png")), pygame.image.load(resource_path("last.png"))]

value_grey = 0
value_blue = 0
value_slimer = 0
value_death = 0
value_grey_death = 0

# Playlist for background music
playlist = [resource_path("01 Ghostbusters.mp3"),
            resource_path("02 Cleanin' Up the Town.mp3"),
            resource_path("03 Savin' the Day.mp3"),
            resource_path("04 In the Name of Love.mp3"),
            resource_path("05 I Can Wait Forever.mp3"),
            resource_path("06 Hot Night.mp3"),
            resource_path("07 Magic.mp3"),
            resource_path("08 Main Title Theme (Ghostbusters).mp3"),
            resource_path("11 Disco Inferno.mp3")]

# Set music volume and start playing
pygame.mixer.music.set_volume(0.7)

def play_next_song():
    if playlist:
        next_song = playlist.pop(0)
        pygame.mixer.music.load(next_song)
        pygame.mixer.music.play()
        playlist.append(next_song)  # Re-add the song to the end of the playlist

def check_music_end():
    if not pygame.mixer.music.get_busy():
        play_next_song()

play_next_song()

# Scaling and transformation of images
imagesize = (110, 110)
buildingsize = (176, 135)

ghost = pygame.transform.scale(ghost, imagesize)
slimer_sprite = [pygame.transform.scale2x(img) for img in slimer_sprite]
grey_sprite = [pygame.transform.scale2x(img) for img in grey_sprite]
badguy = pygame.transform.scale(badguy, imagesize)
slimer_death = [pygame.transform.scale2x(img) for img in slimer_death]
grey_death = [pygame.transform.scale2x(img) for img in grey_death]
blue_sprite = [pygame.transform.scale2x(img) for img in blue_sprite]
blue_death = [pygame.transform.scale2x(img) for img in blue_death]

CDC = pygame.transform.scale(CDC, buildingsize)
CDC_b = pygame.transform.scale(CDC_b, buildingsize)
CITY_ITI = pygame.transform.scale(CITY_ITI, buildingsize)
CITY_ITI_b = pygame.transform.scale(CITY_ITI_b, buildingsize)
JJIC = pygame.transform.scale(JJIC, buildingsize)
JJIC_b = pygame.transform.scale(JJIC_b, buildingsize)
JUVI = pygame.transform.scale(JUVI, buildingsize)
JUVI_b = pygame.transform.scale(JUVI_b, buildingsize)
NOPD = pygame.transform.scale(NOPD, buildingsize)
NOPD_b = pygame.transform.scale(NOPD_b, buildingsize)
OCJC = pygame.transform.scale(OCJC, buildingsize)
OCJC_b = pygame.transform.scale(OCJC_b, buildingsize)
OPDA = pygame.transform.scale(OPDA, buildingsize)
OPDA_b = pygame.transform.scale(OPDA_b, buildingsize)
OPSO = pygame.transform.scale(OPSO, buildingsize)
OPSO_b = pygame.transform.scale(OPSO_b, buildingsize)
OPD = pygame.transform.scale(OPD, buildingsize)
OPD_b = pygame.transform.scale(OPD_b, buildingsize)
MUNC = pygame.transform.scale(MUNC, buildingsize)
MUNC_b = pygame.transform.scale(MUNC_b, buildingsize)
b2 = pygame.transform.scale(b2, buildingsize)
b3 = pygame.transform.scale(b3, buildingsize)
green1 = pygame.transform.scale(green1, imagesize)

# Define building rectangles for collision with player and enimes
buildings = [
    pygame.Rect(120, 0, buildingsize[0], buildingsize[1]),
    pygame.Rect(712, 0, buildingsize[0], buildingsize[1]),
    pygame.Rect(416, 0, buildingsize[0], buildingsize[1]),
    pygame.Rect(1008, 0, buildingsize[0], buildingsize[1]),
    pygame.Rect(1304, 0, buildingsize[0], buildingsize[1]),
    pygame.Rect(120, 255, buildingsize[0], buildingsize[1]),
    pygame.Rect(416, 255, buildingsize[0], buildingsize[1]),
    pygame.Rect(712, 255, buildingsize[0], buildingsize[1]),
    pygame.Rect(1008, 255, buildingsize[0], buildingsize[1]),
    pygame.Rect(1304, 255, buildingsize[0], buildingsize[1]),
    pygame.Rect(120, 510, buildingsize[0], buildingsize[1]),
    pygame.Rect(416, 510, buildingsize[0], buildingsize[1]),
    pygame.Rect(712, 510, buildingsize[0], buildingsize[1]),
    pygame.Rect(1008, 510, buildingsize[0], buildingsize[1]),
    pygame.Rect(1304, 510, buildingsize[0], buildingsize[1]),
    pygame.Rect(120, 765, buildingsize[0], buildingsize[1]),
    pygame.Rect(416, 765, buildingsize[0], buildingsize[1]),
    pygame.Rect(1008, 765, buildingsize[0], buildingsize[1]),
    pygame.Rect(1304, 765, buildingsize[0], buildingsize[1])
]

# Function to generate random positions for bad guys
def generate_badguy_positions(num_positions, buildings, screen_size):
    positions = []
    for _ in range(num_positions):
        while True:
            x = random.randint(0, screen_size[0] - imagesize[0])
            y = random.randint(0, screen_size[1] - imagesize[1])
            new_rect = pygame.Rect(x, y, imagesize[0], imagesize[1])

            if any(new_rect.colliderect(building) for building in buildings):
                continue

            if any(new_rect.colliderect(pygame.Rect(pos[0], pos[1], imagesize[0], imagesize[1])) for pos in positions):
                continue

            positions.append((x, y))
            break
    return positions


badguys_pos = generate_badguy_positions(10, buildings, screen.get_size())
slimer_pos = generate_badguy_positions(1, buildings, screen.get_size())[0]
grey_pos = generate_badguy_positions(1, buildings, screen.get_size())[0]
blue_pos = generate_badguy_positions(1, buildings, screen.get_size())[0]

badguys_alive = [True] * 10
badguys_attack_initiated = [False] * 10
badguys_attack_timer = [0] * 10


slimer_alive = True
slimer_attack_initiated = False
slimer_attack_timer = 0


grey_alive = True
grey_attack_initiated = False
grey_attack_timer = 0


blue_alive = True
blue_attack_initiated = False
blue_attack_timer = 0

# Load and display producer screen
producer_image = pygame.image.load(resource_path('Sith arts.png'))  # Replace with the actual path to your producer image
producer_image = pygame.transform.scale(producer_image, (800, 600))  # Adjust size as needed

def display_producer_screen(duration=3):
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < duration * 1000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill("black")
        screen.blit(producer_image, (400, 150))  # Adjust position as needed
        pygame.display.flip()
        clock.tick(30)

# Function to display game rules
def display_rules_screen():
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    rules_text = [
        "Rules of the Game:",
        "1. Use WASD keys to move the ghostbuster.",
        "2. Press SPACE to attack the ghost.",
        "If the building is green the server is up and red if the server is down ",
        "Press ENTER to start the game.",
        "Click the x in the top right corner to exit the game.",
        "(Game is in early production)"

    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        #rules screen
        screen.fill("black")
        y_offset = 100

        for line in rules_text:
            text_surface = font.render(line, True, "white") if line.startswith("Rules") else small_font.render(line,
                                                                                                               True,
                                                                                                               "white")
            screen.blit(text_surface, (100, y_offset))
            y_offset += 50

        pygame.display.flip()
        clock.tick(30)

# Display producer screen and rules
display_producer_screen()
display_rules_screen()

fade_duration = 2.0  # seconds
fade_step = 255 / (fade_duration * 10)  # assuming 10 frames per second

#values for the enemies to fade in
grey_alpha = 0
slimer_alpha = 0
badguy_alpha = 0
blue_alpha = 0

start_ticks = pygame.time.get_ticks()  # get the start ticks for the game

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # in seconds

    #fade enemies into the game
    if elapsed_time < fade_duration:
        grey_alpha = min(255, grey_alpha + fade_step)
        slimer_alpha = min(255, slimer_alpha + fade_step)
        badguy_alpha = min(255, badguy_alpha + fade_step)
        blue_alpha = min(255, blue_alpha + fade_step)

    else:
        grey_alpha = slimer_alpha = badguy_alpha = blue_alpha = 255

    for img in grey_sprite:
        img.set_alpha(grey_alpha)
    for img in slimer_sprite:
        img.set_alpha(slimer_alpha)
    for img in blue_sprite:
        img.set_alpha(blue_alpha)
    badguy.set_alpha(badguy_alpha)


    if value_slimer >= len(slimer_sprite):
        value_slimer = 0
    if value_death >= len(slimer_death):
        value_death = 0
    if value_grey >= len(grey_sprite):
        value_grey = 0
    if value_grey_death >= len(grey_death):
        value_grey_death = 0
    if value_blue >= len(blue_sprite):
        value_blue = 0

    blue = blue_sprite[value_blue]
    blued = blue_death[value_death]
    grey = grey_sprite[value_grey]
    slimer = slimer_sprite[value_slimer]
    slimerd = slimer_death[value_death]
    greyd = grey_death[value_grey_death]

    screen.fill("teal")

    keys = pygame.key.get_pressed()
    # Player movement logic
    # Game rendering logic
    # Event handling logic

    new_x, new_y = x, y
    if keys[pygame.K_w]:
        new_y -= 200 * dt
    if keys[pygame.K_s]:
        new_y += 200 * dt
    if keys[pygame.K_a]:
        new_x -= 200 * dt
    if keys[pygame.K_d]:
        new_x += 200 * dt

    ghost_rect = pygame.Rect(new_x, new_y, 90, 90)

    #collision handling so player isn't going throuh buildings
    collision = False
    for building in buildings:
        if ghost_rect.colliderect(building):
            collision = True
            break

    if not collision:
        x, y = new_x, new_y

    #use ther server status of organizations from the dict to determine if the building should be green or red
    for key in status_dict:
        if key == 'orleansda.com':
            if status_dict[key] == ['up']:
                screen.blit(OPDA, (120, 0))
            else:
                screen.blit(OPDA_b, (120, 0))
        if key == 'opso.us':
            if status_dict[key] == ['up']:
                screen.blit(OPSO, (712, 0))
            else:
                screen.blit(OPSO_b, (712, 0))

    #other organizations, still waiitng on permission from organizations to ping them and they respond back
    screen.blit(b2, (416, 0))
    screen.blit(NOPD, (1008, 0))
    screen.blit(b3, (1304, 0))

    screen.blit(b2, (120, 255))
    screen.blit(MUNC, (416, 255))
    screen.blit(JJIC, (712, 255))
    screen.blit(b3, (1008, 255))
    screen.blit(CDC, (1304, 255))

    screen.blit(OCJC, (120, 510))
    screen.blit(b2, (416, 510))
    screen.blit(b3, (712, 510))
    screen.blit(b3, (1008, 510))
    screen.blit(JUVI, (1304, 510))

    screen.blit(b3, (120, 765))
    screen.blit(OPD, (416, 765))
    screen.blit(CITY_ITI, (1008, 765))
    screen.blit(b3, (1304, 765))

    screen.blit(ghost, (x, y))

    #death mechanic of ghosts
    if all(not alive for alive in badguys_alive):
        if grey_alive:
            screen.blit(grey, grey_pos)
        else:
            if grey_attack_initiated:
                if grey_attack_timer < len(grey_death):
                    screen.blit(greyd, grey_pos)
                    grey_attack_timer += 1
                else:
                    grey_attack_initiated = False

    if all(not alive for alive in badguys_alive):
        if slimer_alive:
            screen.blit(slimer, slimer_pos)
        else:
            if slimer_attack_initiated:
                if slimer_attack_timer < len(slimer_death):
                    screen.blit(slimer_death[slimer_attack_timer], slimer_pos)
                    slimer_attack_timer += 1
                else:
                    slimer_attack_initiated = False

    if all(not alive for alive in badguys_alive):
        if blue_alive:
            screen.blit(blue, blue_pos)
        else:
            if blue_attack_initiated:
                if blue_attack_timer < len(blue_death):
                    screen.blit(blue_death[blue_attack_timer], blue_pos)
                    blue_attack_timer += 1
                else:
                    blue_attack_initiated = False

    for i, pos in enumerate(badguys_pos):
        if badguys_alive[i]:
            screen.blit(badguy, pos)
        else:
            if badguys_attack_initiated[i]:
                if badguys_attack_timer[i] < 1:
                    screen.blit(green1, pos)
                    badguys_attack_timer[i] += 1
                else:
                    badguys_attack_initiated[i] = False

    #mechanic to kill ghost using the space bar as attack, also checks to make sure all badguy ghosts are dead because the named ghost shouldn't appear before then
    if keys[pygame.K_SPACE]:
        slimer_rect = pygame.Rect(slimer_pos[0], slimer_pos[1], imagesize[0], imagesize[1])
        grey_rect = pygame.Rect(grey_pos[0], grey_pos[1], imagesize[0], imagesize[1])
        blue_rect = pygame.Rect(blue_pos[0], blue_pos[1], imagesize[0], imagesize[1])
        if all(not alive for alive in badguys_alive):
            if slimer_alive and ghost_rect.colliderect(slimer_rect):
                slimer_alive = False
                slimer_attack_initiated = True
                slimer_attack_timer = 0
        if all(not alive for alive in badguys_alive):
            if grey_alive and ghost_rect.colliderect(grey_rect):
                grey_alive = False
                grey_attack_initiated = True
                grey_attack_timer = 0
        for i, pos in enumerate(badguys_pos):
            badguy_rect = pygame.Rect(pos[0], pos[1], imagesize[0], imagesize[1])
            if badguys_alive[i] and ghost_rect.colliderect(badguy_rect):
                badguys_alive[i] = False
                badguys_attack_initiated[i] = True
                badguys_attack_timer[i] = 0
        if all(not alive for alive in badguys_alive):
            if blue_alive and ghost_rect.colliderect(blue_rect):
                blue_alive = False
                blue_attack_initiated = True
                blue_attack_timer = 0
    pygame.display.flip()

    dt = clock.tick(10) / 1000
    value_slimer += 1
    value_blue += 1
    value_grey += 1
    value_grey_death += 1
    value_death += 1

    check_music_end()
    pygame.time.wait(100)

pygame.quit()
