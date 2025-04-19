import dataclasses


@dataclasses.dataclass(frozen=True)
class Email:
    address: str
    subject: str
    content: str


@dataclasses.dataclass(frozen=True)
class Report:
    content: str
