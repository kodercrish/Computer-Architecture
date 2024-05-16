with open('binary_3.txt', 'r') as file1, open('byte_add_mem.txt', 'w') as file2:  //While running this code, change file1 here
  ins = file1.read().splitlines()
  for i in ins:
    line1 = i[0:8]
    line2 = i[8:16]
    line3 = i[16:24]
    line4 = i[24:32]
    file2.write(line1)
    file2.write('\n')
    file2.write(line2)
    file2.write('\n')
    file2.write(line3)
    file2.write('\n')
    file2.write(line4)
    file2.write('\n')

dataMem = {      #datamem{string, string}
  '00010000000000010000000000000000' : '00000000',
  '00010000000000010000000000000001' : '00000000',
  '00010000000000010000000000000010' : '00000000',
  '00010000000000010000000000000011' : '00000000',
  
  '00010000000000010000000000000100' : '00000000',
  '00010000000000010000000000000101' : '00000000',
  '00010000000000010000000000000110' : '00000000',
  '00010000000000010000000000000111' : '00000000',
  
  '00010000000000010000000000001000' : '00000000',
  '00010000000000010000000000001001' : '00000000',
  '00010000000000010000000000001010' : '00000000',
  '00010000000000010000000000001011' : '00000001',

  
  '00010000000000010000000000001100' : '00000000',
  '00010000000000010000000000001101' : '00000000',
  '00010000000000010000000000001110' : '00000000',
  '00010000000000010000000000001111' : '00000000',
  
  '00010000000000010000000000010000' : '00000000',
  '00010000000000010000000000010001' : '00000000',
  '00010000000000010000000000010010' : '00000000',
  '00010000000000010000000000010011' : '00000001',
  
  '00010000000000010000000000010100' : '00000000',
  '00010000000000010000000000010101' : '00000000',
  '00010000000000010000000000010110' : '00000000',
  '00010000000000010000000000010111' : '00000000',
  
  '00010000000000010000000000011010' : '00000000',
  '00010000000000010000000000011001' : '00000000',
  '00010000000000010000000000011000' : '00000000',
  '00010000000000010000000000011011' : '00000001',
  
  '00010000000000010000000000011100' : '00000000',
  '00010000000000010000000000011101' : '00000000',
  '00010000000000010000000000011110' : '00000000',
  '00010000000000010000000000011111' : '00000000',
  
  '00010000000000010000000000100000' : '00000000',
  '00010000000000010000000000100001' : '00000000',
  '00010000000000010000000000100010' : '00000000',
  '00010000000000010000000000100011' : '00000000',
  
  
  '00010000000000010000000000100100' : '00000000',
  '00010000000000010000000000100101' : '00000000',
  '00010000000000010000000000100110' : '00000000',
  '00010000000000010000000000100111' : '00000000',
  
  '00010000000000010000000000101000' : '00000000',
  '00010000000000010000000000101001' : '00000000',
  '00010000000000010000000000101010' : '00000000',
  '00010000000000010000000000101011' : '00000000',
  
  '00010000000000010000000000101100' : '00000000',
  '00010000000000010000000000101101' : '00000000',
  '00010000000000010000000000101110' : '00000000',
  '00010000000000010000000000101111' : '00000000',
  
  '00010000000000010000000000110000' : '00000000',
  '00010000000000010000000000110001' : '00000000',
  '00010000000000010000000000110010' : '00000000',
  '00010000000000010000000000110011' : '00000000',
  
  '00010000000000010000000000110100' : '00000000',
  '00010000000000010000000000110101' : '00000000',
  '00010000000000010000000000110110' : '00000000',
  '00010000000000010000000000110111' : '00000000',
  
  '00010000000000010000000000111000' : '00000000',
  '00010000000000010000000000111001' : '00000000',
  '00010000000000010000000000111010' : '00000000',
  '00010000000000010000000000111011' : '00000000', 
}

registers = {    #registers{string, int}
  '00010': 0,    #$v0
  '00011': 0,    #$v1
  '10000': 0,    #$s0
  '10001': 0,    #$s1
  '10010': 0,    #$s2
  '10011': 0,    #$s3
  '10100': 0,    #$s4
  '10101': 0,    #$s5
  '10110': 0,    #$s6
  '10111': 0,    #$s7
  '01000': 0,    #$t0
  '01001': 0,    #$t1
  '01010': 0,    #$t2
  '01011': 0,    #$t3
  '01100': 0,    #$t4
}
registers['10111'] = 268500992

# Dictionary of instructions
instructions = {}      #instructions{string, string}
with open('byte_add_mem.txt', 'r') as file:
  starting_add = 0b00000000010000000000000000000000
  add = starting_add
  for line in file:
    add_str = format(add, '032b')
    instructions[add_str] = line
    add = add + 1



pc = '00000000010000000000000000000000'
while True:
  print()
  print(f'PC is {pc}')
  print()
  print('--------------------------------------------------------------------------')

  i1 = instructions[format(int(pc,2),'032b')][:8]
  i2 = instructions[format(int(pc,2) + 1, '032b')][:8]
  i3 = instructions[format(int(pc,2) + 2, '032b')][:8]
  i4 = instructions[format(int(pc,2) + 3, '032b')][:8]
  i = i1 + i2 + i3 + i4
  print(f'Instruction is {i}')

  opcode = i[0:6]

  print(f'Opcode is {opcode}')
  print()

  jump = 0
  match opcode:

    # R Format
    case '000000':
      #print('Instruction is R Format')
      rs = i[6:11]
      rt = i[11:16]
      rd = i[16:21]
      shamt = i[21:26]
      funct = i[26:32]

      print(f'rs is {rs}; rd is {rd}; rt is {rt}; shamt is {shamt}; funct is {funct}')
      
      if funct == '100000': #add
        print('Performing addition')
        
        readVal1 = registers[rs]
        readVal2 = registers[rt]

        registers[rd] = readVal1 + readVal2

        print(f'Addition of {readVal1} and {readVal2} is {registers[rd]}')
        print('Add Performed.')
        
      elif funct == '100010': #sub
        print('Performing subtraction')
        
        readVal1 = registers[rs]
        readVal2 = registers[rt]

        registers[rd] = readVal1 - readVal2

        print(f'Subtraction of {readVal1} and {readVal2} is {registers[rd]}')
        print('Sub Performed.')

      elif funct == '001100':  #syscall
        print('Performing syscall')

        if(registers['00010'] == 5):  #v0 = 00010 check once
          #print('Function code for syscall is 5')
          print('Give an integer input.')

          a = int(input())

          registers['00010'] = a # store in v0

          print(f'Stored {a} in v0')

        elif(registers['00010']==10):
          #print('Function code for syscall is 10.')
          #print('Exiting the program.')
          break
      
    case '011100': #mul
      print('Performing multiplication')
      rs = i[6:11]
      rt = i[11:16]
      rd = i[16:21]
      shamt = i[21:26]
      funct = i[26:32]

      print(f'rs is {rs}; rd is {rd}; rt is {rt}; shamt is {shamt}; funct is {funct}')
      
      readVal1 = registers[rs]
      readVal2 = registers[rt]

      registers[rd] = readVal1 * readVal2

      print(f'Multiplication of {readVal1} and {readVal2} is {registers[rd]}')
      print('Mul Performed.')


    # Loadword
    case '100011':
      print('Performed LW')
      
      rs = i[6:11]    #$s7
      rt = i[11:16]
      imm = i[16:32]

      print(f'rs is {rs}; rt is {rt}; imm is {imm}')

      imm_binary = int(imm, 2)
      readVal1 = registers[rs]

      d1 = dataMem[format(readVal1 + imm_binary, '032b')]
      d2 = dataMem[format(readVal1 + imm_binary + 1, '032b')]
      d3 = dataMem[format(readVal1 + imm_binary + 2, '032b')]
      d4 = dataMem[format(readVal1 + imm_binary + 3, '032b')]
      d = d1 + d2 + d3 + d4
      
      registers[rt] = int(d, 2)

      print(f'Loaded {registers[rt]} from Data Memory')

    # Storeword
    case '101011':
      print('Performing SW')
      
      rt = i[6:11]
      rs = i[11:16]      #$s7
      imm = i[16:32]

      readVal1 = registers[rs]
      readVal2 = registers[rt]

      valBin = format(readVal1, '032b')
      
      dataMem[format(readVal2 + int(imm, 2), '032b')] = valBin[:8]
      dataMem[format(readVal2 + int(imm, 2) + 1, '032b')] = valBin[8:16]
      dataMem[format(readVal2 + int(imm, 2) + 2, '032b')] = valBin[16:24]
      dataMem[format(readVal2 + int(imm, 2) + 3, '032b')] = valBin[24:32]
      
      print(f'Stored {readVal1} in Data Memory')


    #loadimmediate
    case '001001':
      print('Performing Load Immediate')
      
      rs = i[6:11]  #here in li,MARS does not implement it directly,instead it does addi
      rt = i[11:16]
      imm = i[16:32]

      registers[rt] = int(imm, 2)

      print(f'Loaded immediate value: {imm} in register: {rt}')


    #jump
    case '000010':
      print('Performing Jump')
      imm = i[6:32]
      print(f'Jumping to {imm}')
      
      imm = '0000' + imm + '00'
      pc = format(int(imm, 2), '032b')
      jump = 1

      print('Jump performed.')
  
    #bne
    case '000101':
      print('Performing Branch Not Equal')
      
      rs = i[6:11]
      rt = i[11:16]
      imm = i[16:32]
      print(f'rs is {rs}; rt is {rt}; imm is {imm}')
      

      imm_dec = int(imm, 2)
      readVal1 = registers[rs]
      readVal2 = registers[rt]
      if readVal1 != readVal2:
        pc = format((int(pc,2) + 4 + (imm_dec*4)), '032b')
        jump = 1

        print('Condition Met. Jumping now.')
      else:
        print('Condition not met. Not jumping.')      

    #beq
    case '000100':
      print('Performing Branch Equal')
      
      rs = i[6:11]
      rt = i[11:16]
      imm = i[16:32]
      print(f'rs is {rs}; rt is {rt}; imm is {imm}')

      imm_dec = int(imm, 2)
      readVal1 = registers[rs]
      readVal2 = registers[rt]
      if readVal1 == readVal2:
        pc = format((int(pc,2) + 4 + (imm_dec*4)), '032b')
        jump = 1
        print('Condition Met. Jumping now.')
      else:
        print('Condition not met. Not jumping.')

    #addi
    case '001000':
      print('Performing Add Immediate')
      
      rs = i[6:11]
      rt = i[11:16]
      imm = i[16:32]
      print(f'rs is {rs}; rt is {rt}; imm is {imm}')
      
      registers[rt] = registers[rs] + int(imm, 2)

      print(f'Addition of {registers[rs]} and {imm} is {registers[rt]}')


  #incrementing the value of pc
  if jump == 0:
    pc = format(int(pc,2) + 4, '032b')

  print('--------------------------------------------------------------------------')

print(f"Answer = {registers['10110']}\n")      # Answer is stored in $s6
print("Thank you :)")
print()
