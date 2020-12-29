# Attendance Taking AI
COVID-19 has resulted in schools shutting out all over the world, including Singapore. As a result, many classes and extra co-curricular activities have no choice but to turn online. Many educators grapple with how to keep track of the student’s attendance, especially in a large group setting. Close to heart, DAC often holds workshops for the members online on zoom. It requires the excos quite some time to do an ID verification to ensure that everyone is from SIM by manually verifying each ID. What if we could automate this attendance process? 

Attendance Face Recon is a program which detects images and tags the images with information based on features it detects. After identification, it will take this data and input it into an excel sheet with a timestamp. It can be then saved as a file for recording purposes. This efficient process of taking attendance can reduce time and manpower as compared to the manual process carried out previously.

# Set Up

**Prerequisites:**

- Git
- Python 3.6
- Pycharm

Libraries | Version
-----------|-----------
opencv-python | 4.4.0.46
cmake | 3.18.4 
dlib ([installation instructions](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)) | 19.21.0
face-recognition | 1.3.0
numpy | 1.19.4
os    |  

**Note:** We could `pip install -r requirements.txt` to install all the required libraries.

# Snapshot

Result:

![](README_Image.png)

# How it works?

Attendance Face Recon works best for a one-time event. Prior to the event, we will need to tag the name and ID with the images of their faces. On the event day, one only needs to run the webcam and the program will automatically input entries in the csv file in the form of attendance. 

For subsequent events, user will have to save a copy of the csv file, so that the original file can be kept. For the next event, user will need to rename the original csv file to the current date (eg. from  "Attendance30112020.csv" to "Attendance01122020.csv"), clear the entries in Pycharm and run the code. Once attendance taking has been completed, we will then need to save a copy of the excel sheet. For the following workshop, we will need to repeat the steps as mentioned.


# Final Thoughts

* #### What are the lessons?


The different components we need to start a face recognition project.

Application of face recognition to suit our needs in our club’s attendance taking.

Adapting to the various sizes of the images as we would collect different images and it would have different coordinates displayed for the bounding box which tags the ID with the face. 


* #### Will this be useful? 

It will be useful but will need improvements to become a foolproof solution.


* #### How to use this model?

Attendance Face Recon is a program which detects images and tags the images with information based on features it detects. After identification, it will take this data and input it into an excel sheet with a timestamp. It can be then saved as a file for recording purposes. This efficient process of taking attendance can reduce time and manpower as compared to the manual process carried out previously.


* #### What are the shortfalls or challenges this model face?

Need for a database/collection for a larger volume.

Need to tag faces with IDs prior to workshop.

Detection of faces based on distance of image from webcam.

# Further work 

- [ ] asdfasdf
- [ ] Saasdfa

# Acknowledgements 

https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78
https://towardsdatascience.com/real-time-face-recognition-an-end-to-end-project-b738bb0f7348

#### Youtube Tutorial
https://www.youtube.com/watch?v=sz25xxF_AVE&feature=youtu.be
