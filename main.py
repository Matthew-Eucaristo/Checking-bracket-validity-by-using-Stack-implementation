from stack import *

def main():
    # init stack
    stack = Stack()

    # init dictionary
    kumpulan_jawaban: dict = {
        ')' : '(',
        ']' : '[',
        '}' : '{',
        '>' : '<'
    }

    inputan = input('Input string yang akan di cek: ')

    for s in inputan:
        # untuk setiap s di inputan
        if stack.isEmpty():
            # jika kosong
            stack.push(s)
        else:
            # jika tidak kosong
            if kumpulan_jawaban.get(s) == stack.peek():
                # jika ada musuhnya langsung
                stack.pop()
                continue
            else:
                # jika tidak sama dengan bawahnya
                stack.push(s)     
    
    # cek popping stack

    # cek apakah empty
    if stack.isEmpty():
        print('benar')
    else:
        print('salah')

if __name__ == '__main__':
    main()