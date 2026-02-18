"""OpenCV vision loop for ZARA."""

from __future__ import annotations

import cv2


def see() -> None:
    """Open the default camera and show frames until ESC is pressed."""
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        raise RuntimeError("Unable to open camera device 0.")

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        cv2.imshow("Zara Vision", frame)

        if cv2.waitKey(1) == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
