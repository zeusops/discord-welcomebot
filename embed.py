#!/usr/bin/env python3.7
from discord import Embed, Colour, Client

from secret import TOKEN

SERVERID = 235478105177718785  # Foobar
CHANNELID = 235478105177718785  # general

# SERVERID = 219564389462704130  # Zeus Operations
# CHANNELID = 287747328264372225  # welcome

# zero-width space
indent = "\u200b \u200b \u200b \u200b"

servers = \
"""{0} - **TeamSpeak:** ts.zeusops.com
{0} - **Arma:** arma.zeusops.com:2302
{0}
""".format(indent)

important_links = """{0} - [Attendance, missions & statistics](https://docs.google.com/spreadsheets/d/1obK3_FU5yMzhBgFLmk3g0v5dn5wFqT30RQXHWCAccCQ/edit)
{0} - [Documentation](https://docs.google.com/document/d/1NKLi_VazqMgpnZYHa6FDOQbZyfqLDPosi4xdOQPgHMU/edit?usp=sharing)
{0} - [Rules](https://docs.google.com/document/d/1DWK53LF3AjRqxZkb4qQXeBBvtSIOtamnUXyk2b6aaAs/edit?usp=sharing)
{0} - [Zeus Guide](https://docs.google.com/document/d/1PFK__UcgmAJ1P3xBnJxeW2ow7u8bgEfM8lkpHJrLYDU/edit?usp=sharing)
{0} - [Mission Templates (GitHub)](https://github.com/zeusops/mission-templates)
{0} - [Mission Templates (single PBO)](https://drive.google.com/file/d/1NuDd5Z9tEmc0wCf6MhzZe697BgBig-0p/view?usp=sharing)
{0}
""".format(indent)

mods = \
"""{0} - [Mods Default](http://steamcommunity.com/sharedfiles/filedetails/?id=754233724)
{0} - [Mods WWII](https://steamcommunity.com/sharedfiles/filedetails/?id=1314684259)
{0} - [Mods Optional](https://steamcommunity.com/sharedfiles/filedetails/?id=1115077330)
{0} - [Extra Terrain Pool](https://steamcommunity.com/sharedfiles/filedetails/?id=1424089214)
{0}
""".format(indent)

other_links = \
"""{0} - [Website](https://www.zeusops.com/)
{0} - [Discord](https://www.zeusops.com/discord)
{0} - [Steam](https://steamcommunity.com/groups/zeusops)
{0} - [A3Units](https://units.arma3.com/unit/zeusops)
{0} - [Twitter](https://twitter.com/zeusops)
{0} - [Facebook](https://www.facebook.com/zeusoperations/)
{0} - [Twitch](https://www.twitch.tv/communities/zeusoperations)
{0} - [Patreon](https://www.patreon.com/zeusoperations)
{0} - [PayPal](https://www.paypal.me/ZeusOperations)
{0} - [Watch2Gether](https://www.watch2gether.com/rooms/zeusoperations-p7wbtfre05cwi65s)
{0} - [TeamSpeak dark theme](https://www.myteamspeak.com/addons/686209af-0b66-4805-b2d7-0e990f7cb9e0)
{0} - [TeamSpeak dark theme icons](https://drive.google.com/open?id=1b_zUlWf8tpUZijimgBK_olFxBUXNZ9V5)
""".format(indent)

client = Client()


@client.event
async def on_ready():
    server = client.get_guild(SERVERID)
    channel = server.get_channel(CHANNELID)
    embed = Embed(colour=Colour(0xe01c2e))

    embed.add_field(name="Servers:", value=servers,
                    inline=False)
    embed.add_field(name="Important links", value=important_links,
                    inline=False)
    embed.add_field(name="Mods", value=mods,
                    inline=False)
    embed.add_field(name="Other links", value=other_links,
                    inline=False)

    await channel.send(content="\u200b\n**Server information**",
                       embed=embed)

    await client.logout()


if __name__ == "__main__":
    client.run(TOKEN)

