#!/usr/bin/env python
import subprocess
import moviepy.editor as mp

print("Benny Hill video maker")

INPUT_VIDEO_NAME = 'input.mp4'
OUTPUT_VIDEO_NAME = 'output.mp4'
FINAL_VIDEO = 'final.mp4'
BACKGROUND_MUSIC = 'BennyHill.mp3'

SPEED_FACTOR = 0.2

# Speed up the video using the Speed factor
subprocess.call(["ffmpeg",  "-i", INPUT_VIDEO_NAME, 
                 "-vf", f"setpts={SPEED_FACTOR}*PTS", OUTPUT_VIDEO_NAME])

# Add background music
video = mp.VideoFileClip(OUTPUT_VIDEO_NAME)
video.write_videofile(FINAL_VIDEO, audio=BACKGROUND_MUSIC)
