assembly = {
    'LOAD': '00100101',
    'STOR': '00100110',
    'ADD': '00100111',
    'SUB': '00101000',
    'MUL': '00101001',
    'CMP': '00101010',
    'RST': '00101011',
    'JUMP+': '00101100',
    'LOADMQ': '00101101',
    'LOADMQAC': '00101110',
    'END': '11111111',
    'NONE': '000000000000',
    'NOP': '11111110'
}

with open('instructions.txt', 'r') as file1, open('binary_code.txt',
                                                  'w') as file2:
  for line in file1:
    # file2.write('0b')
    for word in line.split():
      if word in assembly:
        file2.write(assembly[word])
      elif word.startswith('M(') and word.endswith('0:19)'):
        temp = format(int(word[2:-6]), '012b')
        file2.write(temp)
      elif word.startswith('M(') and word.endswith(')'):
        temp = format(int(word[2:-1]), '012b')
        file2.write(temp)
      else:
        temp = format(int(word), '012b')
        file2.write(f'{temp} ')
    file2.write('\n')