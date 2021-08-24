import pygame
import sys
import numpy as np

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('color_insta')

# インスタアイコン用RGB値
N = 256
R = np.linspace(500,255,N)
R2 = np.zeros(256) + 255
G = np.linspace(400,0,N)
for i in range(N):
    if G[i] >= 256:
        G[i] = 255

running = True
# メインループ
while running:
    screen.fill((255, 255, 255))

    # インスタアイコン
    for i in range(256):
        for j in range(256):
            if j >= 128:
                screen.fill((R[i]*(255-(1-i/512)*j)/N, G[i]*(255-j)/N, j), (272+i, 428-j, 1, 1))
            else:
                screen.fill((R2[i]*(255-i*j/512)/N, G[i]*(255-j)/N, j), (272+i, 428-j, 1, 1))
    
    pygame.draw.rect(screen, (255, 255, 255), (262, 163, 276, 276), 24, border_radius=72)
    pygame.draw.rect(screen, (255, 255, 255), (312, 213, 176, 176), 15, border_radius=49)
    pygame.draw.rect(screen, (255, 255, 255), (355, 256, 90, 90), 14, border_radius=98)
    pygame.draw.circle(screen, (255, 255, 255), (447, 254), 10)
    pygame.draw.rect(screen, (255, 255, 255), (262, 163, 276, 276), 24, border_radius=28)
    pygame.draw.rect(screen, (255, 255, 255), (262, 163, 276, 276), 24, border_radius=1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()  # pygameのウィンドウを閉じる
            sys.exit()  # システム終了
    pygame.display.update()  # 描画処理を実行