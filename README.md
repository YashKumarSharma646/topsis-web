##  Methodology, Results, and Analysis

###  Methodology (TOPSIS Workflow)

The web application implements the standard **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** methodology to rank alternatives based on multiple criteria. The complete workflow is executed using a custom-developed PyPI package and is described below:

1. **Input Data Collection**
   - The user uploads a CSV file through the web interface.
   - The **first column** represents the alternatives.
   - The remaining columns contain **numeric criteria values**.

2. **Weight and Impact Definition**
   - The user provides:
     - **Weights** representing the importance of each criterion.
     - **Impacts** where `+` denotes a beneficial criterion and `-` denotes a non-beneficial criterion.

3. **Normalization of Decision Matrix**
   - Criteria values are normalized using vector normalization to eliminate the effect of differing units and scales.

4. **Weighted Normalized Matrix**
   - Each normalized value is multiplied by its corresponding weight to incorporate relative importance.

5. **Ideal Best and Ideal Worst Solutions**
   - **Ideal Best Solution:** Best values for each criterion based on impacts.
   - **Ideal Worst Solution:** Worst values for each criterion based on impacts.

6. **Distance Calculation**
   - Euclidean distances of each alternative are calculated from:
     - Ideal Best solution
     - Ideal Worst solution

7. **TOPSIS Score Calculation**
   - The relative closeness of each alternative to the ideal solution is computed as:
     ```
     TOPSIS Score = Distance from Ideal Worst /
                    (Distance from Ideal Best + Distance from Ideal Worst)
     ```

8. **Ranking of Alternatives**
   - Alternatives are ranked in descending order of TOPSIS scores.
   - A higher score indicates a more preferred alternative.

All computations are performed using a **custom-built PyPI package**, ensuring modularity, correctness, and reusability.

---

###  Result Table Explanation

After computation, the application generates an output CSV file with the following structure:

| Column Name | Description |
|------------|-------------|
| Alternative | Name of the alternative |
| Criteria Columns | Original numeric criteria values |
| TOPSIS Score | Relative closeness to the ideal solution |
| Rank | Final ranking based on TOPSIS score |

**Interpretation:**
- Alternatives with **higher TOPSIS scores** are closer to the ideal best solution.
- **Rank 1** represents the most optimal alternative based on the provided criteria, weights, and impacts.
- The tabular output ensures **transparent and reproducible** decision-making.

---

###  Sample Input and Output Files

#### Sample Input File
A sample input file used for testing the application is provided below:

- **Input CSV:**  
  [`uploads/data.csv`](uploads/data.csv)

This file contains alternatives and their corresponding criteria values in numeric format.

---

#### Sample Output File
The corresponding output file generated after applying the TOPSIS algorithm is:

- **Output CSV:**  
  [`outputs/result.csv`](outputs/result.csv)

This file includes the computed **TOPSIS Score** and **Rank** for each alternative.

---

###  Final Outcome

The TOPSIS web application successfully:
- Accepts real-world decision data in CSV format
- Applies the TOPSIS algorithm using a custom Python package
- Produces a clear and interpretable result table
- Ensures reproducibility through file-based input and output
- Demonstrates an end-to-end deployed decision-support system

This project effectively combines **theoretical rigor**, **software modularity**, and **practical deployment**.

- Produces transparent and reproducible rankings
- Combines algorithmic rigor with practical usability
- Demonstrates real-world deployment using a custom Python package

This approach ensures both **theoretical correctness** and **practical applicability**.

### Website Link
The Topsis Live website is available here:  
[Topsis Live Website](https://topsis-web-jhxp.onrender.com)

## Part II: PyPI Package

The **TOPSIS-Yash-102303701** package is published on **PyPI**, making it easy to install and use in any Python project.

---

###  Package Information

- **Package Name:** `TOPSIS-Yash-102303701`
- **Version:** `0.4`
- **PyPI Link:** https://pypi.org/project/TOPSIS-Yash-102303701/

---

###  Installation

Install the package using `pip`:

```bash
pip install TOPSIS-Yash-102303701
Usage as Command Line Tool
After installation, use the topsis command from the terminal:

topsis input.csv "1,1,1,1" "+,+,-,+" output.csv
Arguments:

input.csv → Input dataset

"1,1,1,1" → Weights for criteria

"+,+,-,+" → Impacts (+ = benefit, - = cost)

output.csv → Output file with TOPSIS scores & ranks

Usage as Python Module
You can also use the package directly in Python:

from topsis import topsis

topsis(
    input_file="input.csv",
    weights=[1, 1, 1, 1],
    impacts=["+", "+", "-", "+"],
    output_file="output.csv"
)
