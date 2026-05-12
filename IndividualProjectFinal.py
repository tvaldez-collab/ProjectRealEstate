import tkinter as tk
import matplotlib.pyplot as plt

# Function to show graph
def show_graph(annual_profit, down_payment):
    years = list(range(1, 11))
    profits = [annual_profit * year for year in years]

    plt.figure()
    plt.plot(years, profits, label="Profit Over Time")

    # Break-even line
    plt.axhline(y=down_payment, linestyle='--', label="Break-even (Down Payment)")

    # If profitable, mark break-even point
    if annual_profit > 0:
        break_even_years = down_payment / annual_profit
        if break_even_years <= 10:
            plt.scatter(break_even_years, down_payment)
            plt.text(break_even_years, down_payment,
                     f" Break-even: {break_even_years:.1f} yrs")

    plt.xlabel("Years")
    plt.ylabel("Total Profit ($)")
    plt.title("Profit vs Break-even Analysis")
    plt.legend()
    plt.grid()
    plt.show()


# Main calculation function
def calculate():
    try:
        price = float(entry_price.get())
        rent = float(entry_rent.get())
        expenses = float(entry_expenses.get())
        down_payment = float(entry_down.get())

        # Calculations
        cash_flow = rent - expenses
        annual_profit = cash_flow * 12

        if down_payment == 0:
            roi = 0
        else:
            roi = (annual_profit / down_payment) * 100

        # Break-even calculation
        if annual_profit > 0:
            break_even_years = down_payment / annual_profit
            break_even_text = f"{break_even_years:.1f} years"
        else:
            break_even_text = "No break-even (losing money)"

        # Rating system (customized)
        if roi > 12:
            rating = "Excellent Investment"
        elif roi > 8:
            rating = "Moderate Deal"
        else:
            rating = "High Risk"

        # Display results
        result_label.config(
            text=f"Cash Flow: ${cash_flow:.2f}\n"
                 f"Annual Profit: ${annual_profit:.2f}\n"
                 f"ROI: {roi:.2f}%\n"
                 f"Break-even: {break_even_text}\n"
                 f"Rating: {rating}"
        )

        # Show graph
        show_graph(annual_profit, down_payment)

    except ValueError:
        result_label.config(text="Please enter valid numbers.")


# GUI setup
root = tk.Tk()
root.title("Real Estate Investment Analyzer")
root.geometry("350x420")

tk.Label(root, text="Real Estate Analyzer", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Property Price").pack()
entry_price = tk.Entry(root)
entry_price.pack()

tk.Label(root, text="Monthly Rent").pack()
entry_rent = tk.Entry(root)
entry_rent.pack()

tk.Label(root, text="Monthly Expenses").pack()
entry_expenses = tk.Entry(root)
entry_expenses.pack()

tk.Label(root, text="Down Payment").pack()
entry_down = tk.Entry(root)
entry_down.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

root.mainloop()