# Tutorial 2 — advanced: why not just use the editor

This tutorial assumes that you are familiar with the [basic tutorial](../tutorial_iw/README.md).

In the basic tutorial, we covered how you can create Python objects that mirror IW's internal structure. This
tutorial covers how to do it programmatically. As the size of a world increases, it becomes increasingly
unwieldy to develop in the Infinite Worlds interface, and these notebooks cover the techniques that make
developing large worlds manageable. For really large worlds, such as `starlit_frontiers`, using these tools
is necessary.

| | notebook | the argument                                                       |
|---|---|--------------------------------------------------------------------|
| 1 | [**1_helpers**](1_helpers/world.ipynb) | Helpers that reduce trigger overhead.                              |
| 2 | [**2_generating_from_data**](2_generating_from_data/world.ipynb) | Using external data sources such as CSV files to generate objects. |
| 3 | [**3_classes_and_files**](3_classes_and_files/world.ipynb) | Structuring a larger world into modules.                           |
| 4 | [**4_combining_everything**](4_combining_everything/world.ipynb) | Combining everything into a single complete world.                 |

## References

- [**docs/iw.md**](../../docs/iw.md) is the `iw` reference: every object and attribute with its type,
  default and purpose, and every enum member with a line of code using it.
- [**docs/plot.md**](../../docs/plot.md) is the same for the plot compiler, plus what it emits and what
  it refuses to emit.

## Next

[**Tutorial 3 — `plot`**](../tutorial_plot/README.md) is the last layer: a compiler for story structure that
assumes everything in this track. Or see [**`starlit_frontiers`**](../starlit_frontiers/README.md), the same
techniques at full size.
