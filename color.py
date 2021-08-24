import pygame
import sys
import numpy as np

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('color')

# スペクトル用RGB値
N = 192
group0 = []
group1 = []
group2 = []
group3 = []
group4 = []
group5 = []
GR = [group0, group1, group2, group3, group4, group5]

for i in range(N):
    for j in range(6):
        if i+1 <= N * (j+1) // 6:
            GR[j].append(i+1)
            break

R = np.linspace(1,N,N)
G = np.linspace(1,N,N)
B = np.linspace(1,N,N)

for i in range(len(GR[0])):
    rgb = [255,0,0]
    rgb[1] = np.linspace(0, 255, len(GR[0])+2)[i+1]
    R[i] = rgb[0]
    G[i] = rgb[1]
    B[i] = rgb[2]

for i in range(len(GR[1])):
    rgb = [255,255,0]
    rgb[0] = np.linspace(255, 0, len(GR[1])+2)[i+1]
    j = len(GR[0])
    R[i+j] = rgb[0]
    G[i+j] = rgb[1]
    B[i+j] = rgb[2]

for i in range(len(GR[2])):
    rgb = [0,255,0]
    rgb[2] = np.linspace(0, 255, len(GR[2])+2)[i+1]
    j = len(GR[0]) + len(GR[1])
    R[i+j] = rgb[0]
    G[i+j] = rgb[1]
    B[i+j] = rgb[2]

for i in range(len(GR[3])):
    rgb = [0,255,255]
    rgb[1] = np.linspace(255, 0, len(GR[3])+2)[i+1]
    j = len(GR[0]) + len(GR[1]) + len(GR[2])
    R[i+j] = rgb[0]
    G[i+j] = rgb[1]
    B[i+j] = rgb[2]

for i in range(len(GR[4])):
    rgb = [0,0,255]
    rgb[0] = np.linspace(0, 255, len(GR[4])+2)[i+1]
    j = len(GR[0]) + len(GR[1]) + len(GR[2]) + len(GR[3])
    R[i+j] = rgb[0]
    G[i+j] = rgb[1]
    B[i+j] = rgb[2]
    
for i in range(len(GR[5])):
    rgb = [255,0,255]
    rgb[2] = np.linspace(255, 0, len(GR[5])+2)[i+1]
    j = len(GR[0]) + len(GR[1]) + len(GR[2]) + len(GR[3]) + len(GR[4])
    R[i+j] = rgb[0]
    G[i+j] = rgb[1]
    B[i+j] = rgb[2]

# 2方向グラデーション用RGB値
R2 = np.linspace(0,255,N)
G2 = np.linspace(255,0,N)
B2 = np.linspace(255,0,N)

running = True
# メインループ
while running:
    screen.fill((255, 255, 255))
    for i in range(N):
        # 純色スペクトル
        screen.fill((R[i], G[i], B[i]), (4*i+16, 260, 4, 100))
        # 全色スペクトル
        for j in range(N//2):
            # 黒 → 純色
            screen.fill((R[i]*2*j/N, G[i]*2*j/N, B[i]*2*j/N), (4*i+16, 30+j, 4, 1))
            # 純色 → 白
            screen.fill((R[i]+(255-R[i])*2*j/N, G[i]+(255-G[i])*2*j/N, B[i]+(255-B[i])*2*j/N), (4*i+16, 125+j, 4, 1))
        # グラデーション
        for j in range(N):
            screen.fill((R2[i], G2[i], j*256/N), (i+16, 400+j, 1, 1))
            screen.fill((R2[i], j*256/N, B2[i]), (i+282, 400+j, 1, 1))
            screen.fill((R2[i], (N-j-1)*256/N, j*256/N), (i+548, 400+j, 1, 1))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()  # pygameのウィンドウを閉じる
            sys.exit()  # システム終了
    pygame.display.update()  # 描画処理を実行