import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
game_speed = 20
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "ChickenWallpaper.png"))

# Dino
DINO_START = pygame.image.load(os.path.join(IMG_DIR, "ChickenWallpaper.png"))
DINO_DEAD = pygame.image.load(os.path.join(IMG_DIR, "Dino/ChickenDead.png"))

# Run
RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/ChickenRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/ChickenRun2.png")),
]
RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/ChickenRunShield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/ChickenRunShield2.png")),
]
RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunHammer1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunHammer2.png")),
]

# Duck
DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/ChickenDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/ChickenDuck2.png")),
]
DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckShield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckShield2.png")),
]
DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckHammer1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckHammer2.png")),
]

# Jump
JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/Jump/ChickenJump.png"))
JUMPING_SHIELD = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/Jump/ChickenJumpShield.png")
)
JUMPING_HAMMER = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/Jump/DinoJumpHammer.png")
)

# Obstacles
SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]
BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

# Doodads
CLOUD = pygame.image.load(os.path.join(IMG_DIR, "Other/Cloud.png"))

# Power ups
SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Other/Shield.png"))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Other/Hammer.png"))

BG = pygame.image.load(os.path.join(IMG_DIR, "Other/Track.png"))
HEART = pygame.image.load(os.path.join(IMG_DIR, "Other/SmallHeart.png"))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
