# Day 05 — Statistics & Probability

## 1. Population vs Sample

**Population:** The entire group we are interested in.

**Sample:** A smaller subset taken from the population.

Example:
- All students in a university → Population
- 100 selected students → Sample

### Why use samples?
Studying the entire population can be expensive, time-consuming, or impractical.

> Population = Entire group  
> Sample = Subset of the group

---

## 2. Mean, Median & Mode

These are **measures of central tendency**.

### Mean
Mean = Average

Mean = Sum of values / Number of values

```python
import numpy as np

data = [10, 20, 30, 40, 50]
np.mean(data)
```

### Median
Median is the middle value after sorting.

For an even number of values, take the average of the two middle values.

```python
np.median(data)
```

### Mode
Mode = Most frequently occurring value.

```python
from collections import Counter

Counter(data).most_common(1)
```

### Outliers
Mean is sensitive to outliers, while median is more resistant.

> Mean → Sensitive to outliers  
> Median → More resistant  
> Mode → Most frequent value

---

## 3. Variance & Standard Deviation

They measure the **spread of data around the mean**.

Example:

```text
A = [48, 49, 50, 51, 52]
B = [10, 30, 50, 70, 90]
```

Both have mean = 50, but B is more spread out.

> Low SD → Data is clustered around the mean  
> High SD → Data is more spread out

### Variance

Variance measures the average squared distance from the mean.

Population variance:

σ² = Σ(xᵢ - μ)² / N

Squaring prevents positive and negative differences from cancelling.

### Standard Deviation

Standard deviation is the square root of variance.

σ = √σ²

```python
np.var(data)
np.std(data)
```

### ML connection
Standard deviation is important for understanding spread, detecting unusual values, and later for feature standardization/scaling.

---

## 4. Percentiles & Quartiles

### Percentile

A percentile tells us the value below which a certain percentage of observations fall.

Example:

> 90th percentile = 80

Approximately 90% of observations are at or below 80.

### Quartiles

| Quartile | Percentile |
|---|---:|
| Q1 | 25th |
| Q2 | 50th |
| Q3 | 75th |

> Q2 = Median

### IQR — Interquartile Range

IQR represents the spread of the middle 50% of the data.

IQR = Q3 - Q1

Example:

```text
Q1 = 20
Q3 = 60

IQR = 60 - 20 = 40
```

### IQR Outlier Rule

Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR

Values outside these boundaries are considered **potential outliers**.

```python
import numpy as np

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

iqr = q3 - q1
```

### Key idea

```text
Q1 → 25%
Q2 → 50% → Median
Q3 → 75%

IQR = Q3 - Q1
```

---

## Revision Cheat Sheet

```text
Population → Entire group
Sample     → Subset

Mean       → Average
Median     → Middle value
Mode       → Most frequent

Variance   → Average squared spread
SD         → √Variance

Q1         → 25th percentile
Q2         → 50th percentile / Median
Q3         → 75th percentile
IQR        → Q3 - Q1
```


