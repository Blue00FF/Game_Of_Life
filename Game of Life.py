import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

GRID_DIMENSION = 10
FRAMES = 10
UPDATE_INTERVAL = 50
SAVE_COUNT = 50


def cycle(frame, img, old_grid):
    new_grid = np.zeros((10, 10))
    for i in range(GRID_DIMENSION):
        for j in range(GRID_DIMENSION):
            nbr = neighbours(old_grid, i, j)
            if old_grid[i][j] == 1 and (nbr < 2 or nbr > 3):
                new_grid[i][j] = 0
            elif old_grid[i][j] == 0 or nbr == 3:
                new_grid[i][j] = 1
            else:
                new_grid[i][j] = old_grid[i][j]
    img.set_data(new_grid)
    old_grid = new_grid[:]
    return img,


def neighbours(old_grid, x, y):
    neighbour_sum = 0
    for i in (-1, 0, +1):
        for j in (-1, 0, +1):
            X = (x + i + GRID_DIMENSION) % GRID_DIMENSION
            Y = (y + j + GRID_DIMENSION) % GRID_DIMENSION
            if X != Y:
                neighbour_sum += old_grid[X][Y]
    return neighbour_sum


def main():
    grid = np.floor(np.random.rand(GRID_DIMENSION, GRID_DIMENSION) * 2)
    figure, axes = plt.subplots()
    image = axes.imshow(grid, interpolation="nearest")
    anim = FuncAnimation(figure, cycle, fargs=(image, grid))
    anim.save("game_of_life", fps=30, extra_args=['-vcodec', 'libx264'])
    plt.show()


if __name__ == "__main__":
    main()
