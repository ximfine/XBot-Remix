# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Created By @ximfine

import os
import requests
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.dec(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Reply to any user message.`")
        return
    reply_message = await event.get_reply_message()
    # if not reply_message.text:
    # await event.edit("```reply to file message```")
    # return
    chat = "@decryptorxbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Reply to actual users message.`")
        return
    await event.edit("`Decrypting Config...`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1959977163))
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("`Please unblock @decryptorxbot  and try again`")
            return
        if response.text.startswith("Forward"):
            await event.edit("`can you kindly disable your forward privacy settings for good?`")
        else:
            await event.edit(f"{response.message.message}")


@register(outgoing=True, pattern=r"^\.gen(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan bin yang mau di generate!..__")
    await event.edit(f"```Generated CC {query}..```")
    async with bot.conversation("@TorpedoXx_Bot") as conv:
        try:
            jemboed = await conv.send_message(f"/gen {query}")
            await asyncio.sleep(2)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"Gagal generate {query}!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@register(outgoing=True, pattern=r"^\.chk(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan cc yang mau di check!..__")
    await event.edit("```Checking CC Number..```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/ss {query}")
            await asyncio.sleep(10)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"Gagal Mengecek {query}!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@register(outgoing=True, pattern=r"^\.bin(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan BIN yang mau di check!..__")
    await event.edit(f"```Checking BIN {query}```")
    async with bot.conversation("@xcardingxbot") as conv:
        try:
            jemboed = await conv.send_message(f"/bin {query}")
            await asyncio.sleep(10)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"Bin {query} Invalid!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@register(outgoing=True, pattern=r"^\.skey(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan SK-KEY yang mau di check!..__")
    await event.edit(f"```Checking SK KEY {query}```")
    async with bot.conversation("@xcardingxbot") as conv:
        try:
            jemboed = await conv.send_message(f"/key {query}")
            await asyncio.sleep(10)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit("SK KEY Invalid!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@register(outgoing=True, pattern=r"^\.nmap(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan domain yang mau di check!..__")
    await event.edit(f"```Getting info {query}..```")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/nmap {query}")
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @scriptkiddies_bot atau chat dulu")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@register(outgoing=True, pattern=r"^\.subd(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan domain yang mau di generate!..__")
    await event.edit(f"```Generated subdomain {query}..```")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/subdomain {query}")
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @scriptkiddies_bot atau chat dulu")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@register(outgoing=True, pattern=r"^\.cekhttp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan domain yang mau di check!..__")
    await event.edit(f"```Checking Respond {query}..```")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/httpheader {query}")
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @scriptkiddies_bot atau chat dulu")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])



@register(outgoing=True, pattern="^.xbin(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan BIN yang mau di check!..__")
    await event.edit(f"```Checking BIN {query}```")
    input = event.text.split(" ", maxsplit=1)[1]
    url = requests.get(f"https://bins-su-api.now.sh/api/{input}")
    res = url.json()
    vendor = res['data']['vendor']
    type = res['data']['type']
    level = res['data']['level']
    bank = res['data']['bank']
    country = res['data']['country']  
    me = (await event.client.get_me()).username
    await event.edit(f"➤ Valid Bin ✅\n\nBin: {input}\nVendor: {vendor}\nType: {type}\nLevel: {level}\nBank: {bank}\nCountry: {country}\n\nChecked By: @{me}\n")
            




CMD_HELP.update({
    "xphreaker":
    "**HELP FOR XPHREAKER**\
\n╭━━━━━━━━━━━━━━━━━━━╮\
\n  `.gen <bin>`\
\n   Usage: to generate cc with bin.\
\n\n  `.chk <cc>`\
\n   Usage: to check respond cc.\
\n\n  `.bin <bin number>`\
\n   Usage: to cek bin information.\
\n\n  `.skey <SK-KEY>`\
\n   Usage: to check skkey respond.\
\n\n  `.nmap <domain hosts>`\
\n   Usage: to get info bug/host.\
\n\n  `.subd <domain hosts>`\
\n   Usage: to get subdomain bug/host.\
\n\n  `.cekhttp <domain hosts>`\
\n   Usage: to cek respons bug/host.\
\n╰━━━━━━━━━━━━━━━━━━━╯"
})
