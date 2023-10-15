def clean_text(text: str) -> str:
    text = text.lower()
    av_symbols = [chr(code) for code in range(97, 123)]
    av_symbols.append(' ')
    for symbol in text:
        if symbol not in av_symbols:
            text = text.replace(symbol, '')
    return text


if __name__ == '__main__':
    print(clean_text('Python is the most popular programming language'))
