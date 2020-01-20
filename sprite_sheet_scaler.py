#!/usr/bin/env python

from gimpfu import *

def scale_sprite_sheet(image, layer, oldSpriteWidth, oldSpriteHeight, newSpriteWidth, newSpriteHeight):
    (newImageWidth, newImageHeight) = calculate_new_dimensions(
        image.width,
        image.height,
        oldSpriteWidth,
        oldSpriteHeight,
        newSpriteWidth,
        newSpriteHeight
    )
    pdb.gimp_context_set_interpolation(INTERPOLATION_NONE)
    pdb.gimp_image_scale(image, int(newImageWidth), int(newImageHeight))


def calculate_new_dimensions(imageWidth, imageHeight, oldSpriteWidth, oldSpriteHeight, newSpriteWidth, newSpriteHeight):
    rows = imageHeight / oldSpriteHeight
    columns = imageWidth / oldSpriteWidth
    newImageHeight = rows * newSpriteHeight
    newImageWidth = columns * newSpriteWidth
    return (newImageWidth, newImageHeight)


register(
    'python_fu_sprite_sheet_scaler',
    'Scales sprite sheets',
    'Scales sprite sheets by desired sprite size without blurring.',
    'Canaan Manley',
    'Canaan Manley',
    '2020',
    '<Image>/Image/Scale Sprite Sheet..',
    '*',
    [
        (PF_SPINNER, 'oldSpriteWidth', 'Old Sprite Width:', 32, (1, 512, 1)),
        (PF_SPINNER, 'oldSpriteHeight', 'Old Sprite Height:', 32, (1, 512, 1)),
        (PF_SPINNER, 'newSpriteWidth', 'New Sprite Width:', 64, (1, 512, 1)),
        (PF_SPINNER, 'newSpriteHeight', 'New Sprite Height:', 64, (1, 512, 1))
    ],
    [],
    scale_sprite_sheet
)

main()