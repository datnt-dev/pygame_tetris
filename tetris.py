import pygame
import random

pygame.font.init()

s_width = 800
s_height = 700
play_width = 300
play_height = 600
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height = play_height

# Shape

S = [
    [
        \'.....\',
        \'.....\',
        \'..00.\',
        \'.00..\',
        \'.....\',
    ],
    [
        \'.....\',
        \'..0..\',
        \'..00.\',
        \'...0.\',
        \'.....\',
    ]
]

Z = [
    [
        \'.....\',
        \'.....\',
        \'.00..\',
        \'..00.\',
        \'.....\',
    ],
    [
        \'.....\',
        \'..0..\',
        \'.00..\',
        \'.0...\',
        \'.....\',
    ]
]

I = [
    [
        \'..0..\',
        \'..0..\',
        \'..0..\',
        \'..0..\',
        \'.....\',
    ],
    [
        \'.....\',
        \'0000.\',
        \'.....\',
        \'.....\',
        \'.....\',
    ]
]

O = [
    [
        \'.....\',
        \'.....\',
        \'.00..\',
        \'.00..\',
        \'.....\',
    ]
]

J = [
    [
        \'.....\',
        \'.0...\',
        \'.000.\',
        \'.....\',
        \'.....\',
    ],
    [
        \'.....\',
        \'.00..\',
        \'.0...\',
        \'.0...\',
        \'.....\',
    ],
    [
        \'.....\',
        \'.....\',
        \'.000.\',
        \'...0.\',
        \'.....\',
    ],
    [
        \'.....\',
        \'..0..\',
        \'..0..\',
        \'.00..\',
        \'.....\',
    ]
],

L = [
    [
        \'.....\',
        \'...0.\',
        \'.000.\',
        \'.....\',
        \'.....\',
    ],
    [
        \'.....\',
        \'..0..\',
        \'..0..\',
        \'..00.\',
        \'.....\',
    ],
    [
        \'.....\',
        \'.....\',
        \'.000.\',
        \'.0...\',
        \'.....\',
    ],
    [
        \'.....\',
        \'.00..\',
        \'..0..\',
        \'..0..\',
        \'.....\',
    ]
]

T = [
    [
        \'.....\',
        \'..0..\',
        \'.000.\',
        \'.....\',
        \'.....\',
    ],
    [
        \'.....\',
        \'..0..\',
        \'..00.\',
        \'..0..\',
        \'.....\',
    ],
    [
        \'.....\',
        \'.....\',
        \'.000.\',
        \'..0..\',
        \'.....\',
    ],
    [
        \'.....\',
        \'..0..\',
        \'.00..\',
        \'..0..\',
        \'.....\',
    ]
]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


class Piece():
    rows = 20 # y
    columns = 10 # x

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shape.index(shape)]
        self.rotation = 0

def create_crid(locked_position={}):
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_position:
                c = locked_position[(j, i)]
                grid[i][j] = c
    return grid

def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == \'0\':
                positions.append((shape.x + j, shape.y + i))
    
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions
