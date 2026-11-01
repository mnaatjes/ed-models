"""Combined PowerState enumeration."""

from ed_models.core.domain.types.power_state1 import PowerState1
from ed_models.core.domain.types.power_state2 import PowerState2

type PowerState = PowerState1 | PowerState2
