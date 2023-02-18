import os
import librosa
import glob
import soundfile as sf

# Set the path to the directory containing the audio files and text files
dir_path = os.getcwd()

# Find all the audio files in the directory
audio_files = [f for f in os.listdir(dir_path) if f.endswith(".wav")]

# Create the output directory if it doesn't exist
out_dir = "./out"
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

for audio_file in audio_files:
    # Set the path to the corresponding text file
    text_file = os.path.splitext(audio_file)[0] + ".lab"
    text_file_path = os.path.join(dir_path, text_file)

    # Load the audio file
    audio, sr = librosa.load(os.path.join(dir_path, audio_file), sr=None)

    # Read the text file and create a list of segment start and end times
    segment_times = []
    with open(text_file_path, 'r') as f:
        lines = f.readlines()
        prev_end = 0
        pau_count = 0
        segment_count = 0
        for line in lines:
            start, end, label = line.strip().split()
            start = float(start) / 10000000
            end = float(end) / 10000000
            if label == 'pau':
                pau_count += 1
                if pau_count % 3 == 1:
                    segment_times.append((prev_end, start))
                    prev_end = start
                    segment_count += 1
                    
    # Segment the audio file based on the segment start and end times
    for i, (start, end) in enumerate(segment_times):
        segment_audio = audio[int(start*sr):int(end*sr)]
        segment_file = f"{os.path.splitext(audio_file)[0]}_{i+1}.wav"
        segment_file_path = os.path.join(out_dir, segment_file)
        sf.write(segment_file_path, segment_audio, sr, 'PCM_24')

        # Create a new text file for the segment
        segment_text_file = f"{os.path.splitext(text_file)[0]}_{i+1}.txt"
        segment_text_file_path = os.path.join(out_dir, segment_text_file)
        with open(segment_text_file_path, 'w') as f:
            for line in lines:
                line_start, line_end, label = line.strip().split()
                line_start, line_end = float(line_start), float(line_end)
                line_start /= 10000000
                line_end /= 10000000
                if line_end <= start:
                    continue
                if line_start >= end:
                    break
                line_start = max(line_start, start) - start
                line_end = min(line_end, end) - start
                f.write(f"{line_start:.4f} {line_end:.4f} {label}\n")
