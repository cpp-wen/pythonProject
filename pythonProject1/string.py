import re


def main():
    username = input('input you name ')
    qq = input('input you qq')
    m1 = re.match(r'^[0-9a-zA-z_]{6,20}$', username)
    if not m1:
        print("enter username is error")
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print("enter password is error")
    if m1 and m2:
        print("you enter is right®")


# if __name__ == '__main__'; 等于public static void main
if __name__ == '__main__':
    main()
