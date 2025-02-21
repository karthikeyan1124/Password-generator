from flask import Flask, jsonify, render_template
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Correctly load from templates folder

def generate_password():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    special_characters = string.punctuation
    digits = string.digits
    all_characters = lowercase + uppercase + special_characters + digits

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(special_characters),
        random.choice(digits)
    ]
    
    password += random.choices(all_characters, k=11)  # Ensure exactly 15 characters
    random.shuffle(password)
    
    return ''.join(password)

@app.route('/generate-password', methods=['GET'])
def generate_password_route():
    password = generate_password()
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)
