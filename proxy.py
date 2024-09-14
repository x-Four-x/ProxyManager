import aiohttp

from models import Proxy as ProxyModel


class Proxy:
    def __init__(self, proxy_model: ProxyModel):
        self.proxy_model = proxy_model

    @property
    def url(self) -> str:
        return self.proxy_model.url

    async def check(self, attempts: int = 0) -> bool:
        if attempts >= 2:
            return False
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                    "https://httpbin.org/ip",
                    proxy=self.url,
                    timeout=aiohttp.ClientTimeout(total=10)
                ) as response:
                    return response.status == 200
            except:
                return await self.check(attempts + 1)
            
    def __str__(self) -> str:
        return f"<Proxy {self.proxy_model.ip}:{self.proxy_model.port}>"
