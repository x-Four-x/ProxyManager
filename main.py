import asyncio

from models import Proxy as ProxyModel
from enums import ProxyType
from proxy import Proxy


def load_proxies() -> list[ProxyModel]:
    with open("proxies.txt", "r") as f:
        lines = f.readlines()

    proxies = []

    for line in lines:
        ip, port, user, password = line.strip().split(":")
        proxies.append(
            Proxy(
                ProxyModel(
                    type=ProxyType.SOCKS5,
                    ip=ip,
                    port=port,
                    user=user,
                    password=password
                )
            )
        )

    return proxies




class ProxyManager:
    def __init__(self) -> None:
        self.proxies: list[Proxy] = load_proxies()

    async def get_proxy(self) -> Proxy | None:
        for proxy in self.proxies:
            if await proxy.check():
                return proxy

        return None

async def main():
    proxy_manager = ProxyManager()

    proxy = await proxy_manager.get_proxy()
    print(proxy)

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
