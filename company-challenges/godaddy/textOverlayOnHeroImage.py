def textOverlayOnHeroImage(image, height, width):
    def columnSum(x, y1, y2):
        result = 0
        for y in range(y1, y2):
            result += image[y][x]
        return result

    def rowSum(y, x1, x2):
        result = 0
        for x in range(x1, x2):
            result += image[y][x]
        return result

    bestSum = -1
    bestPos = []
    bboxSum = 0
    lastRowLeftmostSum = 0

    for i in range(len(image) - height + 1):
        for j in range(len(image[0]) - width + 1):
            if i == 0 and j == 0:
                for y in range(height):
                    bboxSum += rowSum(y, 0, width)
                lastRowLeftmostSum = bboxSum
            elif j == 0:
                for y in range(height):
                    bboxSum = (lastRowLeftmostSum - rowSum(i - 1, 0, width) + 
                    rowSum(i + height - 1, 0, width))
            else:
                bboxSum = (bboxSum - columnSum(j - 1, i, i + height)
                                   + columnSum(j + width - 1, i, i + height))
            if bboxSum > bestSum:
                bestSum = bboxSum
                bestPos = [i, j]

    return bestPos

