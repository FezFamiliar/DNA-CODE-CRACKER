

DNA_BINARY = {
	'A' : '00',
	'C' : '10',
	'G' : '01',
	'T' : '11'
}

DNA_ASCII = {
	'AAA' : 'a',
	'AAC' : 'b',
	'AAG' : 'c',
	'AAT' : 'd',
	'ACA' : 'e',
	'ACC' : 'f',
	'ACG' : 'g',
	'ACT' : 'h',
	'AGA' : 'i',
	'AGC' : 'j',
	'AGG' : 'k',
	'AGT' : 'l',
	'ATA' : 'm',
	'ATC' : 'n',
	'ATG' : 'o',
	'ATT' : 'p',
	'CAA' : 'q',
	'CAC' : 'r',
	'CAG' : 's',
	'CAT' : 't',
	'CCA' : 'u',
	'CCC' : 'v',
	'CCG' : 'w',
	'CCT' : 'x',
	'CGA' : 'y',
	'CGC' : 'z',
	'CGG' : 'A',
	'CGT' : 'B',
	'CTA' : 'C',
	'CTC' : 'D',
	'CTG' : 'E',
	'CTT' : 'F',
	'GAA' : 'G',
	'GAC' : 'H',
	'GAG' : 'I',
	'GAT' : 'J',
	'GCA' : 'K',
	'GCC' : 'L',
	'GCG' : 'M',
	'GCT' : 'N',
	'GGA' : 'O',
	'GGC' : 'P',
	'GGG' : 'Q',
	'GGT' : 'R',
	'GTA' : 'S',
	'GTC' : 'T',
	'GTG' : 'U',
	'GTT' : 'V',
	'TAA' : 'W',
	'TAC' : 'X',
	'TAG' : 'Y',
	'TAT' : 'Z',
	'TCA' : '1',
	'TCC' : '2',
	'TCG' : '3',
	'TCT' : '4',
	'TGA' : '5',
	'TGC' : '6',
	'TGG' : '7',
	'TGT' : '8',
	'TTA' : '9',
	'TTC' : '0',
	'TTG' : ' ',
	'TTT' : '.'

}
flag = []
encoded = 'ACGCTCGACGACGTAGCGAacgt'
encodedd = 'TTATTCg'
def decode(text,toggle):
	if(toggle == False):
		for x in text.upper():
			flag.append(DNA_BINARY[x])
	else:
		for x in range(0,len(text),3):
			flag.append(DNA_ASCII[text[x:x+3]])

	print ''.join(flag)


input1 = raw_input('Please paste your code here:')
input2 = raw_input('Decode to binary or ASCII? B\\A')


if(input2.upper() == 'B'):
	decode(input1,False)
else:
	decode(input1,True)





