__all__ = ('text_preparation',)

async def text_preparation(text: str) -> str:
    """Prepares the text for sending so that during parsing the text Telegram error is not in

    Args:
        text (str): sourse text

    Returns:
        str: ready for send text
    """
    return text.replace("_", '\\_') \
            .replace("*", '\\*') \
            .replace("[", '\\[') \
            .replace("]", '\\]') \
            .replace("(", '\\(') \
            .replace(")", '\\)') \
            .replace("~", '\\~') \
            .replace("`", '\\`') \
            .replace(">", '\\>') \
            .replace("#", '\\#') \
            .replace("+", '\\+') \
            .replace("-", '\\-') \
            .replace("=", '\\=') \
            .replace("|", '\\|') \
            .replace("{", '\\{') \
            .replace("}", '\\}') \
            .replace(".", '\\.') \
            .replace("!", '\\!')
