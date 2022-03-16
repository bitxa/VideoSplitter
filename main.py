import os, sys
from moviepy.editor import * 

import math

#Command line arguments
input_file, source_type = sys.argv[1], sys.argv[2]

#Project path
project_dir = os.path.dirname(os.path.abspath(__file__))


def split_single(input_file):
    #Creates clip folder
    clips_folder_name = input_file + 'clips'
    clips_folder_path = os.path.abspath(os.path.join(project_dir, clips_folder_name))
    os.mkdir(clips_folder_path)
    print(clips_folder_path)

    #Read video
    video_path = os.path.join(project_dir, input_file)
    video = VideoFileClip(video_path)
    video_len = video.duration
    print(video_len)
    clips_number =  math.ceil(video_len / 180) if video_len > 180 else 1
    print(clips_number)

    #Intervals counters
    init_counter = 0
    end_counter =  video_len / clips_number 


    for i in range(clips_number):        
        #Create clip
        clip = VideoFileClip(video_path).subclip(init_counter, end_counter)
        clip_path = os.path.join(clips_folder_path, 'clip_' + str(i) + '.mp4')
        
        print(clip_path)
        print("CLIP DURATION" + str(init_counter - end_counter))

        #To avoid bugs we first create an empty file
        file = open(clip_path, 'w')
        
        clip.write_videofile(clip_path)

        init_counter = end_counter
        
        #Update counters
        end_counter += video_len / clips_number 

# In case we want to split multiple files into small multiple clips
# Files should be place inside a folder

def split_multiple(frags_folder):
    #input_file will be used as the folder name
    files = os.listdir(input_file)
    print(len(files))
    for i in files:
        split_single(frags_folder + '/' + i)
#Source types: single, multiple
if source_type == 'single':
    split_single(input_file)
elif source_type == 'multiple':
    split_multiple(input_file)

