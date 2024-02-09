# Stretch Exercise: Modifying Existing OOP Code

This exercise is, perhaps, the most realistic simulation of software engineering in this course. It's intended as an open ended exercise, and as such a solution is not provided. By now you should be able to tell if your code is working by running it, testing it, etc!

Goals:

* Learn how to write code in environments with increased complexity.
* Learn how to take a concept or idea, and implement it in code.
* Practice creative problem solving.

## The Exercise:

In this folder there is a program called `05e-dungeonmons.py`. This program is a very simple text based game. But the game has loads of problems, some of which you'll hopefully want to fix!

Start this exercise by "playing" one round of the game. Note that:

* It's completely deterministic, all you can do is advance the round and watch the hero fight, level up once, and ultimately die. 
* The display isn't particularly enticing.
* Everything happens instantly, there's no drama or tension!
* There's only one kind of monster.
* The code isn't very "DRY" so there is a lot of code duplicated between the Hero and Dungeonmon classes.

### Your Goal...

Is simply to make this game better. There are TONS of ways you might do this. Here are some ideas:

#### Add Some Randomness

Most games have an element of random behavior, like a dice roll or a shuffled deck of cards. Introduce mechanics based on the element of chance. Perhaps modifiers to do less or more damage, perhaps a "critical hit" mechanic, perhaps generate some of the stats randomly.

Python has very good built in support for lots of random behavior. See: [https://docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html)

#### Give the player some choices

Right now all the player can do is advance the round. That's not much of a game! Give the player some choices. You could add another type of attack and let the player pick. You could give the player options to heal, run, etc. 

#### Make the display prettier

Terminal displays support the use of color! Check out these two articles and try to implement colors to make the display easier to read, and more exciting!

* [https://saturncloud.io/blog/how-to-print-colored-text-to-the-terminal/](https://saturncloud.io/blog/how-to-print-colored-text-to-the-terminal/)
* [https://chrisyeh96.github.io/2020/03/28/terminal-colors.html](https://chrisyeh96.github.io/2020/03/28/terminal-colors.html)

#### Make the player wait

This one is easy to implement, but really improves the games feel. The following code will pause python's execution for half a second, allowing messages to appear on the screen one by one rather than all at once.

```python
import time

time.sleep(0.5)
```

#### Do something else that sounds interesting to you

Be creative, this world is *your* world after all! 