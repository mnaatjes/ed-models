"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class Fileheader(JournalEvent):
    """The heading entry is added at the beginning of every file. The first event in a new journal file. If the play session goes on a long time, and the journal gets very large, the file will be closed and a new file is started with an increased part number. See also the {@link Continued} event."""

    part: int | float | None = None
    Odyssey: bool | None = None
    language: str | None = None
    gameversion: str | None = None
    build: str | None = None
