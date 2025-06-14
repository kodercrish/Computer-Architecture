import math

with open('gcc.trace', 'r') as file1:
  # ins is a list that stores each line of input file on corresponding indices
  ins = file1.read().splitlines()

  # creating a list that will contain (only) the addresses from the ins
  addresses = []

  for line in ins:
    parts = line.split()
    addresses.append(parts[1])


##################
# we need to set these values inside the code itself
cache_size = 1024*1024  #bytes
block_size = 4          #bytes
ways_in_cache = 32       #ways
index_size = cache_size // (block_size * ways_in_cache)  #decimal number

cache_size_log = int(math.log2(cache_size))       #power of 2
block_size_log = int(math.log2(block_size))       #power of 2 #offset bits
ways_in_cache_log = int(math.log2(ways_in_cache)) #power of 2
index_size_log = int(math.log2(index_size))       #power of 2

tag_bits = 32 - index_size_log - block_size_log
##################


# creating a 4-way set associative cache which contains 65536 lines, each having 4 blocks/ways, and each block having 3 parameters, i.e. valid bit, tag bits and time_stamp
# cache[i][j][0] --- access to valid bit of jth block in ith line
# cache[i][j][1] --- access to tag bits of jth block in ith line
# cache[i][j][2] --- access to last used timestamp of jth block in ith line
# initial value of valid, tag bits and time_stamp respectively are 0, None and 0 respectively
cache = [[[0, None, 0] for _ in range(ways_in_cache)] for _ in range(index_size)]

# main logic
hits = 0    #count of number of hits
misses = 0  #count of number of misses
time_stamp = 0  #to track order of usage of LRU

for each_ads in addresses:
  # change the address from hex to binary
  bin_address = bin(int(each_ads, 16))[2:].zfill(32)    # Remove the '0b' prefix and makes 32bits string
  tag = bin_address[0 : tag_bits]        # bits for tag
  index = bin_address[tag_bits : 32-block_size_log]     # bits for index(line number)
  offset = bin_address[32-block_size_log : 32]    # bits for byte offset

  index_int = int(index, 2)  # Convert index from binary to integer for cache access
  tag_match = False          # to check if we have a tag match

  #check if the instruction is a cache miss or a cache hit
  for j in range(ways_in_cache):
    if(cache[index_int][j][0] == '1' and cache[index_int][j][1] == tag):  #cache hit
      hits = hits+1
      tag_match = True
      cache[index_int][j][2] = time_stamp  # Update the last used time_stamp
      break
    
  if not tag_match: #cache miss
    misses = misses+1

    # Find an empty block to replace (where valid bit=='0')
    for j in range(ways_in_cache):
      if(cache[index_int][j][0]=='0'):  #empty block
        cache[index_int][j][0] = '1'  # set valid bit
        cache[index_int][j][1] = tag  #store the tag
        cache[index_int][j][2] = time_stamp  # Update the last used time_stamp
        break

      else: #no empty block
        #finding the lru block from respective line/set
        lru_idx = 0
        for j in range(ways_in_cache):
          if(cache[index_int][j][2]<cache[index_int][lru_idx][2]):
            lru_idx = j
        
        #replacing the lru block
        cache[index_int][lru_idx][0] = '1'
        cache[index_int][lru_idx][1] = tag
        cache[index_int][lru_idx][2] = time_stamp

  time_stamp = time_stamp+1   # incrementing time_stamp after each instruction operation

print(hits)
print(misses)