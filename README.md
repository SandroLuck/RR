# RR Helpers
This repository contains scripts I created for the game http://rivalregions.com/

# Donation Pie Chart for State
An executable can be found in https://github.com/SandroLuck/RR/releases/tag/v1
MakeFullDonation.exe
This will create a pie chart of the donations to a state over all regions.
This might take a while.
Please understand that this program has very restricted capabilities.
Run under Windows, double click the .exe and allow it.
### Help
You are asked for 7 fields.
![alt text](https://github.com/SandroLuck/RR/blob/master/DonationsFullState/exampleImages/fullview.JPG)
This will produce.
![alt text](https://github.com/SandroLuck/RR/blob/master/DonationsFullState/exampleImages/resultUSA.JPG)

Request Header:
After login into http://rivalregions.com/
In Chrome for example Press F12.
It should look like this.
![alt text](https://github.com/SandroLuck/RR/blob/master/DonationsFullState/exampleImages/F12.JPG)
Press,  the field highlighted in red in the image.
![alt text](https://github.com/SandroLuck/RR/blob/master/DonationsFullState/exampleImages/F12.JPG)
Copy paste the following text into the field Request Header:
![alt text](https://github.com/SandroLuck/RR/blob/master/DonationsFullState/exampleImages/CopyPaste.JPG)
The State id can be found in the link of every country, as shown here it is '2949'
![alt text](https://github.com/SandroLuck/RR/blob/master/DonationsFullState/exampleImages/CountryId.JPG)
The Field End Date should have the format Year.Month.Day e.g. 2018.05.30
This date has to be in the PAST.
The application calculates all donations from that date UNTIL TODAY.
The output path should be a normal windows path for example ' C:\Users\u\Desktop\imageName.png'. I have to end with '.png', so you can open it later.

# Features
More features and scripts exist and can be found throughout this repository.

# Important
The code in this repository is very bad.
It was written and little consideration for usability or maintainability.

# License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.