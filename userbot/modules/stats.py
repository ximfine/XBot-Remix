"""Count the Number of Dialogs you have in your Telegram Account
Syntax: .stats"""
import logging
import time
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING)
logger = logging.getLogger(__name__)


@register(outgoing=True, pattern=r"^.stats(?: |$)(.*)")
async def stats(event: NewMessage.Event) -> None:  # pylint: disable = R0912, R0914, R0915
    """Command to get stats about the account"""
    await event.edit('`Collecting stats, Wait Master`')
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity

        if isinstance(entity, Channel):
            # participants_count = (await event.get_participants(dialog,
            # limit=0)).total
            if entity.broadcast:
                broadcast_channels += 1
                if entity.creator or entity.admin_rights:
                    admin_in_broadcast_channels += 1
                if entity.creator:
                    creator_in_channels += 1

            elif entity.megagroup:
                groups += 1
                # if participants_count > largest_group_member_count:
                #     largest_group_member_count = participants_count
                if entity.creator or entity.admin_rights:
                    # if participants_count > largest_group_with_admin:
                    #     largest_group_with_admin = participants_count
                    admin_in_groups += 1
                if entity.creator:
                    creator_in_groups += 1

        elif isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1

        elif isinstance(entity, Chat):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1

        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time

    full_name = inline_mention(await event.client.get_me())
    response = f'🔸 **Stats for {full_name}** \n\n'
    response += f'**Private Chats:** {private_chats} \n'
    response += f'   • `Users: {private_chats - bots}` \n'
    response += f'   • `Bots: {bots}` \n'
    response += f'**Groups:** {groups} \n'
    response += f'**Channels:** {broadcast_channels} \n'
    response += f'**Admin in Groups:** {admin_in_groups} \n'
    response += f'   • `Creator: {creator_in_groups}` \n'
    response += f'   • `Admin Rights: {admin_in_groups - creator_in_groups}` \n'
    response += f'**Admin in Channels:** {admin_in_broadcast_channels} \n'
    response += f'   • `Creator: {creator_in_channels}` \n'
    response += f'   • `Admin Rights: {admin_in_broadcast_channels - creator_in_channels}` \n'
    response += f'**Unread:** {unread} \n'
    response += f'**Unread Mentions:** {unread_mentions} \n\n'
    response += f'__It Took:__ {stop_time:.02f}s \n'

    await event.edit(response)


@register(outgoing=True, pattern=r"^\.ustat")
async def _(event):
    if event.fwd_from:
        return
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not event.reply_to_msg_id:
        await event.edit("**Silahkan reply di user goblok!**")
        return
    if input_str:
        try:
            uid = int(input_str)
        except ValueError:
            try:
                u = await event.client.get_entity(input_str)
            except ValueError:
                await edit.event("`Silahkan reply di user goblok!`"
                                 )
            uid = u.id
    else:
        uid = reply_message.sender_id
    chat = "@tgscanrobot"
    event = await event.edit("`Checking Group user...`")
    async with bot.conversation(chat) as conv:
        try:
            await conv.send_message(f"{uid}")
        except YouBlockedUserError:
            await steal.reply(
                "```Mohon Unblock @tgscanrobot Dan Coba Lagi```"
            )
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.edit(response.text)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


CMD_HELP.update(
    {
        "stats": ">`.stats`"
        "\nUsage: To check user stats"
        "\n\n>`.ustat`"
        "\nUsage: to check user group join"
    }
)
