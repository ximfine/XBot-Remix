from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.w(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0)
    await typew.edit("/protecc shuten martha altera Atalante penthesilea quetzalcoatl jinako chevalier artoria qin rhyme mata shiki yi medb osakabehime kiyohime Nightingale yu ke Hokusai Carmilla Mysterious Mae drake europa boudica chacha circe medea murasaki kiara ishtar jeanne jane bradamante brynhildr tomoe gozen irisviel von katou medusa parvati orion stheno euryale nero kingprotea hassan yang abigail illyasviel ereshkigal bb charlotte tamamo chiyome minamoto wu helena ibaraki okita oda mash astolfo mordred nitocris gorgon paul benienma mecha elisabeth gray jack marie anastasia passionlip scheherazade semiramis salome lakshmibai valkyrie anne da fujino nagao")
# Owner @erruuu - @salama219


@register(outgoing=True, pattern='^xx(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0)
    await typew.edit("/protecc mysterious heroine x xx")
# Owner @erruuu - @salama219


@register(outgoing=True, pattern='^.h(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0)
    await typew.edit("/protecc hikari hikari oono kirigaya mio atago gaen araragi chisa yuuna izumi izuna nao ruka rikka erice erika chihiro nakano uesugi yui yukino hanyuu medusa mito mii boudica akari tomoe mami papi kagome beatrice eru kyons sister sae cabashira ichinose rias kanao akeno futaba koneko meteora aoko kyouko shinku youmu ryouko asuna haruhi natsumi lelei margaret")
# Owner @erruuu @salama219


CMD_HELP.update({
    "harem":
    "`s`\
\nUsage: Protecc servant (beta).\
\n\n`h`\
\nUsage: Protecc loli (beta).\
\n\n`xx`\
\nUsage: Protecc servant char mysterious."
})
