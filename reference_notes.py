"""What the source cannot say about itself: what each field is *for*, and how each enum member is used.

`reference.py` reads `iw.py` for structure -- the classes, the fields, their types and defaults -- and
merges it with this file to produce `docs/iw.md`. The split is the point. Structure cannot drift, because
it is read from the source every time. Meaning cannot rot silently, because `reference.py` refuses to
generate if anything here names a class, field or enum member that no longer exists.

So: add a field to `iw.py` and the table grows a row on its own, with an empty note. Delete one and the
build tells you the note is now lying. Neither half can quietly disagree with the other.

Examples are written to run. `reference.py --check-examples` evaluates every one against `EXAMPLE_SETUP`.
"""

# The objects every example in the enum tables refers to. Rendered into the page, and used to evaluate
# the examples, so what a reader sees and what gets checked are the same thing.
EXAMPLE_SETUP = '''\
mood    = iw.TrackedItem(name="Mood", initialValue="calm")
crew    = iw.TrackedItem(name="Crew", dataType=iw.TrackedItemDataType.NUMBER, initialValue="4")
roster  = iw.TrackedItem(name="Roster", dataType=iw.TrackedItemDataType.YAML)
rules   = iw.InstructionBlock(name="Rules", content="Be terse.")
dragons = iw.LoreBookEntry(name="Dragons", content="They sleep.", keywords=["dragon"])
ambush  = iw.TriggerEvent(name="Ambush")
storm   = iw.TriggerEvent(name="Storm")
hero    = iw.PossibleCharacter(name="Hero")
ferryman = iw.NPC(name="The Ferryman", detail="A silent boatman.")\
'''

TITLE = "`iw` — the world format"

INTRO = """\
`iw` is a small Python library that mirrors the game engine's world-definition JSON as typed dataclasses,
and serializes them to and from that JSON. Use it to build world definitions programmatically, or to read
and round-trip existing ones. Its only dependency is PyYAML, which Pyodide ships, so it runs in a browser
unchanged — and it is standalone in the sense that matters here: it does **not** require
[`plot`](plot.md).

This page is **every object in `iw`, every attribute on it, and every enum member** — what each one is,
what it is for, and how it is used. The structure is read out of the dataclasses themselves, so it cannot
fall behind the library; the explanations sit beside it rather than in a separate document.

A field you never set gets the default shown, and a default the engine is happy with — so in practice you
name only the handful you care about.

```python
import iw
```

A world is an `iw.World`. It holds content (characters, NPCs, instruction blocks, lorebook entries,
tracked items, image/style settings) plus an **event system** (`triggerEvents`) that drives dynamic
behaviour. You assemble a `World` from the dataclasses below and call `.to_json()` to get the engine's
JSON; or parse engine JSON back with `World.from_json()`.\
"""

# Prose that belongs to one class, printed under its table.
CLASS_NOTES = {
    "World": """\
- `world.to_dict()` / `world.to_json()` — emit the engine JSON. Optional fields are omitted while still
  at their default, and `positionInList` is stamped onto tracked items and NPCs.
- `iw.World.from_dict(data)` / `iw.World.from_json(s)` — parse engine JSON back into dataclasses. Parsing
  is **strict**: an unknown field raises `NotImplementedError`, so the dataclasses stay a faithful mirror
  of the schema.
- `world.validate()` — raise `ValueError` listing everything that doesn't hang together. **`to_json()`
  calls this for you**, so a broken world raises instead of becoming a file.
- `world.summary()` — a readable account of what is in the world. Print it before and after a change.

The dangling-reference case is worth dwelling on, because it is the one that bites. Triggers name their
tracked items, blocks and characters **by id**. If a trigger holds an id nothing answers to any more, the
engine loads the world perfectly happily — and then that trigger simply never fires. Nothing tells you.
You find it by playing. So the library refuses to write that file at all.\
""",
    "TrackedItem": """\
`item.variable_name` is the item's handle — its `variableName` if one is set, otherwise the name
lowercased with spaces → underscores. A **renamed item keeps its original handle**, so it is this, not the
visible `name`, that a `$`-script or a substitution refers to. `item.as_substitution()` wraps it as
`<<…>>` for embedding in trigger and instruction text.

Where an item's starting value comes from is a whole topic of its own — see
[Initial values](#initial-values-same--character--player) below.\
""",
    "TriggerCondition": """\
Set either a `type` (a leaf condition) or `category="logic"` with an `operator` (a group combining
sub-conditions). A group's `data` holds `TriggerCondition`s whether you built the group or parsed one —
a parsed group's raw sub-dicts are built out on construction — and the owning `TriggerEvent` needs
`advancedLogic=True`. Every leaf condition carries `category="condition"`; the helpers set it for you.\
""",
    "TriggerEffect": """\
The engine fills in extra keys on some payloads that you do not have to write: `path`, `updateMode`,
`listExpression` and `targetExpression` on `SET_TRACKED_ITEM_VALUE`, `path`/`updateMode` on
`PRESENT_CHOICE` and `REQUEST_INPUT`, and `alreadyFired` on a victory/defeat condition.\
""",
    "InitialTrackedItemValue": """\
One of these exists per character for each `CHARACTER`-mode tracked item — they are not free-form
overrides you attach at will. See [Initial values](#initial-values-same--character--player).\
""",
}

# {ClassName: {field: what it is for}}. A field with no entry still gets a row.
FIELDS = {
    "World": {
        "favorite": "Marks the world as a favourite in the author's own list.",
        "title": "The world's name, as players see it.",
        "description": "The blurb shown before anyone plays.",
        "background": "The setting the AI narrates within.",
        "instructions": "The main brief to the AI — the single most important field in the world.",
        "authorStyle": "The prose voice to write in.",
        "recommendedAIModel": "The model this world was tuned against, if it matters.",
        "firstInput": "The opening action, played before the player's first turn.",
        "objective": "The goal shown on screen.",
        "imageModel": "Which image model generates art.",
        "imageStyle": "The named visual preset.",
        "illustrationStyleNonCharacterLowPriority": "Scene-art style hints, applied weakly.",
        "illustrationStyleNonCharacterHighPriority": "Scene-art style hints that take precedence.",
        "illustrationStyleCharacterLowPriority": "Character-art style hints, applied weakly.",
        "illustrationStyleCharacterHighPriority": "Character-art style hints that take precedence.",
        "imageStyleCharacterPre": "Text prepended to every character image prompt.",
        "imageStyleCharacterPost": "Text appended to every character image prompt.",
        "imageStyleNonCharacterPre": "Text prepended to every scene image prompt.",
        "imageStyleNonCharacterPost": "Text appended to every scene image prompt.",
        "nsfw": "Flags the world as adult.",
        "mature": "Flags mature-but-not-adult content.",
        "contentWarnings": "Warnings shown before play.",
        "enableAISpecificInstructionBlocks": "Lets blocks target particular AI profiles — required for `InstructionBlock.selectedAIProfiles` to do anything.",
        "previewImage": "The cover image.",
        "fullSizePreviewImage": "The cover image at full resolution.",
        "previewImageOptions": "Every generated cover candidate.",
        "fullSizePreviewImageOptions": "The full-resolution candidates.",
        "currentPreviewImageIndex": "Which candidate is in use; `-1` means none chosen.",
        "imagePromptDetails": "The structured prompt the cover art was generated from.",
        "permissionsOnceShared": "What other people may do with the world once it is shared.",
        "allowChangeCharacterName": "Lets the player rename their character.",
        "allowChangeCharacterDescription": "Lets the player rewrite their character's description.",
        "allowChangeCharacterSkills": "Lets the player adjust starting skills.",
        "allowChangeCharacterItemValues": "Lets the player set per-character tracked-item values.",
        "allowChangeCharacterPortrait": "Lets the player pick a different supplied portrait.",
        "allowChangeCharacterNewPortrait": "Lets the player generate a fresh portrait.",
        "evaluationRequest": "Instructions for how the AI should judge the player's turn.",
        "schemaVersion": "The world-format version this world is written to.",
        "skills": "The named skills characters have.",
        "hideSkillSystem": "Hides skills from the player entirely.",
        "possibleCharacters": "The playable characters to choose between.",
        "triggerEvents": "The event system: everything that fires in response to play.",
        "victoryCondition": "How the world is won.",
        "defeatCondition": "How the world is lost.",
        "conditions": "The named events this world recognises. An `ON_EVENT` condition fires on one by "
                      "carrying the same string in its `data`, so this is the vocabulary those "
                      "conditions draw on rather than each of them inventing its own wording.",
        "descriptionRequest": "Instructions for generating the world description.",
        "summaryRequest": "Instructions for summarising the story so far.",
        "charSelectText": "Text shown on the character-selection screen.",
        "instructionBlocks": "Blocks of instruction the AI is given alongside the main brief.",
        "loreBookEntries": "Keyword-triggered lore, surfaced only when relevant.",
        "trackedItems": "The world's state variables.",
        "NPCs": "The non-player characters.",
        "version": "The author's own version string.",
        "autoAdvanceVersion": "Bumps `version` automatically on save.",
        "designNotes": "Notes to yourself; never shown to players or the AI.",
    },
    "TrackedItem": {
        "name": "What the player sees in the tracked-item panel.",
        "id": "The id triggers refer to it by. Never write one by hand.",
        "dataType": "Whether the value is text, a number, or a structured document.",
        "visibility": "Who can see it.",
        "description": "What this item means, for the AI's benefit.",
        "updateInstructions": "How the AI should decide to change it.",
        "initialValue": "The starting value, for `SAME` and `PLAYER` modes.",
        "initialValueBasedOnPC": "Where the starting value comes from.",
        "autoUpdate": "Lets the AI update the item on its own each turn.",
        "variableName": "The item's `$`-script handle. Derived from the name if unset — and kept when the item is renamed, so the two can diverge.",
        "enforceFormat": "Requires the value to match `formatSchema`.",
        "formatSchema": "The schema a structured value must satisfy.",
        "formatExample": "A worked example of the expected format.",
        "driftAcknowledgedForName": "Engine bookkeeping for a name that has drifted from its handle.",
        "initialValueChoices": "For `PLAYER` mode: the literal options the player picks between.",
        "initialValueChoicesScript": "For `PLAYER` mode: a `$`-script yielding those options.",
    },
    "InitialTrackedItemValue": {
        "id": "The id of the tracked item this value is for.",
        "name": "That item's name, repeated.",
        "initialPCValue": "This character's starting value — or a list of options to choose between.",
        "visibility": "Who can see it, for this character.",
        "initialValueBasedOnPC": "Mirrors the item's own mode; an entry declaring anything but `CHARACTER` is dropped on import.",
        "initialPCValueChoicesScript": "A `$`-script yielding this character's options.",
    },
    "TriggerEvent": {
        "name": "What this event is called. Yours, not the engine's.",
        "id": "The id other triggers name it by, in `PREREQS` and `FIRE_RANDOM_TRIGGER`.",
        "triggerEffects": "What happens when it fires.",
        "triggerConditions": "What has to hold for it to fire.",
        "advancedLogic": "Required before a condition may be a logic group.",
        "triggerOnStartOfGame": "Fires once, before the first turn.",
        "triggerMidGame": "Lets a start-of-game trigger fire on later turns too. Only meaningful "
                          "alongside `triggerOnStartOfGame` — on its own it does nothing.",
        "canTriggerMoreThanOnce": "Lets it fire again; otherwise it fires once ever.",
    },
    "TriggerCondition": {
        "data": "The payload. Its shape depends on `type` — see the condition table.",
        "id": "Its own id.",
        "type": "Which kind of condition. Absent on a logic group.",
        "category": "`\"condition\"` for a leaf, `\"logic\"` for a group.",
        "trackedItemID": "The item read, repeated outside `data` — both copies must agree.",
        "inequality": "The comparison, written here as well as in `data`, and only when it is not the default.",
        "operator": "`AND` / `OR`, on a logic group.",
    },
    "TriggerEffect": {
        "type": "Which kind of effect.",
        "data": "The payload. Its shape depends on `type` — see the effect tables.",
        "id": "Its own id.",
        "trackedItemID": "The item written, repeated outside `data` — both copies must agree.",
    },
    "InstructionBlock": {
        "name": "What the block is called.",
        "content": "The instructions themselves.",
        "id": "The id `MODIFY_INSTRUCTION_BLOCK` names it by.",
        "selectedAIProfiles": "Restricts the block to particular AI profiles — `smilodon`, `massivecat`, `caracal`, `smilodon-thinking`. Anything else is filtered out on import, and `World.enableAISpecificInstructionBlocks` must be on.",
    },
    "LoreBookEntry": {
        "name": "What the entry is called.",
        "content": "The lore revealed when it fires.",
        "id": "The id `MODIFY_KEYWORD_BLOCK` names it by.",
        "keywords": "The words that surface this entry.",
    },
    "PossibleCharacter": {
        "name": "The character's name.",
        "description": "Who they are.",
        "portrait": "Their portrait image.",
        "portraitPromptDetails": "The structured prompt the portrait was generated from.",
        "fullSizePortrait": "The portrait at full resolution.",
        "portraitOptions": "Every generated portrait candidate.",
        "fullSizePortraitOptions": "The full-resolution candidates.",
        "currentPortraitIndex": "Which candidate is in use.",
        "characterId": "The id `ON_CHARACTER` gates on.",
        "skills": "Starting skill values, by name.",
        "initialTrackedItemValues": "This character's values for the `CHARACTER`-mode tracked items.",
    },
    "NPC": {
        "name": "The NPC's name.",
        "id": "Its id.",
        "detail": "The full account of who they are.",
        "one_liner": "A one-line summary.",
        "appearance": "How they look, in prose.",
        "location": "Where they are found.",
        "secret_info": "What the AI knows and the player does not.",
        "names": "Aliases they also answer to.",
        "img_appearance": "Appearance, phrased for the image model.",
        "img_clothing": "Clothing, phrased for the image model.",
    },
    "VictoryDefeatCondition": {
        "condition": "What must happen, judged by the AI.",
        "text": "What the player is told when it does.",
        "alreadyFired": "Engine bookkeeping; reset on import.",
    },
    "ImagePromptDetails": {
        "illustrGenre": "The genre the art should evoke.",
        "illustrClothes": "What the subject is wearing.",
        "illustrSetting": "Where the image is set.",
        "illustrSubject": "Who or what the image is of.",
        "illustrAppearance": "The subject's appearance.",
        "illustrIsCharacter": "Whether this is a character portrait or a scene.",
        "illustrExpressionPosition": "Expression and pose.",
    },
    "PortraitPromptDetails": {
        "illustrGenre": "The genre the portrait should evoke.",
        "illustrClothes": "What the character is wearing.",
        "illustrSetting": "The backdrop.",
        "illustrSubject": "Who the portrait is of.",
        "illustrAppearance": "Their appearance.",
        "illustrIsCharacter": "Whether this is a character portrait or a scene.",
        "illustrExpressionPosition": "Expression and pose.",
    },
    "PermissionsOnceShared": {
        "sharing": "Whether others may share it on.",
        "editing": "Whether others may edit their own copy.",
    },
}

# Prose printed under one enum's table.
ENUM_NOTES = {
    "TrackedItemVisibility": """\
`HIDDEN` and `HIDDEN_BORING` both hide an item from the player in normal play; the difference is *where*
it still shows. `HIDDEN` is visible in **storyteller mode**, `HIDDEN_BORING` only in **debug mode**. Reach
for `HIDDEN_BORING` for bookkeeping the storyteller never needs to see.\
""",
    "TrackedItemInitialValueSource": """\
Which mode an item is in decides *where its starting value lives* — see
[Initial values](#initial-values-same--character--player) below.\
""",
    "ConditionType": """\
Every leaf condition carries `category="condition"`; the helpers set it for you. A **logic group** is a
condition with no `type` at all — `category="logic"` and an `operator` — whose `data` is a list of
sub-conditions. It nests arbitrarily, and its `TriggerEvent` needs `advancedLogic=True`:

```python
iw.TriggerCondition(category="logic", operator=iw.LogicOperator.OR, data=[
    tracked_item_is(mood, "uneasy"),
    tracked_item_is(crew, "2", inequality=iw.Inequality.AT_MOST),
])
```\
""",
    "EffectType": """\
`minSelections`/`maxSelections` come back as ints from some triggers and strings from others — read both.\
""",
}

# {EnumName: {MEMBER: (what it does, example)}}. Examples are evaluated, so they must run.
ENUMS = {
    "TrackedItemDataType": {
        "TEXT": ("A plain string. The default.", 'iw.TrackedItem(name="Mood", dataType=iw.TrackedItemDataType.TEXT, initialValue="calm")'),
        "NUMBER": ("A number, still carried as a string.", 'iw.TrackedItem(name="Crew", dataType=iw.TrackedItemDataType.NUMBER, initialValue="4")'),
        "XML": ("Structured data as XML. Semi-deprecated — prefer `YAML`.", 'iw.TrackedItem(name="Party", dataType=iw.TrackedItemDataType.XML)'),
        "YAML": ("Structured data as a YAML document: nested maps and lists, reachable from `$`-scripts. The going-forward type.", 'iw.TrackedItem(name="Roster", dataType=iw.TrackedItemDataType.YAML, initialValue="members:\\n  - name: Ivo")'),
    },
    "TrackedItemVisibility": {
        "EVERYONE": ("Shown to the player and given to the AI.", 'iw.TrackedItem(name="Mood", visibility=iw.TrackedItemVisibility.EVERYONE)'),
        "AI_ONLY": ("Given to the AI, never shown to the player.", 'iw.TrackedItem(name="Suspicion", visibility=iw.TrackedItemVisibility.AI_ONLY)'),
        "PLAYER_ONLY": ("Shown to the player, withheld from the AI.", 'iw.TrackedItem(name="Notes", visibility=iw.TrackedItemVisibility.PLAYER_ONLY)'),
        "HIDDEN": ("Hidden in normal play; visible in storyteller mode.", 'iw.TrackedItem(name="Stage", visibility=iw.TrackedItemVisibility.HIDDEN)'),
        "HIDDEN_BORING": ("Hidden in normal play; visible only in debug mode.", 'iw.TrackedItem(name="Turn counter", visibility=iw.TrackedItemVisibility.HIDDEN_BORING)'),
    },
    "TrackedItemInitialValueSource": {
        "SAME": ("Every playthrough starts from the item's own `initialValue`.", 'iw.TrackedItem(name="Mood", initialValueBasedOnPC=iw.TrackedItemInitialValueSource.SAME, initialValue="calm")'),
        "CHARACTER": ("The value depends on which character is chosen, and lives on each character.", 'iw.TrackedItem(name="Homeland", initialValueBasedOnPC=iw.TrackedItemInitialValueSource.CHARACTER)'),
        "PLAYER": ("The player enters it; `initialValue` is the default they edit.", 'iw.TrackedItem(name="Callsign", initialValueBasedOnPC=iw.TrackedItemInitialValueSource.PLAYER, initialValue="Nomad")'),
    },
    "TrackedItemAction": {
        "SET": ("Overwrite the value.", 'set_tracked_item(mood, "uneasy")'),
        "ADD": ("Add to it.", 'set_tracked_item(crew, "1", action=iw.TrackedItemAction.ADD)'),
        "SUBTRACT": ("Take away from it.", 'set_tracked_item(crew, "1", action=iw.TrackedItemAction.SUBTRACT)'),
        "REPLACE": ("Find `newValue` and swap in `replaceWith` — here the value you pass is the needle, not the result.", 'set_tracked_item(mood, "calm", action=iw.TrackedItemAction.REPLACE)'),
    },
    "Inequality": {
        "IS_EXACTLY": ("Equal. The default, and the one the engine does not write down.", 'tracked_item_is(mood, "uneasy")'),
        "AT_LEAST": ("Greater than or equal.", 'tracked_item_is(crew, "2", inequality=iw.Inequality.AT_LEAST)'),
        "AT_MOST": ("Less than or equal.", 'tracked_item_is(crew, "2", inequality=iw.Inequality.AT_MOST)'),
        "NOT_EQUAL": ("Different.", 'tracked_item_is(mood, "calm", inequality=iw.Inequality.NOT_EQUAL)'),
    },
    "LogicOperator": {
        "AND": ("Every sub-condition must hold.", 'iw.TriggerCondition(category="logic", operator=iw.LogicOperator.AND, data=[tracked_item_is(mood, "uneasy"), tracked_item_is(crew, "2", inequality=iw.Inequality.AT_MOST)])'),
        "OR": ("Any sub-condition may hold.", 'iw.TriggerCondition(category="logic", operator=iw.LogicOperator.OR, data=[tracked_item_is(mood, "uneasy"), tracked_item_is(mood, "afraid")])'),
        "NONE_OF": ("No sub-condition may hold — the negation the other two cannot express. Wrapping a single condition in it is how you say *unless*.", 'iw.TriggerCondition(category="logic", operator=iw.LogicOperator.NONE_OF, data=[tracked_item_is(mood, "calm")])'),
    },
    "NPCAction": {
        "MODIFY": ("Replace the NPC with the one in `data[\"npc\"]`, matched by `data[\"character\"]`. The whole NPC is written, not the changed fields, so send it as it should end up.", 'iw.TriggerEffect(type=iw.EffectType.CHANGE_OTHER_CHARACTERS, data={"character": ferryman.name, "action": iw.NPCAction.MODIFY, "npc": {"id": ferryman.id, "name": ferryman.name, "detail": "He speaks now."}})'),
        "DELETE": ("Remove the NPC from the world.", 'iw.TriggerEffect(type=iw.EffectType.CHANGE_OTHER_CHARACTERS, data={"character": ferryman.name, "action": iw.NPCAction.DELETE, "npc": {"id": ferryman.id, "name": ferryman.name}})'),
    },
    "ConditionType": {
        "ON_TURN": ("Fires on turn **≥ N**, not exactly N. `data=1` is the \"every turn\" idiom.", 'iw.TriggerCondition(type=iw.ConditionType.ON_TURN, category="condition", data=1)'),
        "ON_EVENT": ("Fires when the AI judges the described situation to have happened.", 'iw.TriggerCondition(type=iw.ConditionType.ON_EVENT, category="condition", data="the crew mutinies")'),
        "ON_CHARACTER": ("Gates on who the player picked.", 'iw.TriggerCondition(type=iw.ConditionType.ON_CHARACTER, category="condition", data=[hero.characterId])'),
        "ON_TRACKED_ITEM": ("Reads a tracked item. `data` is `{inequality, requiredValue, trackedItemID, textComparison}`. `textComparison` is **required** (`\"contains\"` / `\"does_not_contain\"`) — a condition without it is dropped on import. Text items have *no* exact match, only contains. `tracked_item_is` fills it in for you.", 'tracked_item_is(mood, "uneasy")'),
        "ON_RANDOM_CHANCE": ("Fires that percent of the time. The percentage is a **string**.", 'iw.TriggerCondition(type=iw.ConditionType.ON_RANDOM_CHANCE, category="condition", data="37")'),
        "ON_PAW_SCRIPT": ("Fires when a `$`-expression is true.", 'iw.TriggerCondition(type=iw.ConditionType.ON_PAW_SCRIPT, category="condition", data="$roster.party.count()>0")'),
        "PREREQS": ("Fires only once the listed triggers have.", 'iw.TriggerCondition(type=iw.ConditionType.PREREQS, category="condition", data=[ambush.id])'),
    },
    "EffectType": {
        "SHOW_MESSAGE": ("Shows the player a message, outside the narration.", 'iw.TriggerEffect(type=iw.EffectType.SHOW_MESSAGE, data="The bridge collapses behind you.")'),
        "TELL_AI": ("Instructs the AI on what to do next.", 'iw.TriggerEffect(type=iw.EffectType.TELL_AI, data="Raise the tension. End the scene on a threat.")'),
        "GIVE_INFO": ("Tells the AI something out of band, without narrating it.", 'iw.TriggerEffect(type=iw.EffectType.GIVE_INFO, data="The captain is lying about the cargo.")'),
        "CHANGE_MAIN_INSTRUCTIONS": ("Rewrites the main instructions.", 'iw.TriggerEffect(type=iw.EffectType.CHANGE_MAIN_INSTRUCTIONS, data="I am now the hunted, not the hunter.")'),
        "CHANGE_AUTHOR_STYLE": ("Rewrites the author-style voice.", 'iw.TriggerEffect(type=iw.EffectType.CHANGE_AUTHOR_STYLE, data="Terse, clipped, hard-boiled.")'),
        "CHANGE_DESCRIPTION_INSTRUCTIONS": ("Rewrites the description-request instructions.", 'iw.TriggerEffect(type=iw.EffectType.CHANGE_DESCRIPTION_INSTRUCTIONS, data="Describe each scene in two sentences, no more.")'),
        "CHANGE_OBJECTIVE": ("Rewrites the on-screen goal.", 'iw.TriggerEffect(type=iw.EffectType.CHANGE_OBJECTIVE, data="Escape the city before dawn.")'),
        "CHANGE_BACKGROUND": ("Rewrites the background.", 'iw.TriggerEffect(type=iw.EffectType.CHANGE_BACKGROUND, data="A drowned city, ruled by salvage crews.")'),
        "CHANGE_FIRST_ACTION": ("Rewrites `firstInput`, before the first turn.", 'iw.TriggerEffect(type=iw.EffectType.CHANGE_FIRST_ACTION, data="I wake to alarms.")'),
        "CHANGE_PC_NAME": ("Renames the playing character.", 'iw.TriggerEffect(type=iw.EffectType.CHANGE_PC_NAME, data="The Stranger")'),
        "CHANGE_PC_DESCRIPTION": ("Rewrites the playing character's description.", 'iw.TriggerEffect(type=iw.EffectType.CHANGE_PC_DESCRIPTION, data="Scarred, quiet, unwilling to explain the coat.")'),
        "RUN_SCRIPT": ("Runs a `$`-script block.", 'iw.TriggerEffect(type=iw.EffectType.RUN_SCRIPT, data="for each $m in $roster.party\\n  $m.hp += 5")'),
        "SET_TRACKED_ITEM_VALUE": ("Writes a tracked item. `data` is `{action, newValue, replaceWith, trackedItemID}`; the `action` decides how — see `TrackedItemAction`.", 'set_tracked_item(mood, "uneasy")'),
        "MODIFY_INSTRUCTION_BLOCK": ("Rewrites a block's text.", 'iw.TriggerEffect(type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK, data={"id": rules.id, "content": "Be terse. Never explain the magic."})'),
        "MODIFY_KEYWORD_BLOCK": ("The same for a lorebook entry, and rewrites its keywords too.", 'iw.TriggerEffect(type=iw.EffectType.MODIFY_KEYWORD_BLOCK, data={"id": dragons.id, "content": "They are awake now.", "keywords": ["dragon", "wyrm"]})'),
        "MODIFY_TRACKED_ITEM_DETAILS": ("Changes an item's own name / description / visibility / update instructions. Each field you change needs its `override*` flag set alongside it.", 'iw.TriggerEffect(type=iw.EffectType.MODIFY_TRACKED_ITEM_DETAILS, data={"trackedItemID": mood.id, "overrideName": True, "name": "Temper"})'),
        "PRESENT_CHOICE": ("Offers the player a choice; the picked value(s) land in the target item.", 'iw.TriggerEffect(type=iw.EffectType.PRESENT_CHOICE, data={"message": "Which way?", "choices": "Left\\nRight", "selectionMode": "single", "valueDelimiter": "newline", "minSelections": 1, "maxSelections": 1, "targetTrackedItemId": mood.id})'),
        "REQUEST_INPUT": ("Prompts the player for text; the reply lands in the target item.", 'iw.TriggerEffect(type=iw.EffectType.REQUEST_INPUT, data={"inputMode": "single", "requestText": "Name yourself.", "requiresInput": True, "targetTrackedItemId": mood.id})'),
        "FIRE_RANDOM_TRIGGER": ("Fires one of the listed triggers at random.", 'iw.TriggerEffect(type=iw.EffectType.FIRE_RANDOM_TRIGGER, data=[ambush.id, storm.id])'),
        "CHANGE_VICTORY_CONDITION": ("Replaces the victory condition.", 'iw.TriggerEffect(type=iw.EffectType.CHANGE_VICTORY_CONDITION, data={"condition": "I reach the lighthouse", "text": "You made it."})'),
        "CHANGE_DEFEAT_CONDITION": ("Replaces the defeat condition.", 'iw.TriggerEffect(type=iw.EffectType.CHANGE_DEFEAT_CONDITION, data={"condition": "the crew all die", "text": "Nobody came home."})'),
        "CHANGE_PC_SKILL": ("Raises (`increase=True`) or lowers a skill by `amount`, clamped at `minmax`.", 'iw.TriggerEffect(type=iw.EffectType.CHANGE_PC_SKILL, data={"name": "Nerve", "amount": 1, "minmax": 5, "increase": True})'),
        "CHANGE_OTHER_CHARACTERS": ("Rewrites or removes an NPC. `data` is `{character, action, npc}` — `character` names the one to act on, `action` is an `NPCAction`, and `npc` is the whole NPC as it should end up.", 'iw.TriggerEffect(type=iw.EffectType.CHANGE_OTHER_CHARACTERS, data={"character": ferryman.name, "action": iw.NPCAction.MODIFY, "npc": {"id": ferryman.id, "name": ferryman.name, "detail": "He speaks now."}})'),
        "ENDS_GAME": ("Ends the game. `data` is the `can_continue` value — `False` is a hard ending.", 'iw.TriggerEffect(type=iw.EffectType.ENDS_GAME, data=False)'),
    },
}

# Sections printed after the generated tables, in order.
TAIL_SECTIONS = [
    ("Initial values: `same` / `character` / `player`", """\
A tracked item's `initialValueBasedOnPC` picks where its starting value comes from. The three modes put
that value in three *different places*, which is the part worth knowing:

| mode | the UI's wording | where the value lives |
|---|---|---|
| `SAME` | initial value is always the same | the item's own `initialValue` |
| `CHARACTER` | depends on which character the player chooses | one entry per character under `possibleCharacters[].initialTrackedItemValues`; the item's own `initialValue` stays empty |
| `PLAYER` | can be entered by the player | the item's own `initialValue`, acting as the default the player edits |

Both `PLAYER` and `CHARACTER` can offer the player a **list to choose from** instead of free text — given
either literally or as a `$`-script yielding the options — but each mode carries it on a different object,
and the near-identical field names are easy to mix up:

| | literal choices | script yielding choices | the value itself |
|---|---|---|---|
| `PLAYER` — on the **item** | `initialValueChoices` | `initialValueChoicesScript` | `initialValue` (the default selection) |
| `CHARACTER` — on the **per-character entry** | `initialPCValue` *as a list* | `initialPCValueChoicesScript` | `initialPCValue` |

Per-character entries are not free-form overrides you attach at will: a character carries **one entry per
`CHARACTER`-mode item**, and the entry's own `initialValueBasedOnPC` mirrors the item's. An entry declaring
any other mode has no item it can belong to and is dropped on import.\
"""),
    ("Scripting & structured data", """\
The engine has a `$`-expression scripting language and structured (YAML) tracked items. `iw` models the
enum values and passes the script text through verbatim; the language itself is the engine's.
`TrackedItemDataType.YAML` holds the document, `ConditionType.ON_PAW_SCRIPT` reads an expression, and
`EffectType.RUN_SCRIPT` runs a block. The `TrackedItem` fields the feature needs — `variableName`,
`enforceFormat`, `formatSchema`, `formatExample`, `driftAcknowledgedForName`, and the two
`initialValueChoices*` fields — all default to `None` and strip from output unless set, so worlds
predating the feature serialise unchanged.\
"""),
    ("IDs & helpers", """\
Objects that need an id get one from a shared, deterministic `IDGenerator`, and **nothing in this repo
ever writes one by hand**. `World.from_dict` re-seeds it from the parsed data so ids created afterwards
cannot collide with the parsed world's. `iw.reset_ids()` makes a build reproducible regardless of what was
built before it (the build script calls it).

`set_tracked_item(item, value, action=SET)` and `tracked_item_is(item, value, inequality=IS_EXACTLY)`
build the effect that writes a tracked item and the condition that reads one. **Use them.** The engine's
payload for both carries the item's id *twice* — inside `data`, and again in the sibling `trackedItemID`
field — and nothing checks that the two copies agree; a world whose copies disagree loads perfectly and
silently never fires. Both take the item itself, or a raw id string for engine built-ins like
`turn_number` and `player_action` that are not items in your world. Those two are listed in
`iw.BUILTIN_TRACKED_ITEM_IDS`, which is what stops `validate()` rejecting a trigger that reads one; add
to it if you meet another the engine supplies.

**Every skill is a tracked item too.** The engine makes one per entry in `skills`, named `skill_` plus
the skill's own name lowercased with spaces underscored — a world with `skills=["Skill A", "Skill B"]`
can read `skill_skill_a` and `skill_skill_b`. They never appear in `trackedItems`, so `validate()`
derives them from `skills` rather than being told about them; a skill you rename renames its item.\
"""),
    ("Notes", """\
- Dataclasses use **identity** equality and hashing (`eq=False`), so instances are hashable and can be
  used as dict keys (which is how `plot` keys its stage maps). Two instances with identical fields are
  **not** equal — compare `.to_dict()` if you need value equality.
- Parsing is strict on purpose: an unknown field raises `NotImplementedError` rather than being dropped,
  so the dataclasses cannot quietly fall behind the engine's schema.\
"""),
]
