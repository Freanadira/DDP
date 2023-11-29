def konsonan(kampus):
    huruf = ''
    
    for i in kampus:
        if i not in 'aiueo':
        #menambah konsonan ke dtring kosong
            huruf += i
    return huruf

#memanggil fungsi konsonan dengan sting Nurul Fikri

hasil = konsonan("Nurul Fikri")

print('Huruf konsonan dari Nurul Fikri adalah', hasil)