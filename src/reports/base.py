from abc import ABC, abstractmethod


class BaseReport(ABC):
    registry = {}

    @abstractmethod
    def calculate(self, data: dict) -> list:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseReport.registry[cls().name().lower()] = cls
