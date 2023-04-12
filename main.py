from stack import *

def main():
    # init dictionary, berisi seluruh bracket yang ada
    kumpulan_jawaban: dict = {
        ')' : '(',
        ']' : '[',
        '}' : '{',
        '>' : '<'
    }

    # main loop
    while True:
        # init stack
        stack:Stack = Stack()

        # inputan
        inputan: str = input('Input string yang akan di cek: ')

        # cek apakah inputan kosong
        if inputan == '':
            print('Inputan kosong')
            continue

        # cek inputan apakah ada yang bukan bracket
        input_valid: bool = True
        for s in inputan:
            if s not in kumpulan_jawaban.keys() and s not in kumpulan_jawaban.values():
                # jika ada inputan yang bukan bracket
                input_valid = False
                break

        # cek apakah inputan valid
        if not input_valid:
            print('Inputan tidak valid')
            continue

        # loop untuk cek inputan
        for s in inputan:
            # untuk setiap s di inputan
            if stack.isEmpty():
                # jika kosong maka push isi stack, tidak perlu cek apapun
                stack.push(s)
            else:
                # jika tidak kosong maka kita harus cek dulu apa yang ada di dalamnnya
                if kumpulan_jawaban.get(s) == stack.peek():
                    # jika ada musuhnya (bracket lawannya) maka pop
                    stack.pop()
                else:
                    # jika tidak maka push lagi
                    stack.push(s)     
        
        # cek apakah empty
        if stack.isEmpty():
            print('Benar, semua bracket sudah terbuka dan tertutup')
        else:
            print('Salah, ada bracket yang belum terbuka atau tertutup')

        # cek apakah mau lanjut
        print()
        if input('Lanjut? (y/n): ') == 'n':
            break

if __name__ == '__main__':
    main()