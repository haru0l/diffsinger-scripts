# DiffSinger Scripts

Basically some scripts to convert to the DiffSinger nomidi format.

## Script List


| Script | Function |
| ------ | ------ |
| convert_tt2.py | This basically splits a Tacotron2 type dataset (list.txt) into each own .txt file, useful for alignment with MFA. |
| lab2diffsinger.py | This converts ALL .lab (HTK format) files in your folder into a DiffSinger nomidi format in transcription.txt. |
| txt2diffsinger.py | Same as lab2diffsinger but using .txt files (Audacity format) instead of .lab files. |
| segment_audio.py | This just segments your audio using PyDub into chunks. |
| segment_lab.py | This just segments your audio but using a .lab file for reference (it segments at every 3rd pau). It also has a bug that the first file is silence. |
| segment_txt.py | Same as segment_lab.py but with .txt instead. |
