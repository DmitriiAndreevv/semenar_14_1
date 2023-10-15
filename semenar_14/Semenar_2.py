def clean_text(text: str) -> str:
    """
    Delete symbols from text other than A(a) - Z(z) and space. Return string in lower register.
    >>> clean_text('python')
    'python'
    >>> clean_text('Python')
    'python'
    >>> clean_text('Python это не Java')
    'python but not java'
    >>> clean_text('python - это не ПиТоН')
    'python    '
    >>> clean_text('"Python" - это не "Питон"')
    'python    '
    """
    text = text.lower()
    av_symbols = [chr(code) for code in range(97, 123)]
    av_symbols.append(' ')
    for symbol in text:
        if symbol not in av_symbols:
            text = text.replace(symbol, '')
    return text


if __name__ == '__main__':
    import doctest

    # вывод
    doctest.testmod(verbose=True)
