from typing import Any

from mlflow.entities._mlflow_object import _MlflowObject
from mlflow.entities.logged_model_output import LoggedModelOutput


class RunOutputs(_MlflowObject):
    """RunOutputs object."""

    def __init__(self, model_outputs: list[LoggedModelOutput]) -> None:
        self._model_outputs = model_outputs

    def __eq__(self, other: _MlflowObject) -> bool:
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    @property
    def model_outputs(self) -> list[LoggedModelOutput]:
        """Array of model outputs."""
        return self._model_outputs

    def to_dictionary(self) -> dict[Any, Any]:
        return {
            "model_outputs": self.model_outputs,
        }