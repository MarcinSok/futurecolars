def calculate_loan_balance(principal, interest_rate, inflation_rate, payment):
    balance = principal
    for month in range(24):
        interest = (balance + payment) * (interest_rate - inflation_rate) / 12
        balance = (balance + interest - payment)
        if balance <= 0:
            break
        difference = principal - balance
        print(f"Twoja pozostała kwota kredytu to {balance:.2f}, to {difference:.2f} mniej niż w poprzednim miesiącu.")
    return balance

principal = float(input("Podaj kwotę początkowego kredytu: "))
interest_rate = float(input("Podaj oprocentowanie kredytu (ponad inflację): "))
inflation_rate = float(input("Podaj wartość inflacji: "))
payment = float(input("Podaj stałą wartość raty: "))

calculate_loan_balance(principal, interest_rate, inflation_rate, payment)
