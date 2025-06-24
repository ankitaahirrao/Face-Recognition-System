# Face-Recognition System

This is a Face Recognition Attendance System using Python, OpenCV, and face_recognition library.The system uses a camera to capture images of individuals and  Face data is encoded and stored securely using pickle in the databases.
Built with Python, Flask, OpenCV, and Firebase, the system provides an efficient and automated solution to track attendance in various settings such as universities or workplaces.The system allows users to upload their image to the database, which is then used to recognize their face during attendance checks. The recognized faces are matched with the database, and the attendance is updated in real-time. The system also includes a secure login feature for teachers to view the attendance records.

This project is an excellent example of how computer vision and machine learning can be used to automate traditional processes, making them more efficient and accurate.

#Features

The Face Recognition Attendance System comes with a host of features designed to make attendance tracking as seamless and efficient as possible:

1)Face Recognition: The system uses advanced face recognition technology to identify individuals and mark their attendance. This eliminates the need for manual entry and ensures accuracy in attendance tracking.

2)Real-Time Attendance Tracking: The system tracks attendance in real-time. As soon as an individual is recognized by the system, their attendance is marked and updated in the database.

3)Secure Teacher Login: The system includes a secure login feature for teachers. This allows teachers to view the attendance records and ensures that only authorized individuals have access to this data.

4)Multi-Class Support: The system supports multiple classes. Students can be enrolled in multiple classes, and their attendance is tracked separately for each class.

5)Database Integration: The system is integrated with Firebase, a cloud-based NoSQL database. This allows for efficient storage and retrieval of user information and attendance records.

6)Webcam Support: The system supports webcam input for face recognition. This makes it easy to set up and use in a variety of settings.

7)User-Friendly Interface: The system features a user-friendly interface, making it easy for users to navigate and use the system.

8)Open Source: The system is open source. Developers are welcome to contribute and help improve the system.

#Dependencies

The Face Recognition Attendance System relies on several Python libraries to function correctly. Here is a list of the main dependencies:

Flask: A lightweight web application framework. It is used to handle the web server side of the application.

OpenCV: A library of programming functions mainly aimed at real-time computer vision. It is used to capture images from the webcam and perform face detection.

Firebase Admin: A library for interacting with Firebase services. It is used to interact with the Firebase Realtime Database and Firebase Storage.

Werkzeug: A comprehensive WSGI web application library. It is used to handle file uploads in Flask.

Pillow: A Python Imaging Library adds image processing capabilities to your Python interpreter.

numpy: A library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

To install these dependencies, you can use pip, a package manager for Python. Simply run the following command in your terminal:

pip install -r requirements.txt
This will install all the required packages. Make sure you are in the correct directory when you run this command (the directory should contain the requirements.txt file).
