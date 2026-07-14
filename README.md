# 🍷 Wine Quality Predictor

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Flask Version](https://img.shields.io/badge/flask-3.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern, high-performance, asynchronous web application designed to predict wine quality profiles using machine learning. The system decouples the predictive analytics layer (Python Flask) from an optimized, responsive user experience (Tailwind CSS, native JavaScript Fetch API).

---

## 🏗️ Architecture & Implementation Highlights

* **Global Model Caching:** The serialized `DecisionTreeClassifier` model (`model.pkl`) is instantiated once into the global application memory stack at server boot time. This bypasses disk-I/O constraints, reducing route latency from $\mathcal{O}(N)$ file-reads to an $\mathcal{O}(1)$ in-memory operation per request.
* **Asynchronous JSON Payload Pattern:** Departed from legacy multipart form submissions to utilize structured, modern JSON transactions via async/await fetch operations.
* **Defensive API Design:** Implemented thorough type-casting validation blocks inside the request pipeline to gracefully intercept corrupted payloads or mismatched schema inputs prior to model evaluation.
* **Fully Responsive Grid Layout:** Implemented a component-driven mobile-first UI using Tailwind CSS, featuring optimized input element focus states (`focus:ring-2`), conditional layout constraints, and deterministic error handling.

---

## 📂 Project Structure

```text
wine-quality-predictor/
├── templates/
│   └── index.html       # Single Page Application (SPA) view layer
├── app.py               # Optimized Flask application controller code
├── model.pkl            # Serialized Scikit-Learn model binary
├── requirements.txt     # Locked production environment dependencies
└── README.md            # Comprehensive system documentation
