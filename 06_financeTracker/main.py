import pandas as pd
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from data_entry import getAmount, getCategory, getDate, getDescription

class CSV:
    CSV_FILE = "financeData.csv"
    COLUMNS = ["date", "amount", "category", "description"]

    @classmethod
    def initialize_csv(cls):
        
        try:
            pd.read_csv(cls.CSV_FILE)

        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
    
    @classmethod
    def add_entry(cls, date, amount, category, description):
        newEntry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }

        with open(cls.CSV_FILE, 'a', newline="") as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=cls.COLUMNS)
            writer.writerow(newEntry)
        print("Entry created successfully!")
    
    @classmethod
    def getTransactions(cls, startDate, endDate):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
        startDate = datetime.strptime(startDate, "%d-%m-%Y")
        endDate = datetime.strptime(endDate, "%d-%m-%Y")

        mask = (df["date"] >= startDate) & (df["date"] <= endDate)
        filteredDf = df.loc[mask]

        if filteredDf.empty:
            print("No transactions in the given date range.")
        
        else:
            print(f"Transactions from {startDate.strftime("%d-%m-%Y")} to {endDate.strftime("%d-%m-%Y")}")
            print(filteredDf.to_string(index=False, formatters={"date": lambda x: x.strftime("%d-%m-%Y")}))

            totalIncome = filteredDf[filteredDf["category"] == "Income"]["amount"].sum()
            totalExpense = filteredDf[filteredDf["category"] == "Expense"]["amount"].sum()

            print("\nSummary:")
            print(f"Total income: ₹{totalIncome:.2f}")
            print(f"Total expense: ₹{totalExpense:.2f}")
            print(f"Net Savings: ₹{(totalIncome-totalExpense):.2f}")

        return filteredDf


def add():
    CSV.initialize_csv()
    date = getDate("Enter the date of the transaction in DD-MM-YYYY format or press enter for today's date.", allowDefault=True)
    amount = getAmount()
    category = getCategory()
    description =getDescription()
    
    CSV.add_entry(date, amount, category, description)

def plot_transactions(df):
    df.set_index("date", inplace=True)
    
    incomeDf = df[df["category"] == "Income"].resample("D").sum().reindex(df.index, fill_value=0)
    expenseDf = df[df["category"] == "Expense"].resample("D").sum().reindex(df.index, fill_value=0)

    plt.figure(figsize=(10,8))
    plt.plot(incomeDf.index, incomeDf["amount"], label="Income", color='g')
    plt.plot(expenseDf.index, expenseDf["amount"], label="Expense", color='r')
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Summary")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    while True:
        print("\n1. Add a new transaction.")
        print("\n2. View transactions and a summmary within a range.")
        print("\n3. Exit.")

        choice = input("Enter choice (1-3): ")

        if choice=='1':
            add()
        
        elif choice=='2':
            start = getDate("Enter the start date in DD-MM-YYYY format: ")
            end = getDate("Enter the end date in DD-MM-YYYY format: ")
            
            df = CSV.getTransactions(start, end)
            if input("Do you want to see a plot? (y/n)").lower()=='y':
                plot_transactions(df)
        
        elif choice=='3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()


