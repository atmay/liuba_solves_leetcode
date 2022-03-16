"""

"""


def flood_fill(image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
    if image is None or image[sr][sc] == newColor:
        return image
    fill(image, sr, sc, image[sr][sc], newColor)
    return image


def fill(image, raw, column, initial, color):
    """
    1) check for raw or column out of boundaries
    2) check if current cell matches initial colour
    3) recursive call to 4 cell's neighbours
    """
    if raw < 0 or raw >= len(image) or column < 0 or column >= len(image[0]) or image[raw][column] != initial:
        return
    image[raw][column] = color
    fill(image, raw + 1, column, initial, color)  # down
    fill(image, raw - 1, column, initial, color)  # up
    fill(image, raw, column - 1, initial, color)  # left
    fill(image, raw, column + 1, initial, color)  # right
