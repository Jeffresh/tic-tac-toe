# Tic-tac-toe

# Description 

Nowadays, this game is known all over the world. Each country may have its own version of the name, sometimes the rules are different, but the meaning of the game remains the same. Below are the main rules that may be familiar to you since childhood.

Tic-tac-toe is a game played by two players on a 3x3 field where the duel takes place. One of the players plays as 'X', and the other player is 'O'. 'X' plays first, then the 'O' side plays, and so on.

The first player that writes 3 'X' or 3 'O' in a straight line (including diagonals) wins.

However, our game should show the field in an "intermediate" states too. Let's try to visualize different combinations that the user will determine from the input. It is also important to think about the interface and set boundaries for our field.

In addition to analyzing the field, it is equally important to add the ability to select a cell for your move. Now you need to implement human moves. Let's divide the field into cells.

The program should ask to enter the coordinates where the user wants to make a move.

Note that in this stage user moves as X, not O. Keep in mind that the first coordinate goes from left to right and the second coordinate goes from bottom to top. Also, notice that coordinates start with 1 and can be 1, 2 or 3.

But what if the user enters incorrect coordinates? The user could enter symbols instead of numbers or enter coordinates representing occupied cells. You need to prevent all of that by checking a user's input and catching possible exceptions.

We are at the finish line! But playing alone is not so interesting, is it? Let's combine our successes in past stages and get Tic-Tac-Toe with the ability to play from the beginning (empty field) to the result (win or draw).

Now it is time to make a working game!

In the last stage, make it so you can play a full game with a friend. First one of you moves as X, and then the other one moves as O.

# About
Everybody remembers this paper-and-pencil game from childhood: Tic-Tac-Toe, also known as Noughts and crosses or Xs and Os. A single mistake usually costs you the game, but thankfully it is simple enough that most players discover the best strategy quickly. Let’s program Tic-Tac-Toe and get playing!

# Example

The example below shows how your program should work.
The greater-than symbol followed by space (> ) represents the user input. Notice that it's not the part of the input.
```
---------
|       |
|       |
|       |
---------
Enter the coordinates: > 2 2
---------
|       |
|   X   |
|       |
---------
Enter the coordinates: > 2 2
This cell is occupied! Choose another one!
Enter the coordinates: > two two
You should enter numbers!
Enter the coordinates: > 1 4
Coordinates should be from 1 to 3!
Enter the coordinates: > 1 3
---------
| O     |
|   X   |
|       |
---------
Enter the coordinates: > 3 1
---------
| O     |
|   X   |
|     X |
---------
Enter the coordinates: > 1 2
---------
| O     |
| O X   |
|     X |
---------
Enter the coordinates: > 1 1
---------
| O     |
| O X   |
| X   X |
---------
Enter the coordinates: > 3 2
---------
| O     |
| O X O |
| X   X |
---------
Enter the coordinates: > 2 1
---------
| O     |
| O X O |
| X X X |
---------
X wins
```


### This project is a part of the following track Python Developer on Jetbrains Academy
