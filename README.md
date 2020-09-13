# About

 Conway's Game of Life is a zero-player game devised by the British mathemetician John Horton Conway. The rules of the game are as follows:

* Any live cell with fewer than two live neighbours dies, as if by underpopulation.
* Any live cell with two or three live neighbours lives on to the next generation.
* Any live cell with more than three live neighbours dies, as if by overpopulation.
* Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

You can view more information [here](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) 

# Controls

|     Key     |                       What it does                      |
|:-----------:|:-------------------------------------------------------:|
|  Left Click |     Add living cells (can only be done during pause)    |
| Right Click |   Remove living cells (can only be done during pause)   |
|    Space    |                        Play/Pause                       |
|      C      | Clear all living cells (can only be done during pause)  |
|      G      |                       Toggle Grid                       |

# Using the application

* Clone GitHub repository
* Download required dependencies: `$ pip install -r requirements.txt`
* `$ python main.py`
* Adjust the window size, cell size, and FPS at the top of the script (optional)

