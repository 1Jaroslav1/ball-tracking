import cv2 as cv
import numpy as np

def main():
    board=cv.imread("chessboardpattern.jpg")
    print((board.shape[1]*0.5, board.shape[0]*0.5),)
    board_resized = cv.resize(board,(100,100),cv.INTER_AREA)

    while True:
        cv.imshow("haha",board_resized)

        key=cv.waitKey(1)
        if key==27:     #esc
            break

    cv.destroyAllWindows()



if __name__ == "__main__":
    main()