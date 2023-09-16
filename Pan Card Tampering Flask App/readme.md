Step to run application:
Step 1:	Create the copy of the project.
Step 2: Open command prompt and change your current path 
to folder where you can find 'app.py' file.
Step 3: Create environment by command given below-
conda create -name <environment name>
Step 4: Activate environment by command as follows-
conda activate <environment name>
Step 5: Use command below to install required dependencies-
python -m pip install -r requirements.txt
Step 6: Run application by command;
python app.py
You will get url copy it and paste in browser.
Step 7: You have sample_data folder where you can get images to test.



Project 1: Pan Card Tampering Detector App - Deploy On Heroku
Project Overview:
In this project, I've developed an application that detects tampering in Pan Cards (a form of identification in India). Using computer vision techniques, the app analyzes Pan Card images to identify any signs of alteration or tampering. This tool is essential for verifying the authenticity of identification documents.

Code:

The code for this project is available in the "pan-card-tampering-detector" folder.
Data:

No external dataset is used. You can test the app with your own Pan Card images.
Documentation:

Detailed documentation on how the tampering detection works and how to use the app is provided in the project folder.


Dependencies:

OpenCV
Python Flask
Heroku (for deployment)
