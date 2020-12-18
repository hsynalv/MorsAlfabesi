morsKodları = {
    'a':'.- ',   'b':'-... ',  'c':'-.-. ',  'd':'-.. ',  'e':'. ',    'f':'..-. ',  'g':'--. ',
    'h':'.... ', 'i':'.. ',    'j':'.--- ',  'k':'-.- ',  'l':'.-.. ', 'm':'-- ',    'n':'-. ',
    'o':'--- ',  'p':'.--. ',  'q':'--.- ',  'r':'.-. ',  's':'... ',  't':'- ',     'u':'..- ',
    'v':'...- ', 'w':'.-- ',   'x':'-..- ',  'y':'-.-- ', 'z':'--.. ', ' ':' / '
    }

while True:
    çevirilecek = input("Mors Kodlarına Çevirmek İstediğiniz Kelimeyi ya da Cümleyi Giriniz(Çıkış:q): ")
    if çevirilecek == 'q':
        break;
    print(çevirilecek + ": ",end="")
    çevirilecek = çevirilecek.lower()
    for i in çevirilecek:
        print(morsKodları[i],end="")
    print()
