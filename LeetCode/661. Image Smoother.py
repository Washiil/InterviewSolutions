def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
    rows = len(img)
    cols = len(img[0])

    output = [[0] * cols for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            pixel_total = 0
            pixel_count = 0

            # Nice and neat solution to handling upper and lower index out of bounds
            # Credit: https://leetcode.com/MrAke/
            for x in range(max(0, i - 1), min(rows, i + 2)):
                for y in range(max(0, j - 1), min(cols, j + 2)):
                    pixel_total += img[x][y]
                    pixel_count += 1

            output[i][j] = pixel_total // pixel_count

    return output
