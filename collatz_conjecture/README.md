### Collatz Conjecture

##### The Collatz Conjecture is a famous unsolved problem in mathematics. The comjecture simply asks whether or not all numbers will reduce to 1 by following two simple equations. More information can be found [here](https://en.wikipedia.org/wiki/Collatz_conjecture).

##### The goal of this application is merely to visualize the tree that can be formed by applying two simple rules to a list of numbers. The two rules are:
1) If the number is even, divide it by 2
2) If the number is odd, multiply it by 3 and add 1

Running this code is very simple, the following to provide the code for the game, to allow users to play with these rules and experiement with the possible interaction. Running the code in fairly simple:
1) Import the code using <code>from collatz import Collatz</code>
2) Create an instance of the visualization with <code>c = Collatz(X)</code>. The value X must be an integer and represents the top number you are supplying to the conjecture. Following the rule, higher numbers may be added to the tree.
3) Run the game will <code>c.set_turtle(bg, lc, size, starting_point, filename)</code>
    - The bg argument is the background color supplied to the turtle module.
    - The lc argument is the line color supplied to the turtle module.
    - The size argument is the size of the visualization.
    - The starting_point argument is where the visualization will start on the screen.
    - The filename argument is optional. If supplied it saves the file as a JPG with the given filename.

##### The following code will produce the image below:

    from collatz import Collatz
    c = Collatz(10000)
    bg = (212, 166, 83)
    lc = 'black'
    size = (1000, 1000)
    starting_point = (50, 350)
    filename = 'collatz'
    c.set_turtle(bg, lc, size, starting_point, filename)

![Collatz Conjecture example visualization](./images/collatz.jpg)

##### When creating an instance of the game the board is randomly generated. If you want to provide your own board, first create a square numpy 2d array. Then just call the define_board method as follows: <code>life.define_board(board)</code> where the board argument is the numpy array you just created. Then you can run the game normally.