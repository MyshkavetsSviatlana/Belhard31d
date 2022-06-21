import asyncio
from aiohttp import ClientSession


class OnlinerAPI(object):
    HOST: str = "https://catalog.onliner.by"

    @staticmethod
    def create_session(func):
        async def wrapper(**kwargs):
            async with ClientSession(base_url=OnlinerAPI.HOST) as session:
                return await func(**kwargs, session=session)

        return wrapper

    @staticmethod
    @create_session
    async def get_response(category: str, article: str, page: int, session: ClientSession = None):
        response = await session.get(
            url=f'/sdapi/catalog.api/search/{category}?page={page}'
        )
        if response.status == 200:
            data = await response.json()

            lst = []
            for key in data['products']:
                lst.append(key)
            for i in lst:
                for _ in i:
                    if article in i.values():
                        page = data['page']['current']
                        print(page)
                        position = lst.index(i)
                        print(position)
                        print(i)
                        return category, article, page, position


async def main():
    result = await OnlinerAPI.get_response(category='notebook', article='k413eaeb1654')
    print(result)


if __name__ == '__main__':
    asyncio.run(main())
