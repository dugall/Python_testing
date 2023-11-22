#3: Slice list into 3 equal chunks and reverse each chunk

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

#chunk_begin = sample_list[:3]
#chunk_end = sample_list[3:]
#chunk_mid = []

def split_list(sample_list, chunk_size):
    return [sample_list[i:i + chunk_size] for i in range(0, len(sample_list), chunk_size)]

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk_size = 3
chunks = split_list(sample_list, chunk_size)

print(chunks)