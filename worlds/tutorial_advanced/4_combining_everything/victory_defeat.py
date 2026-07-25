import iw
from tracked_items import SANITY, DAYS_ON_ISLAND

# %% [markdown]
# We will set up victory and defeat conditions - we win if we survive the 6 months and are taken off the island, and we lose if we die.
# %%

VICTORY_CONDITION = iw.VictoryDefeatCondition(
    condition="I am taken off the island after surviving six months.",
    text=("It has been the longest six months of your life, but you have survived. As you head back to the mainland, you know that even though you have left Rona, it has left its mark on you and you will never be the same again."),
)
DEFEAT_CONDITION = iw.VictoryDefeatCondition(
    condition="I die.",
    text="Your adventure ends here - yet another lighthouse keeper claimed by Rona.",
)

# %% [markdown]
# We will also set up some helper triggers - when 180 days are reached, a boat arrives to pick up the player.
# We will also add an alternate defeat condition - when sanity reaches 0.

# %%
VICTORY_DEFEAT_TRIGGERS = []
VICTORY_DEFEAT_TRIGGERS.append(iw.TriggerEvent(
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

VICTORY_DEFEAT_TRIGGERS.append(iw.TriggerEvent(
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

def install_into(world: iw.World) -> None:
    """Add the victory and defeat conditions, and the triggers that fire them, to `world`."""
    world.victoryCondition=VICTORY_CONDITION
    world.defeatCondition=DEFEAT_CONDITION
    world.triggerEvents.extend(VICTORY_DEFEAT_TRIGGERS)