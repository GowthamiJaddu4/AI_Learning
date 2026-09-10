# Day 5 — Probability Notes

## 1. Probability Basics
Probability measures how likely an event is.

0 <= P(A) <= 1

- 0 → impossible
- 1 → certain
- 0.5 → 50% chance

**Experiment:** Process whose outcome we observe (coin toss, die roll).

**Outcome:** One possible result.

**Sample Space:** Set of all possible outcomes.
- Coin: {H, T}
- Die: {1, 2, 3, 4, 5, 6}

**Event:** Outcome or collection of outcomes we care about.

For equally likely outcomes:

P(A) = Favorable outcomes / Total possible outcomes

Example:
P(4 on a die) = 1/6
P(even) = 3/6 = 1/2

---

## 2. Probability Rules

### Complement
P(not A) = 1 - P(A)

### OR — Addition
For mutually exclusive events:

P(A OR B) = P(A) + P(B)

General rule:

P(A OR B) = P(A) + P(B) - P(A AND B)

The subtraction prevents double-counting overlap.

### AND — Multiplication
For independent events:

P(A AND B) = P(A) × P(B)

For dependent events:

P(A AND B) = P(A) × P(B|A)

---

## 3. Conditional Probability

Conditional probability means the probability of A **given that B has already happened**.

Notation:

P(A|B)

Formula:

P(A|B) = P(A AND B) / P(B)

**Intuition:** Known information changes the sample space.

Example:
A card is known to be red. Probability it is a Heart:

P(Heart|Red) = 13/26 = 1/2

Important:

P(A|B) is NOT the same as P(B|A).

---

## 4. Independent vs Dependent Events

### Independent
One event does not affect the other.

Example: Two coin tosses.

P(H AND T) = 1/2 × 1/2 = 1/4

### Dependent
The first event affects the probability of the second.

Example: Drawing two cards without replacement.

**Memory trick:**
- Independent → probability stays the same
- Dependent → probability changes

---

## 5. Bayes' Theorem

Bayes' Theorem helps find a reverse conditional probability.

P(A|B) = [P(B|A) × P(A)] / P(B)

It combines:
- **Prior** → belief before evidence
- **Likelihood** → how likely the evidence is
- **Posterior** → updated belief after evidence

### Example
Suppose:
- P(Disease) = 1%
- P(Positive|Disease) = 90%
- P(Positive|No Disease) = 5%

First:

P(Positive) = 0.90(0.01) + 0.05(0.99)
             = 0.0585

Then:

P(Disease|Positive)
= [0.90 × 0.01] / 0.0585
≈ 0.154
≈ 15.4%

Important:

P(Disease|Positive) ≠ P(Positive|Disease)

---

## 6. Probability Distributions

A probability distribution describes possible values of a random variable and their probabilities.

### Discrete
Countable values.
- Number of heads
- Die result
- Number of customers

### Continuous
Values within a range.
- Height
- Weight
- Temperature
- Time

Common distributions:
- Bernoulli
- Binomial
- Poisson
- Normal

---

## 7. Normal Distribution

A normal distribution is:
- Bell-shaped
- Symmetric
- Centered around the mean

For a perfectly normal distribution:

Mean = Median = Mode

Standard deviation controls spread:
- Small SD → data is concentrated
- Large SD → data is spread out

### 68–95–99.7 Rule
- 68% → within 1 SD
- 95% → within 2 SD
- 99.7% → within 3 SD

Example:
Mean = 100, SD = 15

Approximately 68% lies between:

85 and 115

---

## 8. Central Limit Theorem (CLT)

If we repeatedly take sufficiently large random samples and calculate the mean of each sample, the distribution of those sample means tends to become approximately normal.

### Important distinction

**Normal Distribution:** Original data/population is bell-shaped.

**CLT:** Distribution of many **sample means** becomes approximately bell-shaped.

Steps:
1. Take many random samples.
2. Calculate each sample's mean.
3. Collect the sample means.
4. Their distribution tends toward normal.

---

## 9. Sampling & Statistical Inference

**Population:** Entire group.

**Sample:** Smaller group selected from the population.

**Parameter:** Numerical value describing the population.
Example: population mean = μ

**Statistic:** Numerical value calculated from a sample.
Example: sample mean = x̄

**Statistical inference:** Use a sample to make conclusions or estimates about a population.

Example:
Take 100 students from 1,000 students and use their average marks to estimate the college's average.

---

## 10. Hypothesis Testing

Hypothesis testing determines whether an observed result provides enough evidence against a default claim.

### Null Hypothesis — H₀
Default/claimed situation.

If college claims average score is 60:

H₀: μ = 60

### Alternative Hypothesis — Hₐ
What we want to test against H₀.

If we ask whether the average is different from 60:

Hₐ: μ ≠ 60

Other possibilities:
- Greater than 60 → Hₐ: μ > 60
- Less than 60 → Hₐ: μ < 60

---

## 11. P-Value

The p-value tells us how surprising the observed result would be if H₀ were true.

Common significance level:

α = 0.05

Decision:
- p < 0.05 → Reject H₀
- p >= 0.05 → Fail to reject H₀

Example:
p = 0.02 → Reject H₀

**Important:** p-value is NOT the probability that H₀ is true.

---

## 12. Confidence Intervals

A confidence interval gives a range of plausible values for a population parameter based on sample data.

Example:
Sample mean = 170
95% CI = [168, 172]

Classical interpretation:
If we repeatedly take samples and construct 95% confidence intervals using the same method, about 95% of those intervals would contain the true population parameter.

For a typical two-sided 5% test:
- Null value outside 95% CI → reject H₀
- Null value inside 95% CI → fail to reject H₀

---

## 13. Correlation & Covariance

### Covariance
Shows the direction in which two variables tend to move together.

- Positive → both tend to increase together
- Negative → one tends to increase while the other decreases
- Near zero → no clear linear co-movement

Covariance has units and no fixed range.

### Correlation
Standardized measure of linear relationship.

-1 <= r <= 1

- +1 → perfect positive
- +0.8 → strong positive
- 0 → no linear relationship
- -0.8 → strong negative
- -1 → perfect negative

**Important:** Correlation does not imply causation.

---

## 14. Probability & Statistics in Machine Learning

### Statistics helps ML to:
- Understand data
- Measure central tendency
- Understand spread
- Detect outliers
- Understand distributions
- Analyze relationships
- Quantify uncertainty

### Probability helps ML to:
- Represent uncertainty
- Calculate likelihoods
- Predict probabilities
- Model random events
- Make decisions under uncertainty

Example classifier:

Spam → 0.90
Not Spam → 0.10

The model predicts a 90% probability for Spam.

### ML Connections
- Bayes → Naive Bayes
- Probability distributions → Statistical modeling
- Conditional probability → Classification/probabilistic reasoning
- Correlation → Feature analysis/multicollinearity
- Hypothesis testing → Testing whether effects/differences are meaningful
- Confidence intervals → Quantifying uncertainty

---

# Quick Revision Cheat Sheet

| Concept | Remember |
|---|---|
| Probability | How likely an event is |
| Sample Space | All possible outcomes |
| Event | Outcome(s) we care about |
| Complement | 1 - P(A) |
| OR | Add, accounting for overlap |
| AND | Multiply |
| Conditional | P(A|B) = A given B |
| Independent | One event doesn't affect another |
| Dependent | One event affects another |
| Bayes | Reverse/update conditional probability |
| Distribution | Values + probabilities |
| Normal | Bell-shaped and symmetric |
| CLT | Distribution of sample means tends to normal |
| Population | Entire group |
| Sample | Subset of population |
| Inference | Sample → Population |
| H₀ | Default/claimed situation |
| Hₐ | Alternative claim |
| p-value | Surprise under H₀ |
| CI | Plausible range for population parameter |
| Covariance | Direction of joint movement |
| Correlation | Standardized linear relationship |

# Most Important Formulas

P(A) = Favorable outcomes / Total outcomes

P(not A) = 1 - P(A)

P(A OR B) = P(A) + P(B) - P(A AND B)

P(A AND B) = P(A)P(B|A)

P(A|B) = P(A AND B) / P(B)

P(A|B) = [P(B|A)P(A)] / P(B)

-1 <= r <= 1

# Probability → ML

Probability
↓
Conditional Probability
↓
Bayes' Theorem
↓
Probability Distributions
↓
Statistical Inference
↓
Machine Learning
├── Naive Bayes
├── Classification Probabilities
├── Uncertainty
├── Statistical Testing
└── Probabilistic Models
