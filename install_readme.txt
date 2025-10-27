Welcome to:

"ACE-R Continous Music Generator
with Random ChatGPT Lyrics Support"


this is an Addon for the Famous
ACE-Step Music Software Package.


it can generate Music in a
continuous Render and Playing
Loop.


Author: Hermann Knopp
Contact: hermann.knopp@gmx.at
Version: Early Alpha 0.1a



Install:

first:
please install python 3.10.10 x64
in a virtual python environment

then:
install the full ACE-Step Package
so Inference is working correct.


ACE-Step main Repository
Link: https://github.com/ace-step/ACE-Step

copy the repository of ACE-R
into the ACE-Step Directory

Start python App:
"ACE-R Continuous Music Generator.py"
with Virtual python.exe


Usage:

Main "ACE-R Continuous" Render App

will start WAV_Player in a new Task
waiting for first WAV Render.



Lyrics is fetched automatic from
ChatGPT-4-mini (g4f)

prompt for ACE-R is generated randomly 
form Wordlists in Directory(wordlist)



The Software is tested on a
NVIDIA Geforce RTX 3060 with 12Gb Vram
this Card is fast enough to render
and buffer 1-2 Songs before Playback.

so Playback will not stop and play
all found Files continuously.

if you have no fast GFX-Card
Playback will wait for Render til finished.

First Run will take some Time, loading
Model and Setup the Render Pipeline and 
fetch Lyrics fro ChatGPT (g4f library).

Render Time is about 1:30 Minutes (RTX3060) so
Playback for a 3:30 Minute Song
has some Time left.

contact me on github for Issues and Errors

Thanks.







  








 






































 