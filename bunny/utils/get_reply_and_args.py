async def get_reply_and_args(m):
    reply = m.reply_to_message
    if not len(m.command) > 1:
        args = None
    else:
        args = m.text.split(None, 1)[1]
    if not reply:
        type = None 
    elif reply.photo:
        type = "photo"
    elif reply.video:
        type = "video"
    elif reply.animation:
        type = "animation"
    elif reply.document:
        type = "document"
    elif reply.audio:
        type = "audio"
    elif reply.voice:
        type = "voice"
    elif reply.sticker:
        type = "sticker"
    elif reply.text:
        type = "text"
    else:
        type = None
    if reply:
        if reply.caption:
            type += "-caption"
    return type, args
    
        
