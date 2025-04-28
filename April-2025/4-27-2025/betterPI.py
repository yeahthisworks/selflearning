from decimal import Decimal, getcontext

def bs(a, b):
    if b - a == 1:
        if a == 0:
            Pab = Qab = 1
        else:
            Pab = (6*a-5)*(2*a-1)*(6*a-1)
            Qab = a*a*a*26680*640320**3//24
        Tab = Pab * (13591409 + 545140134*a)
        if a % 2:
            Tab = -Tab
    else:
        m = (a + b) // 2
        Pam, Qam, Tam = bs(a, m)
        Pmb, Qmb, Tmb = bs(m, b)
        Pab = Pam * Pmb
        Qab = Qam * Qmb
        Tab = Tam * Qmb + Pam * Tmb
    return Pab, Qab, Tab

def compute_pi_bs(digits):
    getcontext().prec = digits + 10  # extra precision

    n = digits // 14 + 1
    P, Q, T = bs(0, n)
    one_squared = Decimal(10005)
    C = 426880 * one_squared.sqrt()
    pi = C * Q / T
    return str(pi)[:digits+2]

def main():
    try:
        digits = int(input("Enter number of digits of Pi: "))
        if digits <= 0:
            print("Enter a positive integer.")
            return
        print("Calculating... This might take some time.")
        pi_val = compute_pi_bs(digits)
        print(pi_val)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
