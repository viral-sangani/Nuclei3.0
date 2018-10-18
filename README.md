# Nuclei3.0

***********************************************************

sudo apt-get install python3-pip
pip3 install pyttsx3
pip3 install selenium
pip3 install SpeechRecognition
pip3 install pygame
sudo apt-get install espeak
wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz

** extract the above zip by right click.
** go to that folder in terminal

cd geckodriver-v0.18.0-linux64/
sudo mv geckodriver /usr/local/bin/

wget http://portaudio.com/archives/pa_stable_v190600_20161030.tgz

** extract the above zip by right click.
** go to that folder in terminal

./configure && make
sudo make install

cd ../
pip3 install pyaudio

// sudo apt-get install espeak
