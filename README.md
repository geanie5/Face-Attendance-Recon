# Introduction
COVID-19 has resulted in schools shutting out all over the world, including Singapore. As a result, many classes and extra co-curricular activities have no choice but to turn online. Many educators grapple with how to keep track of the student’s attendance, especially in a large group setting. Close to heart, DAC often holds workshops for the members online on zoom. It requires the excos quite some time to do an ID verification to ensure that everyone is from SIM by manually verifying each ID. What if we could automate this attendance process? 

Attendance Face Recon is a program which detects images and tags the images with information based on features it detects. After identification, it will take this data and input it into an excel sheet with a timestamp. It can be then saved as a file for recording purposes. This efficient process of taking attendance can reduce time and manpower as compared to the manual process carried out previously.


# Set up
(1) Download Python
https://www.python.org/downloads/

(2) Download PyCharm (Community Version)
https://www.jetbrains.com/pycharm/download/#section=windows
* Install cmake, numpy, face-recognition, dlib, OpenCV-python


# Further work 
Attendance Face Recon works best for a one-time event. For subsequent events, user will have to save a copy of the csv file, so that the original file can be kept. For the next event, user will need to rename the original csv file to the current date (eg. from  "Attendance30112020.csv" to "Attendance01122020.csv"), clear the entries in Pycharm and run the code. Once attendance taking has been completed, we will then need to save a copy of the excel sheet. For the following workshop, we will need to repeat the steps as mentioned.
To simplify this process, we could automate the creation of a new csv file. 

Depending on the size of the image, the scaling of rectangle will affect the positioning of the label which is something we could improve on.

# Resources 
* https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78
* https://www.youtube.com/watch?v=sz25xxF_AVE&feature=youtu.be
