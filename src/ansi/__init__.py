fgcolors = {
    'black': '30',
    'red': '31',
    'green': '32',
    'yellow': '33',
    'blue': '34',
    'magenta': '35',
    'cyan': '36',
    'lightgray': '37',
    'gray': '90',
    'lightred': '91',
    'lightgreen': '92',
    'lightyellow': '93',
    'lightblue': '94',
    'lightmagenta': '95',
    'lightcyan': '96',
    'white': '97'
}

bgcolors = {
    'black': '40',
    'red': '41',
    'green': '42',
    'yellow': '43',
    'blue': '44',
    'magenta': '45',
    'cyan': '46',
    'lightgray': '47',
    'gray': '100',
    'lightred': '101',
    'lightgreen': '102',
    'lightyellow': '103',
    'lightblue': '104',
    'lightmagenta': '105',
    'lightcyan': '106',
    'white': '107'
}

formats = {
    'reset': '0',
    'bold': '1',
    'faint': '2',
    'italics': '3',
    'underline': '4'
}


def fgcolor(color):
    return '\033[{}m'.format(fgcolors[color])


def color(color):
    return fgcolor(color)


def bgcolor(color):
    return '\033[{}m'.format(bgcolors[color])


def format(format):
    return '\033[{}m'.format(formats[format])
