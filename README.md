Project Title: 
Failure-Aware Machine Learning Classification on Real-World Banking Data

Project Overiew:
This project builds a failure-aware machine learning system to predict whether a customer will subscribe to a term deposit before initiating a marketing call.
Multiple classical machine learning models are evaluated and compared using principled bias–variance reasoning, with final model selection based on robustness, interpretability, and real-world deployability rather than raw accuracy.

Business Problem:
Telemarketing campaigns are costly, and calling uninterested customers leads to wasted effort.
The objective of this project is to predict customer subscription likelihood before making a call, enabling better targeting and improved campaign efficiency.

Dataset Description:
- Dataset: UCI Bank Marketing Dataset
- Samples: ~41,000
- Target variable: Subscription (`yes` / `no`)
- Feature types:
  - Demographic (age, job, education)
  - Financial (balance, loans)
  - Campaign-related (previous contacts)
  - Macroeconomic indicators
The dataset exhibits strong class imbalance, making accuracy an unreliable evaluation metric.

Data Leakage Analysis:
A critical data leakage issue was identified in the `duration` feature, which represents call duration and is only known after the marketing call.
Since predictions must be made before the call, this feature was removed to ensure realistic and deployable model performance.

Exploratory Data Analysis:
EDA was conducted with a focus on understanding how data properties influence model behavior rather than generating generic plots.
Key findings include:
- Strong correlation among macroeconomic features
- Violation of Naive Bayes independence assumptions
- Presence of class imbalance requiring appropriate metric selection

Models Evaluated:
The following models were implemented and evaluated:

- Naive Bayes  
  - Generative model with strong performance on small and imbalanced data  
  - High recall but lower precision due to independence assumptions  

- Logistic Regression  
  - Discriminative model with probabilistic outputs  
  - Stable under class imbalance and data shifts  
  - Interpretable coefficients and threshold tunability  

- Support Vector Machine (Linear)  
  - Margin-based classifier  
  - Robust to outliers near the decision boundary  
  - Does not natively provide probability estimates  

Evaluation Strategy:
Due to class imbalance, accuracy was avoided as the primary metric.
Model performance was evaluated using:
- Recall (for positive class)
- Precision
- F1-score
- ROC-AUC (primary metric)
ROC-AUC was prioritized as it evaluates ranking quality independent of decision thresholds.

Stress Testing and Model Selection:
Models were stress-tested under multiple real-world conditions, including:
- Reduced training data
- Label noise
- Correlated features
While SVM achieved competitive validation scores, Logistic Regression demonstrated the most stable behavior across all stress scenarios.

Final Model Choice:
Logistic Regression was selected for deployment due to:
- Robust performance under class imbalance
- Probabilistic outputs enabling business-driven threshold tuning
- Interpretability of learned coefficients
- Stability under data shifts and noise

Key Takeaways:
This project demonstrates that effective machine learning is not about choosing the most complex model, but about understanding data assumptions, failure modes, and real-world constraints.
