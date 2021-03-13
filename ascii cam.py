import cv2
import numpy as np
import tkinter as tk

def main():

    vc = cv2.VideoCapture(0)

    if vc.isOpened():
        rval, frame = vc.read()
        ascii_pro, frame = vc.read()
    else:
        rval = False
        ascii_print = False

    racine = tk.Tk()

    while ascii_print:
        label = tk.Label(racine, text=toASCII(frame, 120, 30))
        label.pack()
        racine.mainloop()

        key = cv2.waitKey(500)

    while rval:

        rval, frame = vc.read()
        print(toASCII(frame))

        key = cv2.waitKey(500)
        if key == 27:
            break

def toASCII(frame, cols=150, rows=120):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, width = frame.shape
    cell_width = width / cols
    cell_height = height / rows
    if cols > width or rows > height:
        raise ValueError('plus de couleurs')
    result = ""
    for i in range(rows):
        for j in range(cols):
            gray = np.mean(
                frame[int(i * cell_height):min(int((i + 1) * cell_height), height),
                int(j * cell_width):min(int((j + 1) * cell_width), width)]
            )
            result += grayToChar(gray)
        result += '\n'
    return result


def grayToChar(gray):
    CHAR_LIST = '.,;-":/!§%\'@#*µ£$=&éo'
    num_chars = len(CHAR_LIST)
    return CHAR_LIST[
        min(
            int(gray * num_chars / 255),
            num_chars - 1
        )
    ]


if __name__ == '__main__':
    main()