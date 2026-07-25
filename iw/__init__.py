"""`iw` — build Infinite Worlds world JSON from Python.

    import iw              # the data model: a 1-1 mirror of the Infinite Worlds objects
    from iw import plot    # the plot compiler: PlotStage, PlotStageDetails, PlotTransition, add_plot(s)
    from iw import tools   # convenience constructors for the tracked-item trigger payloads

`iw.iw`'s public API is re-exported here, so `iw.World(...)` works after a plain `import iw`. `plot` and
`tools` stay behind their own names on purpose: they are layers on top of the model, not part of it.
"""

from .iw import *
from .iw import reset_ids, BUILTIN_TRACKED_ITEM_IDS
from . import plot
from . import tools
