import asyncio
import aiohttp
import pysmartthings
from specs import getGlobal

# https://pypi.org/project/pysmartthings/

token = getGlobal('Olive', 'token')

async def print_devices():
    async with aiohttp.ClientSession() as session:
        api = pysmartthings.SmartThings(session, token)
        locations = await api.locations()
        for l in locations:
            if 'Olive' == l.name:
                print(l.location_id)

        devices = await api.devices()
        for d in devices:
            print(d.label)
    

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_devices())
    loop.close()

if __name__ == '__main__':
    main()
