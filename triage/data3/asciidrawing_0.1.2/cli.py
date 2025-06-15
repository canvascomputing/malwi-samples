# asciidraw/core.py

ascii_font = {
    'A': ['  A  ', ' A A ', 'AAAAA', 'A   A', 'A   A'],
    'B': ['BBBB ', 'B   B', 'BBBB ', 'B   B', 'BBBB '],
    'C': [' CCC ', 'C    ', 'C    ', 'C    ', ' CCC '],
    'D': ['DDDD ', 'D   D', 'D   D', 'D   D', 'DDDD '],
    'E': ['EEEEE', 'E    ', 'EEEEE', 'E    ', 'EEEEE'],
    'F': ['FFFFF', 'F    ', 'FFFFF', 'F    ', 'F    '],
    'G': [' GGG ', 'G    ', 'G  GG', 'G   G', ' GGG '],
    'H': ['H   H', 'H   H', 'HHHHH', 'H   H', 'H   H'],
    'I': ['IIIII', '  I  ', '  I  ', '  I  ', 'IIIII'],
    'J': [' JJJJ', '   J ', '   J ', 'J  J ', ' JJ  '],
    'K': ['K   K', 'K  K ', 'KKK  ', 'K  K ', 'K   K'],
    'L': ['L    ', 'L    ', 'L    ', 'L    ', 'LLLLL'],
    'M': ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M'],
    'N': ['N   N', 'NN  N', 'N N N', 'N  NN', 'N   N'],
    'O': [' OOO ', 'O   O', 'O   O', 'O   O', ' OOO '],
    'P': ['PPPP ', 'P   P', 'PPPP ', 'P    ', 'P    '],
    'Q': [' QQQ ', 'Q   Q', 'Q   Q', 'Q  QQ', ' QQQQ'],
    'R': ['RRRR ', 'R   R', 'RRRR ', 'R  R ', 'R   R'],
    'S': [' SSSS', 'S    ', ' SSS ', '    S', 'SSSS '],
    'T': ['TTTTT', '  T  ', '  T  ', '  T  ', '  T  '],
    'U': ['U   U', 'U   U', 'U   U', 'U   U', ' UUU '],
    'V': ['V   V', 'V   V', 'V   V', ' V V ', '  V  '],
    'W': ['W   W', 'W   W', 'W W W', 'WW WW', 'W   W'],
    'X': ['X   X', ' X X ', '  X  ', ' X X ', 'X   X'],
    'Y': ['Y   Y', ' Y Y ', '  Y  ', '  Y  ', '  Y  '],
    'Z': ['ZZZZZ', '   Z ', '  Z  ', ' Z   ', 'ZZZZZ'],
    ' ': ['     ', '     ', '     ', '     ', '     '] 
}

def generate_ascii_art(text):
    text = text.upper()  # Convert input text to uppercase
    art_lines = ['' for _ in range(5)]  # Initialize 5 lines for ASCII art

    for char in text:
        if char in ascii_font:
            # Append each line of the character's ASCII art
            for i in range(5):
                art_lines[i] += ascii_font[char][i] + '  '  # Add space between characters

    return '\n'.join(art_lines)


def greet():
    print(generate_ascii_art("Greetings"))
