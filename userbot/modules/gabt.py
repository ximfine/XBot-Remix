from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.ohayou(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`ohayou Sekai`")
    sleep(3)
    await typew.edit("`Morning Lord`")
    sleep(1)
    await typew.edit("`Ohayou Sekai Morning Lord:)`")
# @salama219


@register(outgoing=True, pattern='^.syg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Sayang aku`")
    sleep(3)
    await typew.edit("`Cuma mau bilang`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
    sleep(2) 
    await typew.edit("`Jangan Tinggalin aku ya`")
# @salama219


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Tetap Semangat`")
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# @salama219
