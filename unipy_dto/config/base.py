from pydantic import BaseModel, BaseSettings, validator, Extra, ValidationError
from pydantic.dataclasses import dataclass
from ..types import CPUField
from ..dto import CPUSpec

from .. import MutableDTOConfig, ImmutableDTOConfig

import json
from pathlib import Path
from os import path, environ

from typing import Dict, List, Any, NamedTuple, Optional
from collections import namedtuple
from autologging import logged


__all__ = [
    "JsonConfig",
    "EnvConfig",
    "DotEnvConfig",
]


def _json_config_settings_source(settings: BaseSettings) -> Dict[str, Any]:
    # env_file = settings.__config__.env_file
    encoding = settings.__config__.env_file_encoding
    return json.loads(Path("config.json").read_text(encoding))


@logged
class JsonConfig(BaseSettings):
    """
    JSON Configuration.
    Extra fields can be allowed, forbidden or ignored by
    Extra.{allow, forbid, ignore}.
    """
    app_name: str = "JsonConfig"
    use_yn: bool = False
    is_test: bool
    wrong_integer_field: int
    proper_integer_field: int
    clip_values_between_10_and_20: int
    cpu_spec: CPUSpec

    class Config(ImmutableDTOConfig):
        # Disable 'env_file' to avoid this errors:
        # 'Python-dotenv could not parse statement starting at line ...'
        # env_file = "config.json"
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = Extra.allow
        allow_mutation = False
        validate_assignment = True

        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                init_settings,
                _json_config_settings_source,
                env_settings,
                file_secret_settings,
            )

    @validator("wrong_integer_field", "proper_integer_field", always=True)
    def force_typecast_to_int(cls, v):
        if not isinstance(v, int):
            return int(v)
        else:
            return v

    @validator("clip_values_between_10_and_20", always=True)
    def clip_between_10_and_20(cls, v):
        if v < 10:
            return 10
        elif v > 20:
            return 20
        else:
            return v


@logged
class EnvConfig(BaseSettings):
    """
    DOTENV Configuration.
    Extra fields can be allowed, forbidden or ignored by
    Extra.{allow, forbid, ignore}.
    """
    app_name: str = "EnvConfig"
    use_yn: bool = False
    is_test: Optional[bool]
    OS_DIST: str
    cpu_spec: CPUSpec

    class Config(ImmutableDTOConfig):
        env_nested_delimiter = "__"
        case_sensitive = True
        extra = Extra.allow
        allow_mutation = True
        validate_assignment = True


@logged
class DotEnvConfig(BaseSettings):
    """
    DOTENV Configuration.
    Extra fields can be allowed, forbidden or ignored by
    Extra.{allow, forbid, ignore}.
    """
    app_name: str = "DotEnvConfig"
    use_yn: bool = False
    is_test: bool
    wrong_integer_field: int
    proper_integer_field: int
    clip_values_between_10_and_20: int
    cpu_spec: CPUSpec

    class Config(ImmutableDTOConfig):
        env_file = "config.env"
        env_file_encoding = "utf-8"
        extra = Extra.allow
        allow_mutation = False
        validate_assignment = True
        # env_prefix = "__"
        env_nested_delimiter = "__"

    @validator("wrong_integer_field", "proper_integer_field", always=True)
    def force_typecast_to_int(cls, v):
        if not isinstance(v, int):
            return int(v)
        else:
            return v

    @validator("clip_values_between_10_and_20", always=True)
    def clip_between_10_and_20(cls, v):
        if v < 10:
            return 10
        elif v > 20:
            return 20
        else:
            return v
