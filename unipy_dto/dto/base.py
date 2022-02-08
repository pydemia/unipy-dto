from typing import Optional
from pydantic import BaseModel, validator
from autologging import logged
from ..types.fields import CPUField
from .._modelconfig import (
    MutableDTO, ImmutableDTO,
    MutableDTOConfig, ImmutableDTOConfig
)


__all__ = [
    "CPUSpec",
]


@logged
class CPUSpec(BaseModel):
    cpu_min: float = CPUField
    cpu_max: float = CPUField
    desc: Optional[str]

    @validator("cpu_max", pre=True, always=True, allow_reuse=True)
    def validate_minmax(cls, v, values, **kwargs):
        if v < values["cpu_min"]:
            cls._CPUSpec__log.warn(
                f"'cpu_max' [{v}] is smaller than 'cpu_min' [{values['cpu_min']}].\n" +
                f"replacing it with 'cpu_min' [{values['cpu_min']}]...")
            return values["cpu_min"]
        else:
            return v
