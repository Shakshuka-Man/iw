# Tutorial 3 — `plot`: the plot engine

This tutorial assumes that you are familiar with the [basic](../tutorial_iw/README.md) and
[advanced](../tutorial_advanced/README.md) tutorials.

In the previous tutorials, we built worlds out of tracked items and triggers written by hand. This tutorial
covers `plot`, a module for building branching storylines. A story with many stages needs a trigger for
each stage and each transition between them, which quickly becomes difficult to manage by hand. `plot` lets
us describe the story as a set of stages and the transitions between them, and it generates all of the
underlying tracked items and triggers for us.

| | notebook | what it teaches                                                   |
|---|---|-------------------------------------------------------------------|
| 1 | [**1_simple**](1_simple/world.ipynb) | Stages, transitions, and the shape of a plot file.                |
| 2 | [**2_behind_the_scenes**](2_behind_the_scenes/world.ipynb) | The tracked items and triggers a plot compiles to, built by hand. |
| 3 | [**3_branching**](3_branching/world.ipynb) | Forks in the story, and paths that split and rejoin.              |
| 4 | [**4_characters**](4_characters/world.ipynb) | A plot that is experienced differently by different characters.   |
| 5 | [**5_multiple_plotlines**](5_multiple_plotlines/world.ipynb) | Many plots running at once, gating each other.                    |

## References

- [**docs/plot.md**](../../docs/plot.md) is the `plot` reference: every object and attribute with its
  type, default and purpose, plus what the compiler emits and what it refuses to emit.

