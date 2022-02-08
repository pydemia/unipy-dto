from pydantic import (
    BaseModel,
    NegativeFloat,
    NegativeInt,
    PositiveFloat,
    PositiveInt,
    # NonNegativeFloat, # 5.6 heeseok : 실행 시 오류 발생하여 주석 처리함.
    # NonNegativeInt,   # 5.6 heeseok : 실행 시 오류 발생하여 주석 처리함.
    # NonPositiveFloat, # 5.6 heeseok : 실행 시 오류 발생하여 주석 처리함.
    # NonPositiveInt,   # 5.6 heeseok : 실행 시 오류 발생하여 주석 처리함.
    conbytes,
    condecimal,
    confloat,
    conint,
    conlist,
    conset,
    constr,
    Field,
)

__all__ = [
    "DESCField",
    "MEMField",
    "CPUField",
    "GPUField",
    "K8SNAMEField",
    "REPLICAField",
    "CONCURRENCYField",
    "NODENAMEField",
    "NODESELECTORField",
    "CANARYWEIGHTField"
]


MEMField = Field(
    2, title="Memory 크기",
    ge=0.1, le=128, multiple_of=0.1,
)
CPUField = Field(
    1, title="CPU 크기",
    ge=0.1, le=64, multiple_of=0.1,
)
GPUField = Field(
    0, title="GPU 개수",
    ge=0, le=8, multiple_of=1,
)

REPLICAField = Field(
    1, title="replica 값",
    ge=0, le=10_000, multiple_of=1,
)

CONCURRENCYField = Field(
    100, title="concurrency 값",
    ge=1, le=10_000, multiple_of=1,
)

K8SNAMEField = Field(
    "", title="k8s namespace",
    max_length=200,
)

DESCField = Field(
    "", title="description text",
    max_length=2_000,
)

NODENAMEField = Field(
    None, title="node name",
    max_length=200,
)

NODESELECTORField = Field(
    None, title="nodeSelector 값",
    max_length=200,
)

CANARYWEIGHTField = Field(
    10, title="concurrency 값",
    ge=0, le=100, multiple_of=10,
)
