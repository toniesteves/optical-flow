import cv2
import numpy as np


point_selected = False
point = ()
old_points = np.array([[]])

cap = cv2.VideoCapture(0)

# Initial frame
_, frame = cap.read()
prev_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Lucas Kanade algorithm params
lk_params = dict(winSize = (15, 15),
                 maxLevel = 5,
                 criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))


# Mouse function
def set_initial_point(event, x, y, flags, params):
    
  global point, point_selected, old_points

  if event == cv2.EVENT_LBUTTONDOWN:
    point = (x, y)
    point_selected = True
    old_points = np.array([[x, y]], dtype=np.float32)


cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", set_initial_point)


while cap.isOpened():
  _, frame = cap.read()
  curr_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  if point_selected is True:
    cv2.circle(frame, point, 5, (0, 0, 255), 2)

    new_points, status, error = cv2.calcOpticalFlowPyrLK(prev_frame, curr_frame, old_points, None, **lk_params)
    prev_frame = curr_frame.copy()
    old_points = new_points

    x, y = new_points.ravel()
    cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)


  cv2.imshow("Frame", frame)

  key = cv2.waitKey(1)
  if key == 27:
    break

cap.release()
cv2.destroyAllWindows()