# One-Block Tetris Homework

In this homework you will develop your first micro:bit program &ndash; a simplified version of the popular game [TETRIS](https://en.wikipedia.org/wiki/Tetris). The main difference is that there is only one type of block - a single pixel.

The objective of this homework is to let you **familiarize with the MicroPython/micro:bit developing environment**, as well as understanding **non-blocking scheduling**.

![](/images/tetris.gif)

## Content of this folder

- _src_: source folder with your python code (_main.py_ and an helper file _timer.py_).
- _demo_: a folder that contains the working example of the game you have to make. Simply drag the _hex_ file on your micro:bit for testing it.
- _images_: a folder with some images for this document.
- _README_: this file, containing the instructions.

## Getting started

- You do not need any additional hardware beside a micro:bit to complete the assignment.
- Download or clone this repository on your computer. Extract the folder from the zip file if necessary.
- Open the folder _src_ containing the source code with VSCode. Make sure the [MicroPython extension](https://marketplace.visualstudio.com/items?itemName=MAKinteract.micro-bit-python) is installed correctly (as well as its Python dependency)
- Initialize the sketch by running the comand `micro:bit-python: Initialize the workspace`, but select **empty** as template.
- Flash once the MicroPython environment and then flash the sketch.

## Code requirments

- Blocks always starts at position (0,2) and move downward, 1 row at a time every _500ms_. If there is an obstacle underneath, the block stops there.
- You can use the _left_ (A) and _right_ (B) buttons to move the current block. The system checks for a user input every _100ms_.
- Blocks cannot move to locations that are already occupied.
- If blocks form a _full row_, the row is deleted.
- If one column of blocks reach the top (i.e., all rows are occupied), it is _game over and a SAD face_ appears.

## Tips

- Consider using a list to keep track of the state (on/off) of each one of the 25 pixels.
- The brightness of the builtin LEDs is between 0 (off) and 9 (fully on). In my demo I used the max brightness of 9.
- If you need to change the values assigned to global variables of immutable types (e.g., numbers and booleans) remember to use the keyword `global`. Here an example

```python
x = 0

# Wrong: this will not work!
def changeX (newX):
    # newX is assigned to a new local variable x
    x = newX;

# Correct
def changeX (newX):
    global x
    # x is a reference to the global x
    x= newX;
```

## Submission and grading

Zip your MicroPython sketch (_zip_, not ALZIP, rar or others) and submit this file using the [homework submission system](homework.prototyping.id).

![](images/hwsystem.png)

Please note that:

1. Only submissions made with the system will be considered (no direct emails to TA or Prof).
2. You can re-submit as many times as you want before the deadline &ndash; we will consider your last submission.
3. Submissions after the deadline are **NOT** accepted.
4. If the file is too large the system won’t allow the submission. Remove from the zip file unnecessary files (I only want to see your code!)
5. Do not copy from the Internet or colleagues without attribution. Remember the _honor code policy_.
