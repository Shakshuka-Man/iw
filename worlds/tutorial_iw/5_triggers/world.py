# %% [markdown]
# # Tutorial 5 — Triggers
#
# In the last tutorial, we went over how to create tracked items to track how the player's sanity changes over time
# Now, we will set up some triggers so we can change how the world operates as the player's sanity changes.

# %%
import pathlib
import iw

world = iw.World(
    title="Bones in the Ocean",
)

# %% [markdown]
# We will recreate a simpler version of the sanity tracked item from last tutorial.
# We will also create a new instruction block that we want to change based on the player's sanity
# We will also want a trigger that actually ends the game after the player has survived 6 months.

# %%

SANITY = iw.TrackedItem(name="Sanity", dataType=iw.TrackedItemDataType.NUMBER)
world.trackedItems.append(SANITY)
DAYS_ON_ISLAND = iw.TrackedItem(name="Days on the Island", dataType=iw.TrackedItemDataType.NUMBER)
world.trackedItems.append(DAYS_ON_ISLAND)
SANITY_INSTRUCTIONS = iw.InstructionBlock(name="Sanity Instructions")
world.instructionBlocks.append(SANITY_INSTRUCTIONS)

# %% [markdown]
# We will set up victory and defeat conditions - we win if we survive the 6 months and are taken off the island, and we lose if we die.
# %%

world.victoryCondition = iw.VictoryDefeatCondition(
    condition="I am taken off the island after surviving six months.",
    text=("It has been the longest six months of your life, but you have survived. As you head back to the mainland, you know that even though you have left Rona, it has left its mark on you and you will never be the same again."),
)
world.defeatCondition = iw.VictoryDefeatCondition(
    condition="I die.",
    text="Your adventure ends here - yet another lighthouse keeper claimed by Rona.",
)

# %% [markdown]
# We will also set up some helper triggers - when 180 days are reached, a boat arrives to pick up the player.
# We will also add an alternate defeat condition - when sanity reaches 0

# Note that by default, triggers can get a bit wordy - we have to repeat the tracked item id a couple times, and threre is a lot of boilerplate.
# There are more efficient ways of doing this, and we will explore the more efficient ways in the advanced tutorial.

# %%

world.triggerEvents.append(iw.TriggerEvent(
    name="Boat comes to pick me up",
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=DAYS_ON_ISLAND.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "180",
                "trackedItemID": DAYS_ON_ISLAND.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[iw.TriggerEffect(
        type=iw.EffectType.TELL_AI,
        data=(
            "I have served my full six months. The boatman arrives out of the fog to take "
            "me off Rona and back to the mainland."
        ),
    )],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity defeat",
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "0",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.SHOW_MESSAGE,
            data=(
                "The last traces of your sanity slip away. When the boatman makes his next trip to the "
                "island, he finds it empty. You are never seen or heard from again."
            ),
        ),
        iw.TriggerEffect(type=iw.EffectType.ENDS_GAME, data=False),
    ],
))

# %% [markdown]
# For each band of sanity, we will create a trigger that sets the sanity instruction block to the appropriate value.
# As the player can move between bands multiple times, we will set up the triggers to fire multiple times.
# For now we will do it in the lengthy but straightforward way - in the advanced tutorial, we will see how to do this programatically

# %%

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 91-100",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "91",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "100",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: I spend the daylight hours walking the island and resting from the night's work. The "
                "emptiness of the place unsettles me — no voices, no company, only rock and sea and wind. The "
                "birds, the shore, and the water are exactly as they should be, and my unease is only the "
                "ordinary loneliness of a person left alone.\n"
                "\n"
                "Night: The night is a constant fight to keep the lighthouse working. The machinery fails "
                "again and again, and I move from one problem to the next without rest, forcing the light to "
                "stay lit until morning. By dawn I am exhausted, and the work has taken everything I have."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 81-90",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "81",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "90",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: I use the day to explore the island and recover from the night. Being this alone is "
                "strange, and the silence presses on me, but I notice nothing out of the ordinary. Once in a "
                "while something small catches my attention, and I find the plain reason for it and think no "
                "more of it.\n"
                "\n"
                "Night: The night is spent keeping the lighthouse running, and it does not make it easy. It "
                "breaks down often and demands my attention through the dark hours, and I work hard to keep "
                "the light burning until dawn. The effort leaves me worn out."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 71-80",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "71",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "80",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: In the daytime I walk the island and rest. The loneliness has an eerie edge to it, and "
                "now and then I hear a sound I cannot place or see the birds moving in a way that seems wrong. "
                "I can usually explain these things to myself, though I am not always sure the explanation is "
                "right.\n"
                "\n"
                "Night: At night I work to keep the lighthouse operational. It still fails frequently, and "
                "much of the dark is spent on repairs to keep the light lit. The task is demanding and I feel "
                "it by morning."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 61-70",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "61",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "70",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: I spend the day out on the island and resting from the night. The solitude feels strange "
                "in a way I cannot quite name, and I sometimes notice things I cannot easily explain — a noise "
                "with no source, a shape at the edge of my sight that is gone when I look. The moments pass, "
                "and I tell myself they were nothing.\n"
                "\n"
                "Night: The night is given over to the lighthouse, which needs regular attention to keep "
                "running. Something goes wrong often enough that I cannot rest for long, and I work through "
                "the dark to keep the light burning. Now and then, in the quiet between tasks, I have the "
                "sense that I am not alone."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 51-60",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "51",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "60",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: During the day I explore and try to rest, but the island no longer feels entirely empty "
                "to me. I hear sounds I cannot find the source of, and I come across things on the shore and "
                "among the rocks that I do not remember from before. Some of it I can explain, and some of it "
                "I cannot, and I have begun to look twice at what is around me.\n"
                "\n"
                "Night: At night I keep the lighthouse lit, and it still gives me trouble, though I can manage "
                "it. Between the repairs, in the dark at the top of the tower, I find the light itself holds "
                "my attention more than it used to. I catch myself pausing to look into it before I turn back "
                "to the work."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 41-50",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "41",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "50",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: The day is filled with things I cannot account for. I hear voices and footsteps when I "
                "know I am alone, I see figures that vanish when I turn toward them, and the sea birds gather "
                "and move in patterns that seem to mean something I cannot read. I cannot tell whether any of "
                "it is real or whether my mind is making it, and I have no way to be sure.\n"
                "\n"
                "Night: At night the lighthouse needs little from me, and the light draws me to it. I spend "
                "long stretches simply looking into it, and I find it steadying in a way I cannot explain. The "
                "work I ought to do falls away while I stand there, and the hours pass without my noticing."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 31-40",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "31",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "40",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: In the daylight I wander the island and find it changed. I see and hear people who are "
                "not there, the birds wheel in shapes that feel deliberate, and I keep finding strange objects "
                "washed up along the shore that I cannot account for. I can no longer reliably tell what is "
                "truly in front of me and what I am imagining.\n"
                "\n"
                "Night: The lighthouse asks little of me, and I give myself over to the light. I stand before "
                "it for hours, held by it, unable and unwilling to look away. It comforts me, and the night "
                "goes by while I watch it, the way one might watch something that is calling to them."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 21-30",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "21",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "30",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: My days are full of things that may not be real. Figures, voices, and the feeling of "
                "others close by are with me constantly, the patterns in the birds seem to carry a meaning "
                "meant for me, and the shore offers up objects I cannot explain. I lose track of time and "
                "cannot always say what I have done or how I came to be where I am.\n"
                "\n"
                "Night: At night the light holds me completely. I spend the dark hours before it, staring into "
                "it as though it were calling me, and I struggle to pull myself away. The lighthouse seems to "
                "run without my help, and I do nothing but watch the light, hour after hour, until the day "
                "returns."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 11-20",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "11",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "20",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: In the daylight I can no longer trust what I perceive. I see whole events and people in "
                "full detail that may exist only in my mind, the birds move in patterns I am certain are meant "
                "for me, and the shore is strewn with things I cannot explain. I forget my own actions and "
                "lose long stretches of time, and I rarely know what is real.\n"
                "\n"
                "Night: The light is all there is at night. I stand before it, unable to look away, and the "
                "hours dissolve while I watch it draw me in."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 1-10",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "1",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "10",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: My days have no firm shape. I cannot separate what is real from what is not — the "
                "figures, the birds, the things on the shore all arrive the same way, and I do not know what "
                "is happening, what I have done, or where on the island I am. At times I am not in control of "
                "my own body, and I find myself moving and acting without deciding to.\n"
                "\n"
                "Night: At night the light consumes me. I stand before it and cannot leave it, and there is "
                "nothing else — no work, no thought, no sense of time, only the light and the pull of it. I "
                "watch it until the dark ends, or until I no longer know whether the dark has ended, held by "
                "it as if it were a voice I have to answer."
            )},
        ),
    ],
))

# %% [markdown]
# ## Output
# Now we have added the triggers, we can output the world
# We can then look at the advanced triggers to see how to do these things programatically

# %%
print(world.summary())
pathlib.Path("bones_in_the_ocean_with_triggers.json").write_text(world.to_json())
