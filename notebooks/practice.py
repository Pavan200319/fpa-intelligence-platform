revenue=18_500_000
expenses=12_300_000

profit = revenue - expenses

print(profit)

company = "State Street"
margin = profit / revenue

print(f"{company} profit: ${profit:,.0f}")
print(f"Profit margin: {margin:.1%}")

budget = 13_000_000
variance = expenses - budget
variance_pct = variance / budget

print(f"Expense variance: ${variance:,.0f}")
print(f"Variance %: {variance_pct:.1%}")

# Lesson 3: Lists
quarterly_revenue = [4_200_000, 4_500_000, 4_700_000, 5_100_000]

print(quarterly_revenue[0])      # first quarter
print(quarterly_revenue[-1])     # last quarter
print(sum(quarterly_revenue))    # total for the year
print(len(quarterly_revenue))    # how many quarters
print(max(quarterly_revenue))    # best quarter

# Lesson 4: Dictionaries
budget_by_line = {
    "Salaries": 5_000_000,
    "Technology": 1_200_000,
    "Rent": 800_000,
}

print(budget_by_line["Technology"])     # look up one value

budget_by_line["Marketing"] = 300_000   # add a new line item
print(budget_by_line)

print(sum(budget_by_line.values()))     # total budget

budget = 13_000_000
variance = expenses - budget
variance_pct = variance / budget

print(f"Expense variance: ${variance:,.0f}")
print(f"Variance %: {variance_pct:.1%}")

# Lesson 3: Lists
quarterly_revenue = [4_200_000, 4_500_000, 4_700_000, 5_100_000]

print(quarterly_revenue[0])      # first quarter
print(quarterly_revenue[-1])     # last quarter
print(sum(quarterly_revenue))    # total for the year
print(len(quarterly_revenue))    # how many quarters
print(max(quarterly_revenue))    # best quarter

# Lesson 4: Dictionaries
budget_by_line = {
    "Salaries": 5_000_000,
    "Technology": 1_200_000,
    "Rent": 800_000,
}

print(budget_by_line["Technology"])     # look up one value

budget_by_line["Marketing"] = 300_000   # add a new line item
print(budget_by_line)

print(sum(budget_by_line.values()))     # total budget

quarterly_expenses = [3_100_000, 3_000_000, 3_300_000, 3_200_000]
avg_expense = sum(quarterly_expenses) / len(quarterly_expenses)
print(f"Average quarterly expense: ${avg_expense:,.0f}")

actuals = {
    "Salaries": 5_300_000,
    "Technology": 1_100_000,
    "Rent": 800_000,
}

salary_variance = actuals["Salaries"] - budget_by_line["Salaries"]
print(f"Salaries variance: ${salary_variance:,.0f}")

# Lesson 5: Loops
print("\n--- Variance report ---")

for line_item, budget_amount in budget_by_line.items():
    actual = actuals.get(line_item, 0)
    variance = actual - budget_amount
    print(f"{line_item}: actual ${actual:,.0f} | budget ${budget_amount:,.0f} | variance ${variance:,.0f}")

 # Lesson 6: If statements
print("\n--- Variance flags (5% materiality) ---")

threshold = 0.05

for line_item, budget_amount in budget_by_line.items():
    actual = actuals.get(line_item, 0)

    if budget_amount == 0:
        continue

    variance_pct = (actual - budget_amount) / budget_amount

    if variance_pct > threshold:
        print(f"🔴 {line_item} is {variance_pct:.1%} OVER budget (unfavorable)")
    elif variance_pct < -threshold:
        print(f"🟢 {line_item} is {abs(variance_pct):.1%} UNDER budget (favorable)")
    else:
        print(f"⚪ {line_item} is within tolerance ({variance_pct:.1%})")

        total = 0
for line_item, budget_amount in budget_by_line.items():
    actual = actuals.get(line_item, 0)
    variance = actual - budget_amount
    total = total + variance

print(f"Total variance: ${total:,.0f}")

# Lesson 7: Functions
def variance_pct(actual, budget):
    """Return the variance as a percentage of budget."""
    if budget == 0:
        return None
    return (actual - budget) / budget


print("\n--- Using our function ---")
print(variance_pct(5_300_000, 5_000_000))
print(variance_pct(1_100_000, 1_200_000))
print(variance_pct(500, 0))

def flag_variance(line_item, actual, budget, threshold=0.05):
    """Return a text flag describing the variance."""
    pct = variance_pct(actual, budget)

    if pct is None:
        return f"⚠️ {line_item}: no budget, can't calculate"
    if pct > threshold:
        return f"🔴 {line_item}: {pct:.1%} over budget"
    if pct < -threshold:
        return f"🟢 {line_item}: {abs(pct):.1%} under budget"
    return f"⚪ {line_item}: within tolerance"


print("\n--- Flags using functions ---")
for item, bud in budget_by_line.items():
    print(flag_variance(item, actuals.get(item, 0), bud))

import pandas as pd
# Lesson 8A: A first taste of pandas
print("\n--- pandas preview ---")
df = pd.DataFrame({
    "line_item": list(budget_by_line.keys()),
    "budget": list(budget_by_line.values()),
})
df["actual"] = df["line_item"].map(actuals).fillna(0)
df["variance"] = df["actual"] - df["budget"]
print(df)

# Lesson 8B: Handling errors
print("\n--- Error handling ---")
try:
    result = 100 / 0
except ZeroDivisionError:
    print("Can't divide by zero. Check the denominator!")

try:
    value = actuals["Travel"]
except KeyError:
    print("'Travel' isn't in the actuals table.")