Ensure the following files are in the same directory:

aggiestack.py
cloud.py
flavor.py
image.py
instance.py
pmachine.py
rack.py

hdwr-config.txt - Must be a hardware file with the racks listed. I accidentally implemented some of Part C before I realized it was optional.

flavor-config.txt - Any should be fine

image-config.txt - Must be an image file with no sizes listed. Did not implement this portion of Part C. The image file on my GitHub doesn't work properly for this.

The program doesn't need test.py to work. If I forgot to comment out its import when I turn this in, then comment it out if it causes problems.

This AggieStack runs in a loop that takes commands until Ctrl + C is pressed or "exit" is entered. This was made with Python 3.6. I cannot guarantee it will work with lower versions of Python. To run this, typing in "python aggiestack.py" in the Windows command prompt worked for me.