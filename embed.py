#!/usr/bin/env python3.7
from discord import Embed, Colour, Client, NotFound

from secret import TOKEN

SERVERID = 235478105177718785  # Foobar
CHANNELID = 235478105177718785  # general
MESSAGEID = 712366202579714099

# SERVERID = 219564389462704130  # Zeusops
# CHANNELID = 287747328264372225  # welcome
# MESSAGEID = 586558085179375636

# zero-width space
indent = "\u200b \u200b \u200b \u200b"

servers = \
"""{0} - **TeamSpeak:** ts.zeusops.com
{0} - **Arma:** arma.zeusops.com, **port**: 2302
{0}
""".format(indent)

important_links = """{0} - [Attendance (zeusops.com/attendance)](https://www.zeusops.com/attendance)
{0} - [Documentation (zeusops.com/doc)](https://www.zeusops.com/doc)
{0} - [Rules (zeusops.com/rules)](https://www.zeusops.com/rules)
{0} - [Zeus Guide (zeusops.com/zeus)](https://www.zeusops.com/zeus)
{0} - [Mission Template (zeusops.com/template)](https://github.com/zeusops/mission-templates)
{0} - [Zeus Feedback Form (zeusops.com/feedback)](https://www.zeusops.com/feedback)
{0} - [HQ Feedback Form (zeusops.com/hqfeedback)](https://www.zeusops.com/hqfeedback)
{0} - [Recruit Review Form (zeusops.com/review)](https://www.zeusops.com/review)
{0} - [CO Meeting Notes (zeusops.com/meetings)](https://www.zeusops.com/meetings)
{0}
""".format(indent)

mods = \
"""{0} - [Mods Default (zeusops.com/mods)](http://www.zeusops.com/mods)
{0} - [Mods Optional (zeusops.com/optional)](https://www.zeusops.com/optional)
{0} - [Extra Terrain Pool (zeusops.com/terrains)](https://www.zeusops.com/terrains)
{0}
""".format(indent)

other_links = \
"""{0} - [Website](https://www.zeusops.com/)
{0} - [Discord (zeusops.com/discord)](https://www.zeusops.com/discord)
{0} - [After-Action Report (AAR)](https://aar.zeusops.com/)
{0} - [A3Units (zeusops.com/units)](https://units.arma3.com/unit/zeusops)
{0} - [Twitter](https://twitter.com/zeusops)
{0} - [Twitch](https://www.twitch.tv/zeusoperations)
{0} - [Patreon](https://www.patreon.com/zeusoperations)
{0} - [PayPal](https://www.paypal.me/ZeusOperations)
{0} - [Steam](https://steamcommunity.com/groups/zeusops)
{0} - [Watch2Gether (zeusops.com/watch)](https://www.zeusops.com/watch)
{0} - [TeamSpeak dark theme](https://www.myteamspeak.com/addons/L2FkZG9ucy82ODYyMDlhZi0wYjY2LTQ4MDUtYjJkNy0wZTk5MGY3Y2I5ZTA%3D)
{0} - [TeamSpeak dark theme icons](https://drive.google.com/open?id=1b_zUlWf8tpUZijimgBK_olFxBUXNZ9V5)
{0} - [Unofficial TeamSpeak sound pack](https://drive.google.com/open?id=1HIsPDL2cjacS8cisygiRVx6O_pJmDBDf)
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

    try:
        message = await channel.fetch_message(MESSAGEID)
    except NotFound:
        await channel.send(content="\u200b\n**Server information**",
                        embed=embed)
    else:
        await message.edit(embed=embed)

    await client.close()


if __name__ == "__main__":
    client.run(TOKEN)

