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
                writer.writerow(['username', 'password', 'status', 'type'])  # Adiciona campo de tipo

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
            writer.writerow([username, hashed.decode('utf-8'), 'pending', 'user'])

    def user_exists(self, username):
        with open(self.csv_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Pula o cabeçalho
            for row in reader:
                if row[0] == username:
                    return True
        return False

    def authenticate_user(self, username, password):
        with open(self.csv_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Pula o cabeçalho
            for row in reader:
                if row[0] == username and row[2] == 'approved':  # Verifica se está aprovado
                    if self.check_password(row[1].encode('utf-8'), password):
                        return True, row[3]
        return False, None

    def get_pending_users(self):
        pending_users = []
        with open(self.csv_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Pula o cabeçalho
            for row in reader:
                if row[2] == 'pending':
                    pending_users.append(row[0])
        return pending_users

    def approve_user(self, username, user_type):
        users = []
        with open(self.csv_file, mode='r') as file:
            reader = csv.reader(file)
            users = list(reader)

        for i in range(len(users)):
            if users[i][0] == username:
                users[i][2] = 'approved'
                users[i][3] = user_type

        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(users)
