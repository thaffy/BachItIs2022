import cv2;

def frame_diff(prev_frame, cur_frame, next_frame):
    # Difference between the current frame and the next frame
    diff_frames_1 = cv2.absdiff(next_frame, cur_frame)

    # Difference between the current frame and the previous frame
    diff_frames_2 = cv2.absdiff(cur_frame, prev_frame)
    
    # Compute the bitwise AND between the two difference frames and return it.
    return cv2.bitwise_and(diff_frames_1, diff_frames_2)

def get_frame(cap, scaling_factor):
    # Capture the current frame
    _, frame = cap.read()

    # Resize the image
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Apply Gaussian blurring
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    return gray

if __name__=='__main__':
    # Define the video capture object
    cap = cv2.VideoCapture(0)
    
    # Define the scaling factor for the images
    scaling_factor = 0.5

    # Grab the current frame
    prev_frame = get_frame(cap, scaling_factor)

    # Grab the next frame
    cur_frame = get_frame(cap, scaling_factor)

    # Grab the frame after that
    next_frame = get_frame(cap, scaling_factor)

    try:
        while True:
            # Display the frame difference
            cv2.imshow('Object Movement', frame_diff(prev_frame, cur_frame, next_frame))

            # Update the variables
            prev_frame = cur_frame
            cur_frame = next_frame

            # Grab the next frame
            next_frame = get_frame(cap, scaling_factor)

            # Check if the user pressed a key, specifcally ESC (27)
            key = cv2.waitKey(10)
            if key == 27:
                break
    except:
        print("Error")
    finally:
        # Release the video capture object
        cap.release()

        # Close all the windows
        cv2.destroyAllWindows()



