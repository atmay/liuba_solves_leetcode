"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill
on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels
(also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels
connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
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
