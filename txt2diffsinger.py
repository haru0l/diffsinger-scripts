import os

# Define the directory where the .txt files are located
directory = os.getcwd()

# Open the output file for writing
with open('transcriptions.txt', 'w') as outfile:

    # Loop over all .txt files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.lab'):
            filepath = os.path.join(directory, filename)

            # Open the input file and read the lines
            with open(filepath, 'r') as infile:
                lines = infile.readlines()

            # Extract the transcription from the filename
            transcription = filename[:-4]

            # Loop over the lines and extract the phonemes and timings
            timings = []
            phonemes = []
            for line in lines:
                parts = line.strip().split()
                timings.append(str(round(float(parts[1]) - float(parts[0]), 3)))
                phonemes.append(parts[2])

            # Write the formatted output to the output file
            outfile.write(transcription + '|' + 'ichangethethongstwotimesaday' + '|' + ' '.join(phonemes) + '|rest|0|' + ' '.join(timings) + '|0\n')
