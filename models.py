import pydantic

from enums import ProxyType


class Proxy(pydantic.BaseModel):
    type: ProxyType
    ip: str
    port: int
    user: str
    password: str


    @property
    def url(self) -> str:
        return f"{self.type.value}://{self.user}:{self.password}@{self.ip}:{self.port}"
