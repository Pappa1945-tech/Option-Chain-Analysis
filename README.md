# 📈 Option-Chain Analysis

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)](#)
[![Cythonized](https://img.shields.io/badge/Powered%20By-Cython-informational)](https://cython.org/)

A production-grade, real-time web application for analyzing Nifty and BankNifty options, featuring advanced analytics, robust backend logic compiled with Cython, and blazing-fast `.pyd` dynamic libraries.  
**Ideal for Python developers seeking to showcase expertise in high-performance, scalable Python systems.**

---

## 🎬 Demo

[![Watch the demo](https://img.youtube.com/vi/l4e37CqCvUc/0.jpg)](https://youtu.be/l4e37CqCvUc)

---

## 🚀 Project Highlights

**Option-Chain Analysis** is a high-performance analytics tool designed for options traders and technical analysts.  
It leverages Python and Cython to deliver real-time insights, advanced signal processing, and secure, compiled backend logic.

### Key Features

- **Real-Time Data**: Fetches and processes option chain data from NSE every second using multithreading.
- **Cython Optimization**: Core business logic and heavy computations are compiled into `.pyd` (Windows DLL) files using Cython, dramatically improving performance and code security.
- **Support/Resistance Levels**: Identifies critical price points using Open Interest (OI) and volume analytics.
- **Put-Call Ratio (PCR) Analysis**: Calculates multiple PCR metrics to assess market sentiment.
- **Trend Indicators**: Quantifies bullish/bearish trends on a 0–100 scale.
- **Trading Signals**: Generates actionable buy/sell signals for specific strike prices.
- **Interactive Web UI**: Flask + Flask-SocketIO + Jinja2 for dynamic dashboards and real-time updates.
- **Secure Authentication**: Google Drive-based password system.
- **Robustness**: Comprehensive error handling, real-time status updates, and production-ready logging.

---

## 💡 Why Cython & `.pyd` Files?

- **Performance:** Python is powerful, but for heavy, repetitive computations (like option chain analytics) it can be slow. Cython transforms Python modules into C-extensions, compiled as `.pyd` (DLL) files on Windows for near-native execution speed.
- **Code Protection:** Distributing logic as `.pyd` files obfuscates the source, protecting proprietary algorithms.
- **Scalability:** Cythonized modules handle large data streams and concurrent computation efficiently, enabling real-time analytics and multi-user support.
- **Professionalism:** Using Cython and custom `.pyd` modules demonstrates advanced backend and deployment skills—highly attractive for Python developer roles.

**Example:**  
Heavy-lift modules like `all_functions.py` and `glob_var.py` are compiled into `all_functions.cp311-win_amd64.pyd` and `glob_var.cp311-win_amd64.pyd`.  
This boosts performance, reduces latency for analytics, and secures intellectual property.

---

## 🏗️ Project Architecture

```
Option-Chain-Analysis/
├── app.py                  # Flask app entry point
├── all_functions.cp311-win_amd64.pyd  # Cython-compiled core logic
├── glob_var.cp311-win_amd64.pyd       # Cython-compiled globals/state mgmt
├── requirements.txt
├── static/
│   ├── favicon.ico
│   └── js/
│       └── navigation.js
├── templates/
│   ├── banknifty_analysis.html
│   ├── base.html
│   ├── ContactUs.html
│   ├── disclaimer.html
│   ├── nifty_analysis.html
│   ├── signals.html
│   └── strikes.html
└── __pycache__/
```

---

## ⚙️ Technology Stack

- **Backend:** Python 3.11+, Cython, Flask, Flask-SocketIO
- **Data Processing:** Pandas, NumPy, [nsepython](https://pypi.org/project/nsepython/)
- **Frontend:** HTML, Jinja2, JavaScript
- **Deployment:** Local/Cloud (port 5000, cloud-ready)
- **Concurrency:** ThreadPoolExecutor for parallel data fetch & processing

---

## 🔥 How Cython and `.pyd` Integration Works

1. **Develop Python Modules:** Write computational logic in pure Python (e.g., `all_functions.py`).
2. **Compile with Cython:**  
   Convert `.py` to `.pyx` and build with Cython, targeting the current Python version and platform.
3. **Obtain `.pyd` Files:**  
   Compiled `.pyd` files are dynamically loaded by Python, replacing the original `.py` source.
4. **Usage:**  
   Import like a normal Python module, but get C-level performance and source code protection.
5. **Deployment:**  
   Only compiled `.pyd` files are shipped, not the raw `.py` source—ideal for distributing proprietary tools.

**Sample Build Command:**
```bash
cythonize -i -3 all_functions.py
# Produces: all_functions.cp311-win_amd64.pyd
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Pappa1945-tech/Option-Chain-Analysis.git
cd Option-Chain-Analysis
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
# Required: Visual C++ Redistributable for Python .pyd support (Windows)
```
> `requirements.txt` includes: flask, flask-socketio, pandas, numpy, nsepython, requests

### 3. Run the Application

```bash
python app.py
```
Access at: [http://localhost:5000](http://localhost:5000)

---

## ⚡ Quick Usage Guide

- **Home** (`/`): Analyze strike prices interactively.
- **Nifty Analysis** (`/nifty`): Deep-dive into Nifty metrics.
- **BankNifty Analysis** (`/banknifty`): BankNifty analytics.
- **Signals** (`/signals`): Monitor real-time trading signals.
- **Contact** (`/ContactUs`): Support contact.
- **Disclaimer** (`/disclaimer`): Legal info.

---

## 📝 Implementation Workflow

1. **Startup:**
   - `app.py` launches Flask + SocketIO server.
   - Authenticates using Google Drive credentials.
2. **Data Fetching:**
   - Multithreaded fetch of Nifty/BankNifty option chain data (every second).
   - Filters and augments data with computed OI, PCR, volatility, etc.
3. **Analytics:**
   - Cythonized modules process data for support/resistance, PCR, trend, and signal generation.
   - Hybrid averaging (SMA + rolling mean) for noise reduction.
4. **Real-Time Updates:**
   - Background threads emit analytics to frontend in real time via SocketIO.
5. **Frontend:**
   - Jinja2 templates + JS dynamically update UI with latest stats, signals, and visualizations.

---

## 🏆 Why List This on Your Resume?

- **Demonstrates:**  
  - Advanced Python and Cython integration for scalable, high-performance apps
  - Real-time data engineering, analytics, and visualization
  - Secure code deployment using compiled extensions (`.pyd`)
  - End-to-end web app development (Flask, SocketIO, threading)
- **Portfolio Value:**  
  - Showcases both algorithmic expertise and production-ready deployment
  - Strong evidence of backend, full-stack, and optimization skills

---

## 📈 Future Enhancements

- Cloud deployment (AWS/GCP) for public access
- Modern React frontend
- Historical data with PostgreSQL
- Mobile app integration
- Signal backtesting and analytics dashboard
- CI/CD for build and Cython compilation

---

## ⚠️ Legal Disclaimer

Option-Chain Analysis is for educational purposes only and not financial advice. Consult SEBI-registered advisors for trading decisions.  
See `disclaimer.html` for full details.

---

## 📬 Contact

- **Email:** researchonastrology@gmail.com
- **Phone:** +91 9123779929

---

## 🔗 Explore More

If you’re interested in my other live project on astrology and AI,  
please check out 👉 [Talk2Destiny](https://www.talk2destiny.co.in/) 
and also check https://www.producthunt.com/products/destinyai
for advanced research papers, the Luck Meter, and **DestinyAI** tools.


© 2025 SB TECH. All rights reserved.
