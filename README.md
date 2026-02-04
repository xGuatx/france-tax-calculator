# France Tax Calculator

Income tax calculator for the French tax system.

## Description

Calculate French income tax based on household income, tax brackets, and various deductions according to French tax law.

## Prerequisites

- Python 3.7+

## Installation

```bash
# No dependencies required (uses standard library only)
python3 tax_calculator.py
```

## Usage

### Interactive Mode

```bash
python3 tax_calculator.py
```

Follow prompts:
1. Enter annual net income (revenu net imposable)
2. Enter number of tax shares (parts fiscales)
3. View calculated tax amount

### Command Line

```bash
# Single person, 35000EUR income
python3 tax_calculator.py --income 35000 --parts 1

# Married couple, 60000EUR income
python3 tax_calculator.py --income 60000 --parts 2

# Couple with 2 children, 70000EUR income
python3 tax_calculator.py --income 70000 --parts 3
```

## Features

- **2024 Tax Brackets**: Uses current French tax rates
- **Tax Shares (Parts Fiscales)**: Family quotient calculation
- **Detailed Breakdown**: Shows calculation for each bracket
- **Effective Tax Rate**: Displays average tax rate
- **Take-Home Income**: Net income after taxes

## Tax Brackets (2024)

| Income Range | Tax Rate |
|--------------|----------|
| 0 - 10,777EUR | 0% |
| 10,778 - 27,478EUR | 11% |
| 27,479 - 78,570EUR | 30% |
| 78,571 - 168,994EUR | 41% |
| Above 168,994EUR | 45% |

## Tax Shares (Parts Fiscales)

| Family Situation | Tax Shares |
|------------------|------------|
| Single | 1 |
| Married/PACS | 2 |
| Single + 1 child | 1.5 |
| Single + 2 children | 2.5 |
| Married + 1 child | 2.5 |
| Married + 2 children | 3 |
| Each additional child | +0.5 |

## Example Calculations

### Example 1: Single Person

```
Income: 35,000EUR
Tax shares: 1
Quotient familial: 35,000EUR

Calculation:
- 0-10,777EUR @ 0% = 0EUR
- 10,778-27,478EUR @ 11% = 1,837EUR
- 27,479-35,000EUR @ 30% = 2,256EUR

Total tax: 4,093EUR
Effective rate: 11.7%
Net income: 30,907EUR
```

### Example 2: Married with 2 Children

```
Income: 70,000EUR
Tax shares: 3
Quotient familial: 23,333EUR

Calculation:
- 0-10,777EUR @ 0% = 0EUR
- 10,778-23,333EUR @ 11% = 1,381EUR

Subtotal per share: 1,381EUR
Total tax (x 3 shares): 4,143EUR
Effective rate: 5.9%
Net income: 65,857EUR
```

## Configuration

### Update Tax Brackets

Edit `tax_brackets.py`:
```python
TAX_BRACKETS_2024 = [
    (10777, 0.00),
    (27478, 0.11),
    (78570, 0.30),
    (168994, 0.41),
    (float('inf'), 0.45)
]
```

## Advanced Features

### Include Deductions

```bash
# With deductions
python3 tax_calculator.py --income 50000 --parts 2 --deductions 5000
```

Common deductions:
- Pension contributions
- Childcare expenses
- Charitable donations
- Energy renovation work

### Multiple Income Sources

```bash
# Separate earned and capital income
python3 tax_calculator.py \
  --earned-income 40000 \
  --capital-income 5000 \
  --parts 1
```

## Output Formats

### Console Output (Default)

```
=== French Tax Calculator ===
Income: 35,000.00EUR
Tax Shares: 1.0

Calculation:
[Bracket 1] 10,777EUR @ 0% = 0.00EUR
[Bracket 2] 16,701EUR @ 11% = 1,837.11EUR
[Bracket 3] 7,522EUR @ 30% = 2,256.60EUR

Total Tax: 4,093.71EUR
Effective Rate: 11.7%
Net Income: 30,906.29EUR
```

### JSON Output

```bash
python3 tax_calculator.py --income 35000 --parts 1 --format json

{
  "gross_income": 35000,
  "tax_shares": 1,
  "quotient_familial": 35000,
  "total_tax": 4093.71,
  "effective_rate": 0.117,
  "net_income": 30906.29,
  "brackets": [
    {"amount": 10777, "rate": 0, "tax": 0},
    {"amount": 16701, "rate": 0.11, "tax": 1837.11},
    {"amount": 7522, "rate": 0.30, "tax": 2256.60}
  ]
}
```

### CSV Export

```bash
python3 tax_calculator.py --income 35000 --parts 1 --export tax_report.csv
```

## Comparison Tool

```bash
# Compare different scenarios
python3 compare_scenarios.py \
  --scenario1 "Single:35000:1" \
  --scenario2 "Married:70000:2" \
  --scenario3 "Married+2kids:70000:3"
```

## Accuracy

**Disclaimer**:
- Simplified calculation for estimation purposes
- Does not include all tax credits and deductions
- Does not account for:
  - Exceptional income (capital gains, etc.)
  - Specific professional deductions
  - Tax credits (childcare, energy, etc.)
  - Social contributions (CSG, CRDS)

For official tax calculation, use [impots.gouv.fr](https://www.impots.gouv.fr/)

## Testing

```bash
# Run unit tests
python3 -m pytest tests/

# Test with known values
python3 test_calculator.py
```

## Changelog

- **2024**: Updated tax brackets for 2024
- **2023**: Added deductions support
- **2022**: Initial release

## Resources

- [French Tax Administration](https://www.impots.gouv.fr/)
- [Tax Brackets 2024](https://www.service-public.fr/particuliers/vosdroits/F1419)
- [Tax Shares Calculator](https://www.service-public.fr/simulateur/calcul/quotient-familial)

## License

Personal project - Private use

---

**Note**: This is an educational tool. Always verify calculations with official tax authorities.
