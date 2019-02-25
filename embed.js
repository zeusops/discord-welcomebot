const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
  const channel = client.guilds.find(x => x.id === '235478105177718785').channels.find(x => x.id === '235478105177718785')
  console.log(channel.name)
  channel.send("asd")

  const embed = {
    "color": 14687278,
    "fields": [
      {
        "name": "Servers:",
        "value": "    - **TeamSpeak:** ts.zeusops.com\n    - **Arma:** arma.zeusops.com:2302"
      },
      {
        "name": "Important links",
        "value": "    - [Attendance, missions & statistics](https://docs.google.com/spreadsheets/d/1obK3_FU5yMzhBgFLmk3g0v5dn5wFqT30RQXHWCAccCQ/edit)\n    - [Documentation](https://docs.google.com/document/d/1NKLi_VazqMgpnZYHa6FDOQbZyfqLDPosi4xdOQPgHMU/edit?usp=sharing)\n    - [Rules](https://docs.google.com/document/d/1DWK53LF3AjRqxZkb4qQXeBBvtSIOtamnUXyk2b6aaAs/edit?usp=sharing)\n    - [Zeus Guide](https://docs.google.com/document/d/1PFK__UcgmAJ1P3xBnJxeW2ow7u8bgEfM8lkpHJrLYDU/edit?usp=sharing)\n    - [Mission Templates (GitHub)](https://github.com/zeusops/mission-templates)\n    - [Mission Templates (single PBO)](https://drive.google.com/file/d/1NuDd5Z9tEmc0wCf6MhzZe697BgBig-0p/view?usp=sharing)"
      },
      {
        "name": "Mods",
        "value": "    - [Mods Default](http://steamcommunity.com/sharedfiles/filedetails/?id=754233724)\n    - [Mods WWII](https://steamcommunity.com/sharedfiles/filedetails/?id=1314684259)\n    - [Mods Optional](https://steamcommunity.com/sharedfiles/filedetails/?id=1115077330)\n    - [Extra Terrain Pool](https://steamcommunity.com/sharedfiles/filedetails/?id=1424089214)"
      },
      {
        "name": "Other links",
        "value": "    - [Website](https://www.zeusops.com/)\n    - [Discord](https://www.zeusops.com/discord)\n    - [Steam](https://steamcommunity.com/groups/zeusops)\n    - [A3Units](https://units.arma3.com/unit/zeusops)\n    - [Twitter](https://twitter.com/zeusops)\n    - [Facebook](https://www.facebook.com/zeusoperations/)\n    - [Twitch](https://www.twitch.tv/communities/zeusoperations)\n    - [Patreon](https://www.patreon.com/zeusoperations)\n    - [PayPal](https://www.paypal.me/ZeusOperations)\n    - [Watch2Gether](https://www.watch2gether.com/rooms/zeusoperations-p7wbtfre05cwi65s)\n    - [TeamSpeak dark theme](https://www.myteamspeak.com/addons/686209af-0b66-4805-b2d7-0e990f7cb9e0)\n    - [TeamSpeak dark theme icons](https://drive.google.com/open?id=1b_zUlWf8tpUZijimgBK_olFxBUXNZ9V5)"
      }
    ]
  };
  channel.send("**Server information**", { embed });

});

client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('Pong!');
  }
});

client.login('token');
