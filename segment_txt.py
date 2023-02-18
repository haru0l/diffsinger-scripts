import os
import librosa
import glob
import soundfile as sf

# Set the path to the directory containing the audio files and text files
dir_path = os.getcwd()

# Find all the audio files in the directory
audio_files = glob.glob(os.path.join(dir_path, "*.wav"))

for audio_file_path in audio_files:
    # Set the path to the corresponding text file
    text_file_path = os.path.splitext(audio_file_path)[0] + ".txt"
    if not os.path.exists(text_file_path):
        continue

    # Load the audio file
    audio, sr = librosa.load(audio_file_path, sr=None)

    # Read the text file and create a list of segment start and end times
    segment_times = []
    with open(text_file_path, 'r') as f:
        lines = f.readlines()
        prev_end = 0
        pau_count = 0
        segment_count = 0
        for line in lines:
            start, end, label = line.strip().split()
            end = float(end)
            if label == 'pau':
                pau_count += 1
                if pau_count % 3 == 1:
                    segment_times.append((prev_end, end))
                    prev_end = end
                    segment_count += 1

    # Segment the audio file based on the segment start and end times
    for i, (start, end) in enumerate(segment_times):
        segment_audio = audio[int(start*sr):int(end*sr)]
        segment_file_path = f"{os.path.splitext(audio_file_path)[0]}_{i+1}.wav"
        sf.write(segment_file_path, segment_audio, sr, 'PCM_24')
        
        # Create a new text file for the segment
        segment_text_file_path = f"{os.path.splitext(text_file_path)[0]}_{i+1}.txt"
        with open(segment_text_file_path, 'w') as f:
            for line in lines:
                line_start, line_end, label = line.strip().split()
                line_start, line_end = float(line_start), float(line_end)
                if line_start >= end:
                    break
                if line_end <= start:
                    continue
                line_start = max(line_start, start) - start
                line_end = min(line_end, end) - start
                f.write(f"{line_start:.4f}\t{line_end:.4f}\t{label}\n")
