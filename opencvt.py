import cv2

def get_coords():
    img = cv2.imread('bed1.jpg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    ret, thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    coordinate_list = []
    for contour in contours:
        M = cv2.moments(contour)
        #print("moments")
        #print(M)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        window_name = 'image'

        table_width = img.shape[1]
        table_height = img.shape[0]
        ball_pos_x = (cx / table_width) * 100
        ball_pos_y = (cy / table_height) * 100
        #cv2.imshow(window_name, blurred)
        coordinate_list.append((2*(ball_pos_x//10)+1,20-(2*(ball_pos_y//10)+1)))
        #print(2*(ball_pos_x//10)+1,2*(ball_pos_y//10)+1)
    return coordinate_list

#print(get_coords())

#print(2*(ball_pos_x//10)+1,2*(ball_pos_y//10)+1)

