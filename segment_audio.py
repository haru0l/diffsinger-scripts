# this just segments audio cuz yea
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# set input directory and silence threshold (in decibels)
input_dir = os.getcwd()
silence_threshold = "-50"

# loop over all subdirectories in the directory
for subdir, _, _ in os.walk(input_dir):
    # loop over all WAV files in the subdirectory and process them
    for input_file in os.listdir(subdir):
        if input_file.endswith(".wav"):
            # extract the filename without extension and subdirectory name
            subdir_name = os.path.basename(subdir)
            filename = os.path.splitext(input_file)[0]

            # load audio file and detect silence
            audio = AudioSegment.from_file(os.path.join(subdir, input_file), format="wav")
            chunks = split_on_silence(audio, min_silence_len=2000, silence_thresh=silence_threshold)

            # save each chunk as a new file
            for i, chunk in enumerate(chunks):
                output_file = f"{subdir_name}_{filename}_{i+1:03d}.wav"
                chunk.export(os.path.join(subdir, output_file), format="wav")
