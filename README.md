# Winding Spirals 🌀

This repository contains two Python Turtle graphics projects that create winding spiral patterns. Both use the same movement and turning angle, but the second version introduces colour to make the design more visually interesting.

## Projects

| File | Description |
|---|---|
| `WindingSpiral1.py` | Creates a winding spiral using progressively increasing forward distances and a 91° turn. |
| `WindingSpiral2.py` | Creates the same winding spiral pattern, but adds a cornflower blue pen colour. |

## Concepts Learned

- **Turtle Graphics:** Using Python's `turtle` module to draw patterns.
- **For Loops:** Repeating drawing instructions using `range(200)`.
- **Movement:** Using `forward(x)` to increase the turtle's movement distance with each iteration.
- **Angles:** Using `left(91)` to create a winding pattern.
- **Custom Colours:** Using `pencolor("cornflowerblue")` to change the pen colour.

## How to Run

1. Make sure Python is installed.
2. Open the repository in your Python editor.
3. Run either `WindingSpiral1.py` or `WindingSpiral2.py`.
4. Watch the turtle draw the pattern!

## Key Differences

Both projects use the same loop, forward movement and turning angle.

The main difference is that `WindingSpiral2.py` includes:

```python
t.pencolor("cornflowerblue")
```

This changes the turtle's drawing colour to cornflower blue while keeping the original spiral pattern.

## Experimentation

Try experimenting with different:
- Pen colours using `t.pencolor()`
- Turning angles using `t.left()`
- Drawing speeds using `t.speed()`
- Loop ranges to change the number of iterations

A small change in the code can create a noticeably different visual result!
