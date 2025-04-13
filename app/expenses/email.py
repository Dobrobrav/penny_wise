import dataclasses


@dataclasses.dataclass
class Email:
    address: str
    subject: str
    content: str
