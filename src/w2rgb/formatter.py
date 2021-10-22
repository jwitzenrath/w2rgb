'''
convert RGB values to different formats
'''

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def rgb_to_rgb_255(r,g,b):
    return f'({r:d}, {g:d}, {b:d})'

def rgb_to_rgb_1(r,g,b):
    return f'({r/255.:.6f}, {g/255.:.6f}, {b/255.:.6f})'
