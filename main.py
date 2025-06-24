import datetime
import os
import pickle
import tkinter as tk

import cv2
import face_recognition
from PIL import Image, ImageTk

import util

# from test import test  # Uncomment when `test.py` is available and working


class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")
        self.main_window.title("Face Attendance System")

        self.login_button_main_window = util.get_button(self.main_window, 'login', 'green', self.login)
        self.login_button_main_window.place(x=750, y=200)

        self.logout_button_main_window = util.get_button(self.main_window, 'logout', 'red', self.logout)
        self.logout_button_main_window.place(x=750, y=300)

        self.register_new_user_button_main_window = util.get_button(
            self.main_window, 'register new user', 'gray', self.register_new_user, fg='black')
        self.register_new_user_button_main_window.place(x=750, y=400)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

        self.add_webcam(self.webcam_label)

        self.db_dir = './db'
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

        self.log_path = './log.txt'

    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)  # changed from 2 to 0 for default webcam

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to grab frame from webcam.")
            self._label.after(100, self.process_webcam)
            return

        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)

    def login(self):
        # label = test(...)  # Uncomment when test.py is present
        label = 1  # Temporary bypass for spoof detection

        if label == 1:
            name = util.recognize(self.most_recent_capture_arr, self.db_dir)
            if name in ['unknown_person', 'no_persons_found']:
                util.msg_box('Oops...', 'Unknown user. Please register.')
            else:
                util.msg_box('Welcome!', f'Welcome back, {name}!')
                with open(self.log_path, 'a') as f:
                    f.write(f'{name},{datetime.datetime.now()},in\n')
        else:
            util.msg_box('Spoof Alert!', 'You are not a real user!')

    def logout(self):
        # label = test(...)  # Uncomment when test.py is present
        label = 1  # Temporary bypass for spoof detection

        if label == 1:
            name = util.recognize(self.most_recent_capture_arr, self.db_dir)
            if name in ['unknown_person', 'no_persons_found']:
                util.msg_box('Oops...', 'Unknown user. Please register.')
            else:
                util.msg_box('Goodbye!', f'See you again, {name}!')
                with open(self.log_path, 'a') as f:
                    f.write(f'{name},{datetime.datetime.now()},out\n')
        else:
            util.msg_box('Spoof Alert!', 'You are not a real user!')

    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1200x520+370+120")
        self.register_new_user_window.title("Register New User")

        self.accept_button = util.get_button(
            self.register_new_user_window, 'Accept', 'green', self.accept_register_new_user)
        self.accept_button.place(x=750, y=300)

        self.try_again_button = util.get_button(
            self.register_new_user_window, 'Try again', 'red', self.try_again_register_new_user)
        self.try_again_button.place(x=750, y=400)

        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)

        self.add_img_to_label(self.capture_label)

        self.entry_text = util.get_entry_text(self.register_new_user_window)
        self.entry_text.place(x=750, y=150)

        self.text_label = util.get_text_label(self.register_new_user_window, 'Please input username:')
        self.text_label.place(x=750, y=70)

    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def add_img_to_label(self, label):
        if hasattr(self, 'most_recent_capture_pil'):
            imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
            label.imgtk = imgtk
            label.configure(image=imgtk)
            self.register_new_user_capture = self.most_recent_capture_arr.copy()
        else:
            util.msg_box('Camera Error', 'No frame captured yet. Please wait a moment and try again.')

    def accept_register_new_user(self):
        name = self.entry_text.get(1.0, "end-1c")
        if not name.strip():
            util.msg_box('Input Error', 'Username cannot be empty.')
            return

        try:
            embeddings = face_recognition.face_encodings(self.register_new_user_capture)[0]
        except IndexError:
            util.msg_box('Error', 'Face not detected. Please try again.')
            return

        file_path = os.path.join(self.db_dir, f'{name}.pickle')
        with open(file_path, 'wb') as file:
            pickle.dump(embeddings, file)

        util.msg_box('Success!', f'User {name} registered successfully.')
        self.register_new_user_window.destroy()

    def start(self):
        self.main_window.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()

