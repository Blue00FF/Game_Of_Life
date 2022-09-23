import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

GRID_DIMENSION = 100
FRAMES = 100
UPDATE_INTERVAL = 1000/60


def cycle(frame_number, img, old_grid):
    new_grid = old_grid.copy()
    for i in range(GRID_DIMENSION):
        for j in range(GRID_DIMENSION):
            nbr = neighbours(old_grid, i, j)
            if old_grid[i][j] == 1 and (nbr < 2 or nbr > 3):
                new_grid[i][j] = 0
            elif old_grid[i][j] == 0 and nbr == 3:
                new_grid[i][j] = 1
    img.set_data(new_grid)
    old_grid[:] = new_grid[:]
    return img


def neighbours(old_grid, x, y):
    neighbour_sum = 0
    for i in (-1, 0, +1):
        for j in (-1, 0, +1):
            X = (x + i + GRID_DIMENSION) % GRID_DIMENSION
            Y = (y + j + GRID_DIMENSION) % GRID_DIMENSION
            neighbour_sum += old_grid[X][Y]
    neighbour_sum -= old_grid[x][y]
    return neighbour_sum


def main():
    grid = np.floor(np.random.rand(GRID_DIMENSION, GRID_DIMENSION) * 2)
    figure, axes = plt.subplots()
    plt.title("Conway's Game of Life")
    image = axes.imshow(grid, interpolation="nearest")
    anim = FuncAnimation(figure, cycle, fargs=(image, grid), frames=FRAMES,
                         interval=UPDATE_INTERVAL)
    plt.show()


if __name__ == "__main__":
    main()
