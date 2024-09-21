This project presents a File Integrity System designed to detect alterations in files using cryptographic hashing techniques, specifically the Secure Hash Algorithm 256-bit (SHA-256). The system, developed with the Flask web framework in Python, provides a user-friendly interface for uploading, storing, and verifying the integrity of files.
The core principle of the File Integrity System is the use of cryptographic hash functions, which generate a unique hash value—a digital fingerprint—for each file. Any change to the file, no matter how minor, results in a different hash value, thereby signaling potential tampering. SHA-256 is chosen for its strong security properties and widespread recognition as a reliable method for generating cryptographic hashes.
 Test Cases
Description of Test Cases for Different Functionalities:
To ensure that the File Integrity System operates as expected, a series of test cases were designed 
and executed. These test cases cover various functionalities of the system, including file upload, file 
download, hash generation, and integrity verification. Below are the details of these test cases


****************************************
Test Case 1: Uploading a Valid File
 Objective: To verify that the system correctly handles the upload of a valid file.
 Steps:
1. Navigate to the file upload page
    ![1 1](https://github.com/user-attachments/assets/b893c1cc-cd41-43b6-a962-5aa14789aa2b)
2.	Select a valid file (e.g., a .txt, .pdf, or .jpg file).
3. Click the "Upload" button.
  ![1 3](https://github.com/user-attachments/assets/86df6db9-3adb-4b3a-b0a5-d5f5347e9397)
 
*************************************
   
Test Case 2: Downloading a File
 Objective: To verify that users can download files they have uploaded.
 Steps:
1. Upload a valid file
2. Navigate to the "Available Files" section.
   ![2 2](https://github.com/user-attachments/assets/d1d5c6db-1fe6-4385-ae91-4dc53ec746ed)

4. Click the "Download" link for the uploaded file
**************************************

Test Case 3: Verifying File Integrity (Unaltered File)
 Objective: To ensure that the system correctly verifies the integrity of a file that has not been 
altered.
 Steps:
1. Upload a valid file.
2. Click the "Verify Integrity" link for the uploaded file.
   ![3](https://github.com/user-attachments/assets/a766f7b8-3b14-4d7b-8ee5-41fea2eb7f88)

***********************************************

Test Case 4: Verifying File Integrity (Altered File)
 Objective: To test the system’s ability to detect alterations in a file.
 Steps:
1. Upload a valid file.
2. Manually alter the content of the file in the upload/ directory
   ![4 3](https://github.com/user-attachments/assets/2c37b279-63e1-4a69-bb5f-b785abb2c59b)
![hash value](https://github.com/user-attachments/assets/d95d6900-ecaa-4f1e-a489-a47044d629dd)

4. Click the "Verify Integrity" link for the altered file
![4 f](https://github.com/user-attachments/assets/b7281a47-2d1a-4a4d-a3c3-21bfaf5068f0)

