str = 'X-DSPAM-Confidence:    0.8475'
index = str.find(":")
required = str[index+1:]
print(required.strip())
print(float(required))
