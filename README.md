# Conway's Game Of Life

The aim of this project is to experiment with the "animation" submodule of "matplotlib" in order to display Conway's Game of Life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) 
on a 100 x 100 grid. For more powerful computers larger grids are possible in real time, but in my case a 200x200 grid is slow and 1000x1000 is unplayable.

In my code I created a 100x100 numpy 2D array of random numbers between 0 and 1, doubled them and applied the floor function in order to obtain a grid of random binary 
numbers. Being floats, they area also interpreted as white and black respectively when converted to RGB. I then created a "neighbours" function to check for the number 
of neighbours at each coordinate and a "cycle" function to apply changes to each cell based on the number of neighbours and its current state.

The cycle function is then applied to the grid repeateadly, plotting the new result every time using the "FuncAnimation" function of "matplotlib.animate". I set the 
frames as 1000/600 (60 Hz) and the pre-rendered frames to 100. These values can be tweaked at the start of the script in order to get a more or a less fluid image according to their preferences.
