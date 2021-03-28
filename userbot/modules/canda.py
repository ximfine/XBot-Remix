from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Woii...**")
    sleep(2)
    await typew.edit("`Ganteng doang`")
    sleep(2)
    await typew.edit("`Jemput cewe depan gang`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Woii...**")
    sleep(2)
    await typew.edit("`Ganteng doang`")
    sleep (2)
    await typew.edit("`Ganteng doang jemput cewe depan gang`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^.c(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Cantik doang`")
    sleep(1)
    await typew.edit("`Tapi chat cowok lebih dari satu`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^.c(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Cantik doang`")
    sleep(1)
    await typew.edit("`Tapi chat cowok lebih dari satu`")
# Owner @Si_Dian

@register(outgoing=True, pattern='^.brokn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit(f"**I'M A BROKENT HOME.**")
    sleep(5)
    await typew.edit("`Tangisan hanya mengacaukan segalanya tapi senyuman membuat mereka yakin aku Tegar`")
    sleep(5)
    await typew.edit("`Setiap anak ingin keluarga yang sempurna\ntapi tidak semua anak memilikinya`")
    sleep(5)
    await typew.edit("`Sayangilah kedua orang tuamu dengan\nsepenuh hati selagi masih ada🙂`")


@register(outgoing=True, pattern='^.oe(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**oee....**")
    sleep(3)
    await typew.edit("`Muka kalian 8 bit...`")
    sleep(3)
    await typew.edit("`Kayak Monyet`")
    sleep(3)
    await typew.edit("`Muka gw Gak Burik Kek Kalian`")


@register(outgoing=True, pattern='^.tidr(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Eh, beban keluarga tdr woi**")
    sleep(2)
    await typew.edit("`Sadar gadangnya bukan untukmu.`")
    sleep(2)
    await typew.edit("`Melainkan untuk dia di akun satu`")


@register(outgoing=True, pattern='^.pc(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Eh, yelah pc doang jadian kagak**")
    sleep(2)
    await typew.edit("`Percuma Jadian putus iya, ngewe kgk.`")
    sleep(2)
    await typew.edit("`Canda ngewe:v`")
    sleep(2)
    await typew.edit("`Awoawok Canda monyet`")


@register(outgoing=True, pattern='^.tbat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Eh beban keluarga**")
    sleep(2)
    await typew.edit("`Bapak lu kerja keras nafkahin keluarga`")
    sleep(2)
    await typew.edit("`Anaknya kelakuannya kek sempak Dajjal!!`")
    sleep(2)
    await typew.edit("`Tobat sadar lu anak haram`")


@register(outgoing=True, pattern='^.gbt(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Nyanyi dikit bolehlah ya:v**")
    sleep(2)
    await typew.edit("`Du🤸‍♂️`")
    sleep(2)
    await typew.edit("`Du du 🤸‍♂️`")
    sleep(0.5)
    await typew.edit("`Du du du🤸‍♂️`")
    await typew.edit("`Du🤸‍♂️`")
    sleep(2)
    await typew.edit("`Du du 🤸‍♂️`")
    sleep(0.5)
    await typew.edit("`Du du du🤸‍♂️`")
    sleep(0.5)
    await typew.edit("`Aye aye kimochi:v`")
    sleep(2)
    await typew.edit("`Asw Gabut bet gw:v`")


CMD_HELP.update({
    "canda":
    "`.g`\
\nUsage: Untuk nyindir laki.\
\n\n`.c`\
\nUsage: Untuk nyindir cewe.\
\n\n`.brokn`\
\nUsage: Liat aja dah sendiri.\
\n\n.`oe`\
\nUsage: Buat ngatain orang.\
\n\n`.pc`\
\nUsage: Buat ngatain orang yg sllu pc.\
\n\n`.tbat`\
\nUsage: Tobat woi tobat.\
\n\n`.gbt`\
\nUsage: Buat lu pada yang gabut."
})
