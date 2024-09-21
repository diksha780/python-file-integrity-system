import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Set up the directories
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')
HASHES_FOLDER = os.path.join(os.getcwd(), 'hashes')

# Ensure the directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(HASHES_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['HASHES_FOLDER'] = HASHES_FOLDER

# Helper function to calculate file hash
def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

@app.route('/')
def index():
    # List all files in the upload directory
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Create hash for the uploaded file
        file_hash = calculate_hash(file_path)
        hash_file_path = os.path.join(app.config['HASHES_FOLDER'], filename + '.hash')
        with open(hash_file_path, 'w') as hash_file:
            hash_file.write(file_hash)
       

        flash('File successfully uploaded and hashed generated.','success')
        print("Flash message set: File successfully uploaded and hash generated.")
        return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/verify/<filename>')
def verify_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    hash_file_path = os.path.join(app.config['HASHES_FOLDER'], filename + '.hash')
    
    if os.path.exists(file_path) and os.path.exists(hash_file_path):
        current_hash = calculate_hash(file_path)
        with open(hash_file_path, 'r') as hash_file:
            original_hash = hash_file.read().strip()
        
        if current_hash == original_hash:
            flash(f'The file "{filename}" is verified and has not been altered.', 'success')
            print("Flash message set: File is verified and has not been altered.")
        else:
            flash(f'The file "{filename}" has been altered!','error')
            print("Flash message set: File has been altered!.")
    else:
        flash(f'File or hash not found for "{filename}".','error')
        print("Flash message set: File or hash not found!.")
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
