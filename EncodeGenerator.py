import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import firebase_admin
from firebase_admin import credentials


cred = credentials.Certificate(r"serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': " ",
})

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)

imgList = []
studentIds = []

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentId = os.path.splitext(path)[0]
    studentIds.append(studentId)

    # Upload metadata to Firebase Realtime Database
    student_data = {
        "id": studentId,
        "image_path": f"{folderPath}/{path}"  # You can customize the image path as needed
    }
    db.reference(f"Students/{studentId}").set(student_data)

    print(f"Student {studentId} data uploaded.")

print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

# Save the encodings to a file
with open("EncodeFile.p", 'wb') as file:
    pickle.dump(encodeListKnownWithIds, file)

print("File Saved")
