"""Domain events for squadrons category."""

from ed_models.core.domain.events.squadrons.applied_to_squadron import AppliedToSquadron
from ed_models.core.domain.events.squadrons.invited_to_squadron import InvitedToSquadron
from ed_models.core.domain.events.squadrons.joined_squadron import JoinedSquadron
from ed_models.core.domain.events.squadrons.left_squadron import LeftSquadron
from ed_models.core.domain.events.squadrons.shared_bookmark_to_squadron import (
    SharedBookmarkToSquadron,
)
from ed_models.core.domain.events.squadrons.squadron_created import SquadronCreated
from ed_models.core.domain.events.squadrons.squadron_demotion import SquadronDemotion
from ed_models.core.domain.events.squadrons.squadron_promotion import SquadronPromotion
from ed_models.core.domain.events.squadrons.squadron_startup import SquadronStartup

__all__ = [
    "AppliedToSquadron",
    "InvitedToSquadron",
    "JoinedSquadron",
    "LeftSquadron",
    "SharedBookmarkToSquadron",
    "SquadronCreated",
    "SquadronDemotion",
    "SquadronPromotion",
    "SquadronStartup",
]
