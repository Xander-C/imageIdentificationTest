from PIL import Image

IMG = './image/04.jpg'
char_table = list('''☻@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. ''')


def get_char(r, g, b, tsp=256):
    if tsp == 0:
        return ' '
    length = len(char_table)
    gray = int(r*0.299 + g*0.587 + b*0.114)
    return char_table[int(gray / (256.0 + 1) * length)]


if __name__ == '__main__':
    im = Image.open(IMG)
    w, h = im.size
    w, h = int(1.0*w), int(0.6*h)
    im=im.resize((w,h),Image.NEAREST)
    print('image size is : %s x %s' % (w, h))
    txt = ''
    for i in range(h):
        for j in range(w):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)
    with open(IMG+'.txt', 'w') as f:
        f.write(txt)
