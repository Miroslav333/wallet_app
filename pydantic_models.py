import pydantic


class Operation(pydantic.BaseModel):
    operation: str
    amount: int

