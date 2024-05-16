def main_code(memory):
  instructions = {}
  for ele in memory:
    instructions[ele[0]] = ele[1]

  PC = memory[0][0]
  MAR = '0'
  MBR = '0'
  IBR = '0'
  IR = '0'
  AC = '0'
  MQ = '0'
  print('PC:', PC, ' MAR:', MAR, ' MBR:', MBR, ' IBR:', IBR, ' IR:', IR,
        ' AC:', AC, ' MQ:', MQ, ('\n\n'))

  t=0
  
  while (IR != '11111111'):

    print('------------------------------------')
    print('Modification of PC and corresponding values of other components :')
    print('PC:',PC)
    MAR = PC
    print('MAR:', MAR, ' -> ', end='')
    MBR = instructions[MAR]
    print('MBR:', MBR, ' -> ', end='')
    IBR = MBR[20:40]
    print('IBR:', IBR, ' and ', end='')
    IR = MBR[0:8]
    print('IR:', IR, ' and ', end='')
    MAR = MBR[8:20]
    print('MAR:', MAR)
    print('-------------------------------------')
    print()

    i = 0
    while (i < 2 and IR!='11111111'):
      if (IR == '00100101'):  #LOAD
        print('LOAD : ')
        print('MAR:', MAR, ' -> ', end='')
        MBR = instructions[MAR]
        print('MBR:', MBR, ' -> ', end='')
        AC = MBR
        print('AC:', AC, '\n')

      elif (IR == '00100110'):  #STOR
        print('STOR : ')
        print('AC:', AC, ' -> ', end='')
        MBR = AC.zfill(20)
        print('MBR:', MBR, ' -> ', end='')
        instructions[MAR] = MBR
        print('[address:', MAR, ' -> value:', instructions[MAR], ']\n')
        # here there can be issues as we are changing the value
        # of data in instructions[MAR] but not changing it in
        # memory(list), although it might not cause error

      elif (IR == '00100111'):  #ADD
        print('ADD : ')
        print('MAR:', MAR, ' -> ', end='')
        MBR = instructions[MAR]
        print('MBR:', MBR, ' -> ', end='')
        AC = str(format(int(AC, 2) + int(MBR, 2), '012b'))
        print('AC:', AC, '\n')

      elif (IR == '00101000'):  #SUB
        print('SUB : ')
        print('MAR:', MAR, ' -> ', end='')
        MBR = instructions[MAR]
        print('MBR:', MBR, ' -> ', end='')
        AC = str(format(int(AC, 2) - int(MBR, 2), '012b'))
        print('AC:', AC, '\n')

      elif (IR == '00101001'):  #MUL
        print('MUL : ')
        print('MAR:', MAR, ' -> ', end='')
        MBR = instructions[MAR]
        print('MBR:', MBR, ' -> ', end='')
        MQ = str(format(int(MQ, 2) * int(MBR, 2), '012b'))
        print('MQ:', MQ, '\n')

      elif (IR == '00101010'):  #CMP
        print('CMP : ')
        print('MAR:', MAR, ' -> ', end='')
        MBR = instructions[MAR]
        print('MBR:', MBR, ' -> ', end='')
        if (int(AC, 2) < int(MBR, 2)):
          AC = '11111111'
        print('ÁC:', AC, '\n')

      elif (IR == '00101011'):  #RST
        print('RST : ')
        print('MAR:', MAR, ' -> ', end='')
        MBR = instructions[MAR]
        print('MBR:', MBR, ' -> ', end='')
        AC = MBR
        print('AC:', AC, ' -> ', end='')
        AC = format(1, '012b')
        print('AC:', AC, ' -> ', end='')
        MBR = AC.zfill(20)
        print('MBR:', MBR, ' -> ', end='')
        instructions[MAR] = MBR
        print('[address:', MAR, ' -> value:', instructions[MAR], ']\n')

      elif (IR == '00101100'):  #JUMP+
        print('JUMP+ : ')
        if (AC!='11111111'):
          print('PC:', PC)
          # PC = memory[int(MAR, 2) - 5][0]
          PC = (str(bin(int(MAR,2))[2:]).zfill(12))
          print('PC:', PC)
          i=0
          
          IBR = instructions[MAR][20:40]
          IR = instructions[MAR][0:8]
          MAR = instructions[MAR][8:20]
          print('IR:',IR)
          print('MAR:',MAR)
          print()
          t=-1
          continue
        else:
          print('No jump')


      elif (IR == '00101101'):  #LOADMQ #LOAD MQ,M(X) #loads data from M(X) to MQ
        print('LOADMQ : ')
        print('MAR:', MAR, ' -> ', end='')
        MBR = instructions[MAR]
        print('MBR:', MBR, ' -> ', end='')
        MQ = MBR
        print('MQ:', MQ, '\n')

      elif (IR == '00101110'):  #LOADMQAC #LOAD MQ #loads data from MQ to AC
        print('LOADMQAC : ')
        print('MQ:', MQ, ' -> ', end='')
        AC = MQ
        print('AC:', AC, '\n')

      IR = IBR[0:8]
      MAR = IBR[8:20]
      if(i==0):
        print('Modification of IR nad MAR :')
        print('IR : ', IR)
        print('MAR : ', MAR)
        print()
      i = i + 1
    t = t + 1
    PC = memory[t][0]

  return instructions['000001110101']


with open('binary_code.txt', 'r') as f:
  lines = f.readlines()
memory = []
for each_line in lines:
  words = each_line.split()
  memory.append(words)
ans = main_code(memory)
print('Answer = ',int(ans, 2))
print('Thank You :)')