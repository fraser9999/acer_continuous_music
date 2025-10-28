# Init

import click
import os

os.system("cls")

# Set Window Titel
os.system("title Main ACE-R Render Window")

print("ACE-R Continous Music Generator")
print("with random Data Support")
print("")
print("Author: Hermann Knopp 2025")
print("Contact: hermann.knopp@gmx.at")
print("")
print("")
print("Be patient, first run will take some time, loading...")
print("")
print("")  

print("Importing Libs...please wait")
print("")

#--Libs----

import time
import random
from random import randrange
#from deep_translator import GoogleTranslator
import codecs
from datetime import datetime

#Task Libs
import subprocess
import os
import signal

#Finde Fenster
import pygetwindow as gw



import g4f
import asyncio
import sys

if sys.platform:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

g4f.debug.logging = False  # Enable debug logging
g4f.debug.version_check = False  # Disable automatic version checking

dir_path = os.path.dirname(os.path.realpath(__file__))

from acestep.pipeline_ace_step import ACEStepPipeline
from acestep.data_sampler import DataSampler







# ----- Setup Routine-------

print("")
print("Please Connect to the Internet for CHATGPT use.")
print("This Software uses free ChatGPT Client with g4f Library")
print("Do not use other Version than g4f==0.6.2.8 for working correct")
print("")

# Debug 0
a=input("Wait Return Key")

img_out_folder=""

# Check for None String   
if img_out_folder=="" or img_out_folder==None:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = "songs"
    filepath= dir_path + "\\" + path
    img_out_folder=filepath
    print("Checking.. " + img_out_folder + " for saving Songs.")    

# Check whether the specified path exists or not
isExist = os.path.exists(img_out_folder)
if not isExist:
   
    # Create a new directory because it does not exist
    os.makedirs(img_out_folder)
    print("The new directory " + img_out_folder + " is created!")   
    print("")
    print("I am using: "+img_out_folder+" for Songs saving")





#-----Wordlist Loader----------------------


# Load Wordlists_
# Hook Words



# hooks.txt

# Load Main Words File (Hooks)
wordspath4=os.path.dirname(os.path.realpath(__file__))
wordspath4=wordspath4 + "\\wordlist\\hooks.txt"

print("Loading Wordlist Files..")
print("")
print("Wordsfile4: "+ wordspath4)

filename4=wordspath4
with open(filename4, encoding="utf8") as f4:
    words4 = f4.readlines()
    words4 = [x4.strip() for x4 in words4]
    anz4 = len(words4) 
    random.shuffle(words4)

#------------------------------

def random_word(word,anz):

    rnd=randrange(1,anz)
    wort=word[rnd]
    return wort

#-----------------------------------



#----------------------------------------------

# Main Load Wordlists_
# Genre,Instruments,Feature



# Genre.txt
#
# Load Main Words File (Genre)
wordspath=os.path.dirname(os.path.realpath(__file__))
wordspath=wordspath + "\\wordlist\\genre.txt"

print("Loading Wordlist Files..")
print("")
print("Wordsfile: "+ wordspath)

filename=wordspath
with open(filename, encoding="utf8") as f:
    words = f.readlines()
    words = [x.strip() for x in words]
    anz = len(words) 
    random.shuffle(words)

#------------------------------

# Instruments.txt

# Load Main Words File (Instruments)
wordspath2=os.path.dirname(os.path.realpath(__file__))
wordspath2=wordspath2 + "\\wordlist\\instruments.txt"

print("Loading Wordlist Files..")
print("")
print("Wordsfile2: "+ wordspath2)

filename2=wordspath2
with open(filename2, encoding="utf8") as f2:
    words2 = f2.readlines()
    words2 = [x2.strip() for x2 in words2]
    anz2 = len(words2) 
    random.shuffle(words2)


#------------------------------

# Features.txt

# Load Main Words File (Features)
wordspath3=os.path.dirname(os.path.realpath(__file__))
wordspath3=wordspath3 + "\\wordlist\\features.txt"

print("Loading Wordlist Files..")
print("")
print("Wordsfile3: "+ wordspath3)

filename3=wordspath3
with open(filename3, encoding="utf8") as f3:
    words3 = f3.readlines()
    words3 = [x3.strip() for x3 in words3]
    anz3 = len(words3) 
    random.shuffle(words3)

#-------------------------------------------------


def random_word(word,anz):

    rnd=randrange(1,anz)
    wort=word[rnd]
    return wort


def random_voice():

    rnd=randrange(0,2)
    if rnd==1:
        ret=1
    else:
        ret=0
    return ret


def random_drum():
    
    rnd=randrange(0,2)
    if rnd==1:
        ret=1
    else:
        ret=0
    return ret


def bring_window_to_front(title):
    for w in gw.getWindowsWithTitle(title):
        if w.isMinimized:
            w.restore()
        w.activate()
        break


def safe_activate(title, retries=3):
    for i in range(retries):
        try:
            win = gw.getWindowsWithTitle(title)
            if win:
                w = win[0]
                if w.isMinimized:
                    w.restore()
                w.activate()
                return True
        except Exception as e:
            print(f"Versuch {i+1}: {e}")
            time.sleep(0.2)
    return False




#------Main Render Routine---------------------------------

def main(checkpoint_path, bf16, torch_compile, cpu_offload, overlapped_decode, device_id, output_path):
    os.environ["CUDA_VISIBLE_DEVICES"] = str(device_id)

    model_demo = ACEStepPipeline(
        checkpoint_dir=checkpoint_path,
        dtype="bfloat16" if bf16 else "float32",
        torch_compile=torch_compile,
        cpu_offload=cpu_offload,
        overlapped_decode=overlapped_decode
    )
    print(model_demo)

    data_sampler = DataSampler()

    

    while True:

        os.system("cls")
        print("")
        print("")

        #prompt1=input("Prompt> ")
        #print("")
        #lyrics1=input("Lyrics 60sec> ")    


        # Start Parameter Settings

        audio_duration=220 # max 1000



        #prompt="slow, country, drums, female voice, guitar"
        
        #------------------------------------------------

        
        a=random_voice()
        if a==1:
            voice_prompt="Female Voice"
   
        else:
            voice_prompt="Male Voice"


        b=random_drum()
        if b==1:
            drums_prompt="drums"

        else:
            drums_prompt=""


        #-----------------------------------

        # Get Words

        genre=random_word(words,anz)
        genre_prompt=genre

        instruments=random_word(words2,anz2)
        instr_prompt=instruments

        feature=random_word(words3,anz3)
        feat_prompt=feature


        # Set Prompt Full

        prompt1=" "+genre_prompt+","+voice_prompt+","+drums_prompt+","+instr_prompt+","+feat_prompt




        # Set Fenster Focus to Render Window 
        #bring_window_to_front("Main ACE-R Render Window")
        

        safe_activate("Main ACE-R Render Window")
        #print("→ Fenster in den Vordergrund gebracht.")
        #time.sleep(5)





        # Display Prompt ------------------------------------------- 

        print(prompt1)

        #Save ACE-R Genre Prompt------------------------------------ 

        # datetime object containing current date and time
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        filename=img_out_folder + "\\song_prompt_" + dt_string +".txt"

        # Save Prompt
                
        with open(filename, "a") as sf1:
            sf1.write("ACE-R Continous Music Gen.")
            sf1.write("\n\n")
            sf1.write("Prompt:")
            sf1.write("\n\n\n")
            sf1.write(str(prompt1))
            sf1.close()




        #Debug 1 
        #a=input("Wait key")  

        #-Start lyrics------------------------------------------------ 


        # Get Words

        hook=random_word(words4,anz4)
        hook_prompt=hook

        chatgpt_prompt="Make me a random songtext in english, wich is 3min30sec long and goes about " + hook_prompt + " , please set the words verse, verse1, verse2 , bridge and chorus into brakets[], please set a little [intro] and a little [outro]"


        os.system("cls")
        print("")
        print("")
        print(chatgpt_prompt)
        print("")
        print("")

        # Send Prompt to ChatGPT


        print("Sending Payload to ChatGPT")
        print("")
        print("")


        try: 


            response = g4f.ChatCompletion.create(
                provider="PollinationsAI",
                model="o4-mini",
                messages=[{"role": "user", "content": chatgpt_prompt}],
                stream=True,
            )

            #------------------------------------------

            # Print response message


            response_text=""
            for message in response:
    
                response_text = response_text + str(message)


        except Exception as e:
            print("")
            print("")
            print("No Connection to G4F Provider -PollinationsAI- ")
            print("I will render with Standard Programmed Lyrics")
            print("Error Thrown" + str(e))
            print("")

               
            response_text=""""[Verse] I see the sunrise in your eyes, The world feels small when you are mine [Chorus] Hold me close, don’t let me go, Love is all we need to know"""

            pass






        # Dummy Debug    
        print(response_text)

        print("")
        print("")
        print("Completed: Text generated from ChatGPT...")

        print("")
    
        # Dummy Debug 2
        #a=input("wait key")


        lyrics1=response_text


        #Save ACE-R Lyrics Text------------------------------------ 

        # datetime object containing current date and time
        now = datetime.now()
 
        #dt_string = now.strftime("%d%m%Y_%H%M%S")
        # use old dt_string         

        filename=img_out_folder + "\\song_lyrics_" + dt_string +".txt"

        # Save Prompt
                
        with open(filename, "a") as sf2:
            sf2.write("ACE-R Continous Music Gen.")
            sf2.write("\n\n")
            sf2.write("Lyrics:")
            sf2.write("\n\n\n")
            sf2.write(str(lyrics1))
            sf2.close()  








        #-End Lyricsa------------------------------------------------


        prompt=prompt1    
        lyrics=lyrics1
        infer_step=50
   
        # guidance scale Std.=7.5
        guidance_scale=4
        scheduler_type="euler"
        cfg_type="apg"
        omega_scale=1

        # Set Random Seed
        max=4294967295
        # generate random Seed Value
        seed=random.randint(1,max)
        manual_seeds=seed

        guidance_interval=1
        guidance_interval_decay=0
        min_guidance_scale=1
        use_erg_tag=False
        use_erg_lyric=False
        use_erg_diffusion=True
        oss_steps=10
        guidance_scale_text=1
        guidance_scale_lyric=1 # min=1 max=10
    
        output_path=img_out_folder


        model_demo(
            audio_duration=audio_duration,
            prompt=prompt,
            lyrics=lyrics,
            infer_step=infer_step,
            guidance_scale=guidance_scale,
            scheduler_type=scheduler_type,
            cfg_type=cfg_type,
            omega_scale=omega_scale,
            manual_seeds=manual_seeds,
            guidance_interval=guidance_interval,
            guidance_interval_decay=guidance_interval_decay,
            min_guidance_scale=min_guidance_scale,
            use_erg_tag=use_erg_tag,  
            use_erg_lyric=use_erg_lyric,
            use_erg_diffusion=use_erg_diffusion,
            oss_steps=oss_steps,
            guidance_scale_text=guidance_scale_text,
            guidance_scale_lyric=guidance_scale_lyric,
            save_path=output_path,
        )



def start_wav_player():
    python_exe = sys.executable
    cmd = f'start cmd /k "{python_exe} {PLAYER_PATH}"'
    subprocess.Popen(cmd, shell=True)
    print("[Main] WAV-Player in neuem Fenster gestartet.")







if __name__ == "__main__":

    checkpoint_path=""
    bf16=True
    torch_compile=False
    cpu_offload=True
    overlapped_decode=False
    device_id=0
    output_path=None
    
    # Pfad zum Player
    dir_path = os.path.dirname(os.path.realpath(__file__))
    PLAYER_PATH = dir_path + "\\wav_player.py"


    print("[Main] Starte WAV-Player...")
    start_wav_player()
    print("[Main] Hauptprogramm läuft unabhängig weiter.")  

    

    # Hauptprogramm macht andere Dinge
    try:

        main(checkpoint_path,bf16,torch_compile,cpu_offload,overlapped_decode,device_id,output_path)
        

    except KeyboardInterrupt:
        print("[Main] Abbruch erkannt – beende Player.")
        process.terminate()





    
