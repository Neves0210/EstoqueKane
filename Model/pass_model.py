import bcrypt
import csv
import os

class UserModel:
    def __init__(self, csv_file='users.csv'):
        self.csv_file = csv_file
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['username', 'password'])  # Adiciona cabeçalho

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed

    def check_password(self, hashed_password, user_password):
        return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

    def register_user(self, username, password):
        hashed = self.hash_password(password)
        with open(self.csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, hashed.decode('utf-8')])

    def authenticate_user(self, username, password):
        with open(self.csv_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Pula o cabeçalho
            for row in reader:
                if row[0] == username:
                    if self.check_password(row[1].encode('utf-8'), password):
                        return True
                    else:
                        return False
        return False
