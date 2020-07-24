# Face Alert System
An app that works like an alert mechanism to prevent us from touching our face and hence it can help to prevent the spread of covid-19.
If the user moves his/her hand towards their face then the app generates an alert and the phone starts vibrating  
It works as follows:
1. When the user moves his hand, the device collects accelerometer data and sends it to the API as a JSON file.

2. The API is backed up with a machine learning model.

3. The machine learning model is well trained to differentiate when a hand is near the face and when it is not.

4. Our backend algorithm calculates the Roll, Yaw and Pitch using accelerometer data which can be used to define the orientation of the device.

5. So whenever the user brings his or her hand near the face, the backend model raises an alert and the device starts vibrating.

6. We’ve further integrated Watson ChatBot with our app to help people with their covid related queries. 

WE’VE USED SVM TO TRAIN OUR MODEL AS IT GIVES THE HIGHEST ACCURACY


## app-universal-release.apk
This app is for Phone users.

## app-debug.apk
This app is for smartwatch user.
This app is still not tested. Anyone interested in testing this app can contact me
Anyone can contibute to imporve accuracy of the model.
##
mail : namanmehrora05@gmail.com
