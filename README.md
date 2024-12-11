# Final Project - AIDI 1003
# Recommendation System for E-commerce

This project provides a Flask-based REST API to deploy a machine learning model for making predictions in an e-commerce recommendation system. The API accepts input features in JSON format and returns the model's prediction. The project demonstrates a complete pipeline for deploying a trained Random Forest model.

---

## Team Members
- **TejasKumar Patel**
- **Chintan Chauhan**
- **Nirmoh Nagwadia**
- **Girik Nohani**

---

## Features

- **Endpoints**:
  - `GET /`: Returns a welcome message and API usage instructions.
  - `POST /predict`: Accepts input features and returns the model's prediction.
- **Input Format**:
  - JSON with a key `"features"` containing an array of numerical values.
- **Output Format**:
  - JSON with a key `"prediction"` containing the predicted value(s).
- **Model**:
  - A trained Random Forest model serialized using `joblib`.

---

## Setup Instructions

### Prerequisites

1. Python 3.7 or higher
2. Required Python libraries:
   - Flask
   - NumPy
   - joblib
   - scikit-learn (for training and compatibility)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/recommendation-system-ecommerce.git
   cd recommendation-system-ecommerce
