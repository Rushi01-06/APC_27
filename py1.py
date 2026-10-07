import pandas as pd

def highest_paid_employee(df):
    return df.loc[df['Salary'].idxmax()]

def department_avg_salary(df):
    return df.groupby('Department')['Salary'].mean().sort_values(ascending=False)

def main():
    data = {
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
        'Department': ['HR', 'IT', 'IT', 'Finance', 'Finance', 'HR'],
        'Salary': [50000, 75000, 80000, 65000, 70000, 55000]
    }
    df = pd.DataFrame(data)
    highest = highest_paid_employee(df)
    print("Highest Paid Employee:")
    print(highest)
    print("\nDepartment-wise Average Salary Ranking:")
    print(department_avg_salary(df))

if __name__ == "__main__":
    main()
