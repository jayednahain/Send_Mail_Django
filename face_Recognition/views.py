from django.shortcuts import render, redirect
import cv2
from Attendance_Management_System.settings import BASE_DIR
import os


def recognations_page(request):

   return render(request,'face_recognation.html')


def get_data(request):
   if request.method == "POST":
      name = request.POST.get('name')
      student_id = request.POST.get('student_id')




      return render(request,'face_recognation.html')


def takeImages(request):
   if request.method == "POST":
      name = request.POST.get('name')
      student_id = request.POST.get('student_id')

      # print request.POST
      #userId = request.POST['userId']
      print(cv2.__version__)
      # Detect face
      # Creating a cascade image classifier
      file_path = 'ml\haarcascade_frontalface_default.xml'
      path = os.path.join(BASE_DIR,file_path)
      faceDetect = cv2.CascadeClassifier(path)

      # camture images from the webcam and process and detect the face
      # takes video capture id, for webcam most of the time its 0.
      cam = cv2.VideoCapture(0)

      # Our identifier
      # We will put the id here and we will store the id with a face, so that later we can identify whose face it is

      # Our dataset naming counter
      sampleNum = 0
      # Capturing the faces one by one and detect the faces and showing it on the window
      while (True):
         # Capturing the image
         # cam.read will return the status variable and the captured colored image
         ret, img = cam.read()
         # the returned img is a colored image but for the classifier to work we need a greyscale image
         # to convert
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         # To store the faces
         # This will detect all the images in the current frame, and it will return the coordinates of the faces
         # Takes in image and some other parameter for accurate result
         faces = faceDetect.detectMultiScale(gray, 1.3, 5)
         # In above 'faces' variable there can be multiple faces so we have to get each and every face and draw a rectangle around it.
         for (x, y, w, h) in faces:
            # Whenever the program captures the face, we will write that is a folder
            # Before capturing the face, we need to tell the script whose face it is
            # For that we will need an identifier, here we call it id
            # So now we captured a face, we need to write it in a file
            sampleNum = sampleNum + 1
            # Saving the image dataset, but only the face part, cropping the rest
            file_name = f'ml\TrainingImage\{name} -{student_id}-{sampleNum}.jpg'
            cv2.imwrite(os.path.join(BASE_DIR,file_name, gray[y:y + h, x:x + w]))
            # @params the initial point of the rectangle will be x,y and
            # @params end point will be x+width and y+height
            # @params along with color of the rectangle
            # @params thickness of the rectangle
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Before continuing to the next loop, I want to give it a little pause
            # waitKey of 100 millisecond
            cv2.waitKey(250)

         # Showing the image in another window
         # Creates a window with window name "Face" and with the image img
         cv2.imshow("Face", img)
         # Before closing it we need to give a wait command, otherwise the open cv wont work
         # @params with the millisecond of delay 1
         cv2.waitKey(1)
         # To get out of the loop
         if (sampleNum > 20):
            break
      # releasing the cam
      cam.release()
      # destroying all the windows
      cv2.destroyAllWindows()

      return redirect('/')

   return render(request,'face_recognation.html')




