## converts tacotron2 style transcriptions into separate txt files
filename = "list.txt"

with open(filename, "r") as file:
    for line in file:
        parts = line.strip().split("|")
        input_file_name = parts[0].replace("wavs/", "")
        outfile_name = input_file_name.replace(".wav", "")
        try:
            with open(f"{outfile_name}.txt", "w") as outfile:
                outfile.write(parts[1])
        except Exception as e:
            print(f"Error creating output file {outfile_name}.txt: {e}")
