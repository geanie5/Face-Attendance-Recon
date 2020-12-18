import cv2
import numpy as np
import face_recognition
import os
import glob
from datetime import datetime

#create a list to get the images from our folder automatically
#generate encoding for it and find it in our webcam
image_folder_path = 'data/*.jpg'
images, classNames, ID = [], [], []
#use class names and import the imgs 1 by 1  cl = name of our image
#(os.path.splitext(cl)[0] will give us the file name without .jpg
for cl in glob.glob(image_folder_path):
    curImg = cv2.imread(cl)
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

#to display name and student ID from image name
for i in classNames:
    v = i
    splitedname = v.split('_')
    Name = splitedname[0]
    ID = splitedname[1]

#once we import images, we find the encodings for each of them
def findEncoding(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncoding(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

#to mark attendance with name, date, time and student ID
def markAttendance(name,ID):
    Date = datetime.now().strftime('%d%m%Y')
    with open('Attendance'+Date+'.csv','r+') as f:
        #read all lines in csv to ensure that there is no double entry
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            #append into name list for checking with csv
        if name not in nameList:
            now = datetime.now()
            date = now.strftime('%d/%m/%Y')
            dtString = now.strftime('%H:%M:%S')
            f.writelines('\n{},{},{},{}'.format(name, date, dtString, ID))

while True:
    success, img = cap.read()
    #since we are doing this in real time, we will reduce the image size to speed up the process
    #(img) = send in image , (0,0) = pixels size , 0.25, 0.25 = scale (1/4 of size)
    #convert colour afterwards
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    #send location to encoding function in event multiple faces
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    #loop through together to grab 1 face from location
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        #compare encodings with faces to see if it matches the face distance
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        #lowest face distance will be best match (eg. 0.38)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDis)
        #finding the index of best match image from the array
        matchIndex = np.argmin(faceDis)

        #to display name and student ID for best match image
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            AnyName = name.split('_')
            Person_Name = AnyName[0]
            print(Person_Name)

            STUDENT_ID = AnyName[1]
            print(STUDENT_ID)

            #to draw a rectangle for face location
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,Person_Name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            cv2.putText(img,STUDENT_ID,(x1+6,y2-178),cv2.FONT_ITALIC,0.5,(255,255,255),2)
            markAttendance(Person_Name,STUDENT_ID)

        cv2.imshow('Webcam',img)
        cv2.waitKey(1)
