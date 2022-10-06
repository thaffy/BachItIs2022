import cv2
import numpy as np

# Define a function to get the current frame from the webcam
def get_frame(cap, scaling_factor):
    # Capture the current frame
    _, frame = cap.read()

    # Resize the image
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    return frame

if __name__=='__main__':
    # Define the video capture object
    cap = cv2.VideoCapture(0)

    # Define the background subtractor object
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    # Define the history and learning rate:
    # You can change this paramters to see how the results change
    history = 100

    # Define the learning rate
    learning_rate = 1.0 / history

    # Keep reading frames from the webcam
    # until the user hits the 'Esc' key
    try:
        while True:
            # Grab the current frame
            frame = get_frame(cap, 0.5)

            # Compute the mask
            mask = bg_subtractor.apply(frame, learningRate=learning_rate)

            # Convert the grayscale image to RGB
            mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

            # Display the input and output frames
            cv2.imshow('Input', frame)
            cv2.imshow('Output', mask & frame)

            # Check if the user hit the 'Esc' key
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



