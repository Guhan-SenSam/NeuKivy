def rgb_2_dec(color):
    return [channel / 255 for channel in color]


def dec_2_rgb(color):
    return [int(channel * 255) for channel in color]
