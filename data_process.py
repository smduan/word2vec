import zipfile
import os
import tensorflow as tf
import collections

# Step 1: Download the data.
# pylint: disable=redefined-outer-name
def maybe_download(expected_bytes):
    """Download a file if not present, and make sure it's the right size."""
    # url = 'http://mattmahoney.net/dc/text8.zip'
    # local_filename, _ = urllib.request.urlretrieve(url ,'./text8.zip')
    local_filename = './data/text8.zip'
    statinfo = os.stat(local_filename)
    if statinfo.st_size == expected_bytes:
        print('Found and verified', local_filename)
    else:
        print(statinfo.st_size)
        raise Exception('Failed to verify ' + local_filename +'. Can you get to it with a browser?')

    return local_filename

# Read the data into a list of strings.
def read_data(filename):
    """Extract the first file enclosed in a zip file as a list of words."""
    with zipfile.ZipFile(filename) as f:
        print(f.namelist())
        #读取文件中的二进制数据，并转化成str
        data = tf.compat.as_str(f.read(f.namelist()[0])).split()
    return data

vocabulary_size = 50000
def build_dataset(words, n_words):
    """Process raw inputs into a dataset."""
    count = [['UNK', -1]]
    #print(collections.Counter(words).most_common(n_words - 1))
    #数据类型[['UNK', 0], ('the', 1061396), ('of', 593677), ('and', 416629), ('one', 411764)]
    count.extend(collections.Counter(words).most_common(n_words - 1))

    #将数组内数据转化成字典，{'UNK': 0, 'the': 1, 'of': 2, 'and': 3, 'one': 4, 'in': 5}
    dictionary = dict()
    for word, _ in count:
        dictionary[word] = len(dictionary)

    data = list()
    unk_count = 0
    for word in words:
        index = dictionary.get(word, 0)
        if index == 0:  # dictionary['UNK']
            unk_count += 1
        data.append(index)

    count[0][1] = unk_count
    reversed_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    return data, count, dictionary, reversed_dictionary

# Filling 4 global variables:
# data - list of codes (integers from 0 to vocabulary_size-1).
#   This is the original text but words are replaced by their codes
# count - map of words(strings) to count of occurrences
# dictionary - map of words(strings) to their codes(integers)
# reverse_dictionary - maps codes(integers) to words(strings)

if __name__ == '__main__':
    filename = maybe_download(31344016)
    vocabulary = read_data(filename)
    data, count, dictionary, reverse_dictionary = build_dataset(
        vocabulary, vocabulary_size)
    print('Data size', len(vocabulary))
    print('Most common words (+UNK)', count[:5])
    print('Sample data', data[:10], [reverse_dictionary[i] for i in data[:10]])

