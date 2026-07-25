# Tutorial 1 — `iw`: the data model

`iw` is a typed mirror of the JSON that Infinite Worlds reads: one object for each thing the format has,
one attribute for each field. These tutorials cover the basics of creating a world using the `iw` module.

## The world they build

We will be building a psychological horror world named `Bones in the Ocean`. In each tutorial, we will be
exploring an aspect of how we can develop the world, and add features to make creating it more effective.

Each tutorial will produce a json that can be imported into Infinite Worlds to form a playable world. The
tutorials also provide an interactive environment where you can alter the world code yourself to play around
and adapt this logic to your own world.

Click a title to open it.

| | notebook | what it covers |
|---|---|---|
| 1 | [**1_simple_world**](1_simple_world/world.ipynb) | Creating the simplest version of the world from scratch. |
| 2 | [**2_instruction_blocks**](2_instruction_blocks/world.ipynb) | Extra instruction blocks and keyword instruction blocks. |
| 3 | [**3_characters**](3_characters/world.ipynb) | Creating playable characters and NPCs. |
| 4 | [**4_tracked_items**](4_tracked_items/world.ipynb) | How to create and maintain tracked items. |
| 5 | [**5_triggers**](5_triggers/world.ipynb) | Creating triggers to alter the world as it is played. |

If you prefer, the [tutorial page](../../docs/tutorial-1-iw.md) combines these five tutorials into a single document.

## Reference

- [**docs/iw.md**](../../docs/iw.md) is the `iw` reference: every object and attribute with its type,
  default and purpose, every enum member with a line of code using it, and what the engine does with each.

## Further reading

This set of tutorials covers the basics of the `iw` tool, but it does not cover *why* you would want to use it - the
basic usage isn't any more efficient than just using the Infinite Worlds native world editor interface. In [**Tutorial 2 — advanced**](../tutorial_advanced/README.md),
we will cover more advanced ways to create worlds and how to programmatically create the objects within a world. For
larger worlds, this automation provides a massive benefit over having to do everything manually.

You can also read [**Tutorial 3 — `plot`**](../tutorial_plot/README.md), which details the plot engine - a powerful tool for handling
plot threads, character advancement, and other advanced logic.
