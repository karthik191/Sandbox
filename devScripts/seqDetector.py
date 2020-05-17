outFile = open("testPattern.log","w+")
#seq detect 101
import random
for index in range(0,50000):
    print(random.randint(0, 1), file = outFile)
outFile.close()

inputSequence = [random.randint(0,1) for i in range(0,500000)]
sequenceIndex = 0
outputSequence = []
for sequence in inputSequence:
    if sequenceIndex > 2 :
        if inputSequence[sequenceIndex] == '1' and inputSequence[sequenceIndex-1] == '0' and inputSequence[sequenceIndex-2] == '1':
            outputSequence.append('1')
            print(int(sequence),1,'->SEQ FOUND')
        else:
            outputSequence.append('0')
            print(int(sequence), 0)

    else:
        outputSequence.append('0')
        print(int(sequence), 0)
    sequenceIndex += 1
