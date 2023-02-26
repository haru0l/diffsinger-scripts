import mytextgrid
import os

# Function to convert TextGrid to lab file
def textgrid_to_lab(textgrid_file):
    tg = mytextgrid.read_from_file(textgrid_file)
    lab_lines = []
    for tier in tg:
        if tier.name =='None_2' and tier.is_interval():
            for interval in tier:
                time_start = int(float(interval.xmin)*10000000)
                time_end = int(float(interval.xmax)*10000000)
                label = interval.text
                if label == '':
                    label = 'pau'
                lab_lines.append(f"{time_start} {time_end} {label}")
    return lab_lines

# Get all TextGrid files in subfolders
for subdir, dirs, files in os.walk("./"):
    for file in files:
        if file.endswith(".TextGrid"):
            textgrid_file = os.path.join(subdir, file)
            lab_lines = textgrid_to_lab(textgrid_file)
            # Write lab lines to a space separated lab file
            lab_file = textgrid_file.replace(".TextGrid", ".lab")
            with open(lab_file, 'w') as f:
                for lab_line in lab_lines:
                    f.write("%s\n" % lab_line)
            print(f"Converted {textgrid_file} to {lab_file}")
