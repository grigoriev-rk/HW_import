from datetime import date
import people
import salary

    
if __name__ == '__main__':
    print('proverka svyazi')
    people.calculate_salary()
    salary.get_employees()
    today = date.today()
    print("Текущая дата :", today)