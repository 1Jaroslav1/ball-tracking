import cv2 as cv
import numpy as np
import random


def main():
    cam = cv.VideoCapture(0)

    while True:
        check, frame = cam.read()

        cv.imshow("video", frame)

        key = cv.waitKey(1)
        if key==27:     #esc
            break
        if key==32:     #space
            warped = createHomographyMatrix(frame)
            cv.imshow("frame", frame)
            cv.imshow("warped", warped)    

    cam.release()
    cv.destroyAllWindows()


def createHomographyMatrix(frame):
    board=cv.imread("chessboardpattern.jpg")
    board_resized = cv.resize(board,(frame.shape[1],frame.shape[0]),cv.INTER_AREA)

    ret1, corners1 = cv.findChessboardCorners(frame, (6,8))
    ret2, corners2 = cv.findChessboardCorners(board_resized, (6,8))

    H, _ = cv.findHomography(corners1, corners2)
    warp = cv.warpPerspective(frame, H, (board_resized.shape[1], board_resized.shape[0]))
    
    
    ##Drawing matches
    img_draw_matches = cv.hconcat([frame, board_resized])
    for i in range(len(corners1)):
        pt1 = np.array([corners1[i][0][0], corners1[i][0][1], 1])
        pt1 = pt1.reshape(3, 1)
        pt2 = np.dot(H, pt1)
        pt2 = pt2/pt2[2]
        end = (int(frame.shape[1] + pt2[0]), int(pt2[1]))
        cv.line(img_draw_matches, tuple([int(j) for j in corners1[i][0]]), end, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 1)
    cv.imshow("Draw matches", img_draw_matches)

    return warp


if __name__ == "__main__":
    main()