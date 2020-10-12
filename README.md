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

# Stage 1/5: Initial setup

## Description 

In this project, you'll write a game called Tic-Tac-Toe that you can play with your computer. The computer will have three levels of difficulty - easy, medium, hard.

But, for starters, let's write a program that knows how to work with coordinates and determine the state of the game.

Suppose the bottom left cell has the coordinates (1, 1) and the top right cell has the coordinates (3, 3) like in this table:

- (1, 3) (2, 3) (3, 3)
- (1, 2) (2, 2) (3, 2)
- (1, 1) (2, 1) (3, 1)

The program should ask to enter the coordinates where the user wants to make a move.

Keep in mind that the first coordinate goes from left to right and the second coordinate goes from bottom to top. Also, notice that coordinates start with 1 and can be 1, 2 or 3.

But what if the user enters incorrect coordinates? The user could enter symbols instead of numbers or enter coordinates representing occupied cells. You need to prevent all of that by checking a user's input and catching possible exceptions.

## Objectives

The program should work in the following way:
  1. Get the 3x3 field from the first input line (it contains 9 symbols containing X, O and _, the latter means it's an empty cell),
  2. Output this 3x3 field with cells before the user's move,
  3. Then ask the user about his next move,
  4. Then the user should input 2 numbers that represent the cell on which user wants to make his X or O. (9 symbols representing the field would be on the first line and these 2 numbers would be on the second line of the user input). Since the game always starts with X, if the number of X's and O's on the field is the same, the user should make a move with X, and if X's is one more than O's, then the user should make a move with O.
  5. Analyze user input and show messages in the following situations:
    - "This cell is occupied! Choose another one!" - if the cell is not empty;
    - "You should enter numbers!" - if the user enters other symbols;
    - "Coordinates should be from 1 to 3!" - if the user goes beyond the field.
  6. Then output the table including the user's most recent move.
  7. Then output the state of the game.

Possible states:
  - "Game not finished" - when no side has a three in a row but the field has empty cells;
  - "Draw" - when no side has a three in a row and the field has no empty cells;
  - "X wins" - when the field has three X in a row;
  - "O wins" - when the field has three O in a row;

If the user input wrong coordinates, the program should keep asking until the user enters coordinate that represents an empty cell on the field and after that output the field with that move. You should output the field only 2 times - before the move and after a legal move.

# Stage 2/5: Easy does it

## Description

Now it is time to make a working game. Let's create our first opponent! In this version of the program, the user will be playing as X, and the "easy" level computer will be playing as O. This will be our first small step to the AI!

Let's make it so that at this level the computer will make random moves. This level will be perfect for those who play this game for the first time! Well, though... You can create a level of difficulty that will always give in and never win the game. You can implement such a level along with "easy" level, if you want, but it will not be tested.

## Objectives

In this stage you should implement the following:
1. When starting the program, an empty field should be displayed.
2. The first to start the game should be the user as X. The program should ask the user to enter the cell coordinates.
3. Next the computer should make its move as O. And so on until someone will win or there will be a draw.
4. At the very end of the game you need to print the final result of the game.

### This project is a part of the following track Python Developer on Jetbrains Academy
