from PIL import Image
import argparse

chars = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#define parameter for conversion
parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('--width', type = int, default = 80)
parser.add_argument('--height', type = int, default = 80)


#parsing arguments
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output


#convert image to grey scale
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(chars)
    grey = int(0.2126*r + 0.7152*g + 0.0722*b)

    unit = (256.0+1)/length
    
    return chars[int (grey/unit)]


#open and convert image
if __name__ == '__main__':
    img = Image.open(IMG)
    img = img.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*img.getpixel((j,i)))

        txt += '\n'

    print txt

    #write to file
    if OUTPUT:
        with open (OUTPUT,'w') as f:
            f.write(txt)

    else:
        with open("output.txt",'w') as f:
            f.write(txt)



