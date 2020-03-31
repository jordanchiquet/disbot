import asyncio

import callofduty
from callofduty import Mode, Platform, Title


async def getcodstats(user):
    client = await callofduty.Login("jordanchiq@gmail.com", "CoDPass40+2")

    results = await client.SearchPlayers(Platform.BattleNet, user, limit=3)
    for player in results:
        print(f"{player.username} ({player.platform.name})")

    me = results[1]
    profile = await me.profile(Title.ModernWarfare, Mode.Multiplayer)

    level = profile["level"]
    kd = profile["lifetime"]["all"]["properties"]["kdRatio"]
    wl = profile["lifetime"]["all"]["properties"]["wlRatio"]

    print(f"\n{me.username} ({me.platform.name})")
    print(f"Level: {level}, K/D Ratio: {kd}, W/L Ratio: {wl}")

    await client.Logout()

asyncio.get_event_loop().run_until_complete(getcodstats("HotDog94#11957"))