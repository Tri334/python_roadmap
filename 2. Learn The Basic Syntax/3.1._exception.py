''' Exception biasanya untuk Bypass Suatu error '''

''' Saat kita ingin print suatu_varibale tetapi tidak di deklarasikan terlebih, 
    dahulu maka akan error 
'''
try:
    print(suatu_variable)
except:
    print('Tidak ada variable')
    
    
try:
    print('Jika tidak error')
except:
    print('Jika error')
else:
    ''' Akan ter eksekusi jika program jalan saat di 'try' '''
    print('Jika program tidak ada yang tidak error')
finally:
    ''' Tereksekusi program mau jalan ataupun tidak. '''
    print('program jalan')