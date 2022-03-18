import asyncio

import discord
from discord.ext import commands

from bot_function import config_bot, get_badword

list_bad_word = get_badword()
config = config_bot()
mute_time = config["mute_time"]
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(f'Bot is online!'))
    print('Bot dang chay: {0.user}'.format(client))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.mention} | Làm ơn hãy điền những tham số bị thiếu! :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention} | Bạn không có quyền để sử dụng câu lệnh! :angry:")
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**Này này! Bạn phải chờ `{:.2f}s` để sử dụng lại lệnh đó** :angry:'.format(error.retry_after)
        delete_msg = await ctx.send(msg)
        await asyncio.sleep(int(error.retry_after))
        await delete_msg.delete()


@client.command(brief='ping', description='kiểm tra độ trễ của Bot')
@commands.cooldown(5, 10000, commands.BucketType.user)
async def ping(ctx):
    await ctx.send(f'{ctx.author.mention} | in {round(client.latency * 1000)}ms')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    if message.content.startswith(':D'):
        print("hello")

    else:
        msg = msg.split(' ')
        for word in msg:
            if word.lower() in list_bad_word:
                guild = message.guild
                channel = client.get_channel(config["id_channel_send"])
                delete_message = message
                await delete_message.delete()

                for role in guild.roles:
                    if role.name == "Muted":
                        await message.author.add_roles(role)
                        ping = await channel.send(f'{message.author.mention}')
                        await ping.delete()
                        embed_mute = discord.Embed(title=f"{message.author}", description="", color=0xff7373)
                        embed_mute.add_field(name=f"Mute {mute_time}s", value=f"Lí do: Nói bậy", inline=False)
                        embed_mute.add_field(name=f"Nội dung tin nhắn:", value=f"{message.content}", inline=False)
                        embed_mute.add_field(name=f"Tin nhắn được gửi tại kênh:", value=f"{message.channel}",
                                             inline=False)
                        embed_mute.add_field(name=f"Lưu ý:",
                                             value=f"Nếu bạn không nói tục mà bot warn thì hãy nhắn tin tới {config['author']} để được gỡ mute.",
                                             inline=False)
                        await channel.send(embed=embed_mute)

                        await asyncio.sleep(mute_time)

                        await message.author.remove_roles(role)
                        await channel.send(f'{message.author.mention} Hết bị mute gòi nha')
                break

    await client.process_commands(message)


client.run(config["TOKEN"])
