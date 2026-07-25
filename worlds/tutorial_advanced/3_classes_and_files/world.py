# %% [markdown]
# # Advanced tutorial 3 — Classes and files
#
# Tutorial 2 showed how we could load external data and build it into the world definition, but it still involved
# a lot of code making the file a bit complex. If we were to work on a larger world, that could quickly
# expand to make the world difficult to maintain and build.
#
# Instead, as a world grows, it is optimal to implement it as a series of subsystems that you can install into
# a base world. In our case, we will create a subsystem for the shipwrecks, and a subsystem for the sanity
# bands.
#
# An important thing to note - in this example the ordering of which module is installed first does not matter,
# but in more complex worlds it may be important, if there are triggers that need to fire in a certain order.

# %%
import pathlib
import iw

world = iw.World(title="Bones in the Ocean")

# %% [markdown]
# Both `wrecks` and `sanity_bands` are implemented as python modules in the same directory as this script, and can
# be locally imported. More complex projects may have a more complex file structure.
#
# If you want to see how these work, you can use the file browser on the left to examine these modules.
# %%
import wrecks
import sanity_bands

# Each of these modules is equipped with an `install_into` method that will modify the world to include
# the effects of that module.
wrecks.install_into(world)          # a KIB per ship, and the roster that makes the AI name them
sanity_bands.install_into(world)    # the sanity meter, the block it rewrites, and the ten band triggers

# %% [markdown]
# ## Output

# %%
print(world.summary())
pathlib.Path("tutorial_advanced_3_classes_and_files.json").write_text(world.to_json())
