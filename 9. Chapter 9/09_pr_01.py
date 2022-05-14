f= open('poem.txt','r')
t=f.read()
if 'Twinkle' in t:
    print ('Twinkle is present')
else:
    print('Twinkle is not present')
f.close()