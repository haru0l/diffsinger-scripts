import os
import shutil

# Define the top-level directory
directory = os.getcwd()

# Loop over all subdirectories
for subdir, dirs, files in os.walk(directory):
    # Create a new directory for the .wav files
    new_dir = os.path.join(subdir, 'wavs')
    os.makedirs(new_dir, exist_ok=True)

    # Loop over all files in the subdirectory
    for filename in files:
        if filename.endswith('.lab'):
            # Open the input file and read the lines
            filepath = os.path.join(subdir, filename)
            with open(filepath, 'r') as infile:
                lines = infile.readlines()

            # Extract the transcription from the filename
            transcription = filename[:-4]

            # Loop over the lines and extract the phonemes and timings
            timings = []
            phonemes = []
            for line in lines:
                parts = line.strip().split()
                timings.append(str(round((float(parts[1]) - float(parts[0]))/10000000, 4)))
                phonemes.append(parts[2])

            # Write the formatted output to the output file
            output_filename = os.path.join(subdir, 'transcriptions.txt')
            with open(output_filename, 'a') as outfile:
                outfile.write(transcription + '|' + 'ichangethethongstwotimesaday' + '|' + ' '.join(phonemes) + '|rest|0|' + ' '.join(timings) + '|0\n')

        elif filename.endswith('.wav'):
            # Move the .wav file to the new directory
            src_file = os.path.join(subdir, filename)
            dst_file = os.path.join(new_dir, filename)
            shutil.move(src_file, dst_file)
