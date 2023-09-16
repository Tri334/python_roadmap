'''Panggil function terus menerus sampai ada waktunya dia berhenti'''

def ulangiFungsiSebanyakX(loops):
    counter = 0
    data = True
    while data:
        counter+=1
        print('looping ke',counter)
        if counter == loops:
            data = False
            print('Program di looping sebanyak',counter)
            
'''Ulangi function sebanyak x kali'''
ulangiFungsiSebanyakX(10)