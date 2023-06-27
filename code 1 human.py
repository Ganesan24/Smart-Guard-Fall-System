import cv2
import serial

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Open a video capture device (use 0 for the default camera)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # Use CAP_DSHOW for faster camera access on Windows

# Open the serial port to communicate with the Arduino board
ser = serial.Serial('COM6', 9600) # Replace 'COM3' with the port your Arduino board is connected to

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    
    # Prepare the frame for object detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Run object detection on the frame for human faces
    face_detections = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    
    # Post-process the detections to filter out non-human objects
    human_count = 0
    for (x, y, w, h) in face_detections:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        human_count += 1
    
    # Display the resulting frame with the human count
    cv2.putText(frame, f"Human Count: {human_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Human Detection", frame)
    
    # Send the human count to the Arduino board via the serial port
    ser.write(f"{human_count}\n".encode())
    
    # Exit the program if the "q" key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()
# Close the serial port
ser.close()
