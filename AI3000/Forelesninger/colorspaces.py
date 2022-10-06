import cv2
import numpy as np

def get_frame(cap,scaling_factor):
    # Capture the current frame
    _, frame = cap.read()

    # Resize the image
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    return frame

if __name__ =='__main__':
    # Define the video capture object
    cap = cv2.VideoCapture(0)

    # Define the scaling factor for the images
    scaling_factor = 0.5

    # Keep reading the frames from the webcam
    # untill the user hits the 'Esc' key
    try:
        while True:
            # Grab the current frame
            frame = get_frame(cap, scaling_factor)

            # Convert to HSV color space
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Define range of skin color in HSV
            lower = np.array([0,70,60])
            upper = np.array([50,150,255])

            # Threshold the HSV image to get only skin color
            # This is our mask
            mask = cv2.inRange(hsv,lower,upper)

            # Compute the bitwise AND between the mask and original image
            img_bitwise_and = cv2.bitwise_and(frame,frame,mask=mask)

            # Run the median blurring to smoothen the image:
            img_median_blurred = cv2.medianBlur(img_bitwise_and,5)

            # Display the input and output frames:
            cv2.imshow('Input',frame)
            cv2.imshow('Output',img_median_blurred)

            # Check if the user pressed the 'Esc' key
            c = cv2.waitKey(5)
            if c == 27:
                break
    except:
        print("Error")
    finally:
        # Release the video capture object
        cap.release()

        # Close all the windows
        cv2.destroyAllWindows()