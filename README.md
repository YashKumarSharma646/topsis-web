## 📊 Methodology, Results, and Analysis

### 🔹 Methodology (TOPSIS Workflow)

The web application follows the standard **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** methodology to rank alternatives based on multiple criteria. The complete workflow is as follows:

1. **Input Data Collection**
   - The user uploads a CSV file containing alternatives and criteria values.
   - The first column represents the alternatives (e.g., funds, options).
   - Remaining columns represent numerical criteria values.

2. **Weight and Impact Definition**
   - The user provides:
     - Weights for each criterion (importance level).
     - Impacts (`+` for benefit criteria, `-` for cost criteria).

3. **Normalization of Decision Matrix**
   - Each criterion value is normalized using vector normalization to remove scale differences between criteria.

4. **Weighted Normalized Matrix**
   - Normalized values are multiplied by their corresponding weights to reflect relative importance.

5. **Ideal Best and Ideal Worst Solutions**
   - Ideal Best: Best value for each criterion based on its impact.
   - Ideal Worst: Worst value for each criterion based on its impact.

6. **Distance Calculation**
   - Euclidean distance of each alternative from:
     - Ideal Best solution
     - Ideal Worst solution

7. **TOPSIS Score Calculation**
   - The relative closeness to the ideal solution is computed for each alternative:
     ```
     TOPSIS Score = Distance from Ideal Worst / (Distance from Ideal Best + Distance from Ideal Worst)
     ```

8. **Ranking**
   - Alternatives are ranked in descending order of TOPSIS scores.
   - Higher score indicates a better alternative.

This entire computation is performed using a **custom-built PyPI package**, ensuring modularity and reusability.

---

### 🔹 Result Table Explanation

After computation, the output file includes the following columns:

| Column Name | Description |
|------------|-------------|
| Alternative | Name of the option/fund |
| Criteria Columns | Original numeric criteria values |
| TOPSIS Score | Relative closeness to ideal solution |
| Rank | Final rank based on TOPSIS score |

**Interpretation:**
- A higher TOPSIS score means the alternative is closer to the ideal best solution.
- Rank `1` indicates the most preferred alternative based on given criteria, weights, and impacts.

---

### 🔹 Result Graph Interpretation

A graphical analysis can be derived from the result table by plotting:

- **X-axis:** Alternatives
- **Y-axis:** TOPSIS Scores

**Graph Insights:**
- Taller bars (or higher points) represent better-performing alternatives.
- The graph visually highlights:
  - Performance gaps between alternatives
  - Dominant and weak options
- It helps decision-makers quickly compare and justify rankings.

Such visualization enhances interpretability and supports data-driven decision-making.

---

### 🔹 Final Outcome

The TOPSIS web application successfully:
- Automates multi-criteria decision-making
- Produces transparent and reproducible rankings
- Combines algorithmic rigor with practical usability
- Demonstrates real-world deployment using a custom Python package

This approach ensures both **theoretical correctness** and **practical applicability**.
