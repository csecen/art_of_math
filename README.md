### Conway's Game of Life 

##### The Game Of Life was developed by John Conway as a way to show that simple rules can lead to complex interaction. More information can be found [here](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

##### The goal of this application is to provide the code for the game, to allow users to play with these rules and experiement with the possible interaction. Running the code in fairly simple:
1) Import the code using <code>from gol import Game_Of_Life as gol</code>
2) Create an instance of the game <code>life = gol(X)</code>. The value X must be an integer and represents the size of the board that will be create, X by X.
3) Run the game will <code>life.run(steps, animate, filename)</code>
    - The steps argument is an integer value representing the number of step you want the game to take, it is required
    - The animate argument is a boolean values that indicates whether you want the game to be displayed when you call run. It defaults to true.
    - If animate is true, the filename argument can be provided if you wish to save the animation.

##### The following code will produce the gif below:

    from gol import Game_Of_Life as gol
    life = gol(68)
    life.run(100, filename="gol.gif")

![Game of Life example run](/clips/gol.gif)

##### When creating an instance of the game the board is randomly generated. If you want to provide your own board, first create a square numpy 2d array. Then just call the define_board method as follows: <code>life.define_board(board)</code> where the board argument is the numpy array you just created. Then you can run the game normally.