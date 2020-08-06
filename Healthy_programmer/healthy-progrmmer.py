import time
from pygame import mixer


# Music did not played hence I have printed it as well.
def playMusic(file, stopper):
    print(file)
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def IsOfficeTime(currenttime):
    if currenttime > '09:00:00' and currenttime < '17:00:01': # this is office time stamp form 9:00 am to 5:00pm
        return True
    else:
        return False


NumberofWaterRemaining = 18

WaterAfterEvery = 20*60  # Seconds  - 20 minutes
EyeExerciseAfterEvery = 30*60  # Seconds - 30 minutes
PhysicalExerciseAfterEvery = 45*60  # Seconds  - 45 minutes

waterMp3 = 'water.mp3'
eyesMp3 = 'rush.mp3'
PhysicalMp3 = 'physical-exercise.mp3'

currenttime = time.strftime('%H:%M:%S')
WaterTakenAt = time.time()
EyeExerciseAt = time.time()
PhysicalExerciseAt = time.time()

SleepTime = 60  # Sleep time in seconds It will check after every 60 seconds.

def log_now(msg):
    with open("../mylogs.txt", "a") as f:
         f.write(f"{msg} {time.now()}\n")

while (IsOfficeTime(currenttime)):
    #     Check for water
    if NumberofWaterRemaining > 0:

        if (time.time() - WaterTakenAt) > WaterAfterEvery:  # water after every 20 minutes
            print("Time to drink water")
            while True:
                playMusic(water.mp3)
                if input("Enter Done if you had water: ").lower() == "done":
                    log_now("Drank water at")
                    WaterTakenAt = time.time()
                    NumberofWaterRemaining -= 1
                    break

        if time.time() - EyeExerciseAt > EyeExerciseAfterEvery:
            print("Time to do eye exercise")
            while True:
                playMusic(eyesMp3)
                if input("Enter Done if you done eye exercise : ").lower() == "done":
                    log_now("Eyes exercise done at")
                    EyeExerciseAt = time.time()
                    break

        if time.time() - PhysicalExerciseAt > PhysicalExerciseAfterEvery:
            print("Time to do Physical exercise")
            while True:
                playMusic(PhysicalMp3)
                if input("Enter Done if you done Physical exercise : ").lower() == "done":
                    PhysicalExerciseAt = time.time()
                    log_now("Body exercise done at")
                    break

    time.sleep(SleepTime)
    currenttime = time.strftime('%H:%M:%S')

