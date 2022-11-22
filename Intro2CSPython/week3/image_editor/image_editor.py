from image_editor_helper import *

def divide_channels(image):
    chan = len(image[0][0])
    lst = []
    for i in range(chan):
        ch = []
        for row in image:
            r = []
            for px in row:
                r.append(px[i])
            ch.append(r)
        lst.append(ch)
    return lst


def merge_channels(image):
    lst = []
    for i in range(len(image[0])):
        row = []
        for j in range(len(image[0][0])):
            px = []
            for k in range(len(image)):
                px.append(image[k][i][j])
            row.append(px)
        lst.append(row)
    return lst


def from_rgb_to_gray(colored_image):
    lst = []
    idx = 0
    for i in colored_image:
        lst.append([])
        for j in i:
            lst[idx].append(round((j[0] * .299) + (j[1] * .587) + (j[2] * .114)))
        idx +=1
    return lst


def blur(size):
    x = size**2
    lst = (([size * [1 / x]]) * size)
    return lst


if __name__ == "__main__":
    image_filename = 'assets/rgb_30x10.png'
    # image_filename = 'assets/girl.jpeg'
    image = image_loader(image_filename)