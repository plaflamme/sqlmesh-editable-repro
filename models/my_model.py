import typing as t
from datetime import datetime
import pandas as pd
from sqlmesh import ExecutionContext
from sqlmesh import model
from sqlmesh.core.model.kind import ModelKindName
from editable_repro.my_module import my_function


@model(
    "foo.my_model",
    kind=ModelKindName.FULL,
    columns={"a": "int", "b": "string", "c": "float"},
)
def my_model(
    ctx: ExecutionContext,
    start: datetime,
    end: datetime,
    execution_time: datetime,
    **kwargs: t.Any,
):
    my_function()
    return pd.DataFrame([], columns=["a", "b", "c"])
