from os import listdir, mkdir
from os.path import isfile, join
import string
import sys

# TODO: Get file path and chunk number from user input
filepath = sys.argv[1]
chunk_count = int(sys.argv[2])

output_dir = "output"

# Get file names from directory
only_files = [f for f in listdir(filepath) if isfile(join(filepath, f))]

# Set values for removing punctuation from files
remove = dict.fromkeys(map(ord, string.punctuation))

# Create directory for output files
output_folder = join(filepath, output_dir)
mkdir(output_folder)

for f in only_files:
    # Get name of current speaker to create directory
    dir_name = f[0:-4]
    print(dir_name)

    # Open current file from base directory
    curr_file = open(join(filepath, f))

    # Remove punctuation from current file, send to array
    file_data = curr_file.read().translate(remove)
    file_words = file_data.split()

    print("number of words: " + str(len(file_words)))

    # Create new directory for speaker data
    new_path = output_folder + "/"
    new_dir = join(new_path, dir_name)
    mkdir(new_dir)

    # Initialize values for iteration through files
    words_per_chunk = round((len(file_words)/chunk_count))
    print(words_per_chunk)
    word_start_index = 0
    word_end_index = words_per_chunk

    for i in range(0, chunk_count):
        print("Processing file #" + str(i+1) + ": " + dir_name)

        # Check if out of range for files that don't split evenly
        if i == (chunk_count - 1):
            if word_end_index != len(file_words):
                print("*********Non-matching value found ************")
                word_end_index = len(file_words)

        print("Looping through " + dir_name + " on " + str(i + 1) + "th loop")
        print("Starting index: " + str(word_start_index))
        print("Ending index: " + str(word_end_index))

        # Get array of words to print
        curr_chunk = file_words[word_start_index:word_end_index]

        # Increment values used to count words to print
        word_start_index += words_per_chunk
        word_end_index += words_per_chunk

        # Create string for output file name
        file_str = dir_name + "_" + str(i+1)
        chunk_file_name = join(new_dir, file_str)

        # Open output file and print array with spaces to it
        chunk_file = open(chunk_file_name + ".txt", "w")
        chunk_file.write(" ".join(curr_chunk))
        chunk_file.close()
