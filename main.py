import pygame
import math

pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Haxball Python Edition")

# 색상 및 물리
GREEN, WHITE, RED = (67, 142, 62), (255, 255, 255), (229, 57, 53)
FPS = 60
clock = pygame.time.Clock()

player = {"x": 150, "y": 200, "radius": 15, "speed": 5}
ball = {"x": 400, "y": 200, "radius": 10, "dx": 0, "dy": 0, "friction": 0.98}

running = True
while running:
    screen.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    # 조작
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]: player["x"] -= player["speed"]
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: player["x"] += player["speed"]
    if keys[pygame.K_UP] or keys[pygame.K_w]: player["y"] -= player["speed"]
    if keys[pygame.K_DOWN] or keys[pygame.K_s]: player["y"] += player["speed"]

    # 충돌 및 물리
    dist = math.hypot(ball["x"] - player["x"], ball["y"] - player["y"])
    if dist < player["radius"] + ball["radius"]:
        angle = math.atan2(ball["y"] - player["y"], ball["x"] - player["x"])
        ball["dx"], ball["dy"] = math.cos(angle) * 7, math.sin(angle) * 7

    ball["x"] += ball["dx"]; ball["y"] += ball["dy"]
    ball["dx"] *= ball["friction"]; ball["dy"] *= ball["friction"]

    # 그리기
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT), 5)
    pygame.draw.circle(screen, RED, (int(player["x"]), int(player["y"])), player["radius"])
    pygame.draw.circle(screen, WHITE, (int(ball["x"]), int(ball["y"])), ball["radius"])

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
