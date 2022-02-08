from pydantic import BaseModel, BaseSettings, Extra
from typing import Dict, List, Any, NamedTuple, Optional

import json
from pathlib import Path


__all__ = [
    "MutableDTOConfig",
    "ImmutableDTOConfig",
]

class _BaseDTOConfig:
    env_file_encoding = "utf-8"
    case_sensitive = True
    extra = Extra.allow
    validate_assignment = True


class MutableDTOConfig(_BaseDTOConfig):
    allow_mutation = True


class ImmutableDTOConfig(_BaseDTOConfig):
    allow_mutation = False


class BaseDTO(BaseModel):
    class Config(_BaseDTOConfig):
        pass


class MutableDTO(BaseModel):
    class Config(MutableDTOConfig):
        pass


class ImmutableDTO(BaseModel):
    class Config(ImmutableDTOConfig):
        pass
