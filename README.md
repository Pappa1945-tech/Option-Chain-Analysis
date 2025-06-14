# 📈 Option-Chain Analysis

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)](#)

Analyze Nifty & BankNifty option chains in real time, with comprehensive analytics, trading signals, and interactive dashboards. Built for traders and Python developers seeking robust, production-grade analytics.

---

## 🎬 Demo

[![Watch the demo](https://img.youtube.com/vi/l4e37CqCvUc/0.jpg)](https://youtu.be/l4e37CqCvUc)

---

## 🚀 Overview

Option-Chain Analysis is a sophisticated web application for real-time options analytics. It fetches Nifty and BankNifty option chain data from NSE, processes it using advanced algorithms, and displays actionable support/resistance, trend, and signal information.

- **Real-Time Analytics:** Multithreaded data fetch and processing.
- **Advanced Signals:** PCR, trend indicators, and buy/sell signals.
- **Built with:** Python, Cython, Flask, SocketIO, Pandas, NumPy.

---

## 🛠 Features

- **Support/Resistance Calculation:** Based on open interest and volume.
- **PCR Analysis:** Put-Call Ratio with hybrid (SMA/rolling mean) metrics.
- **Trend Indicators:** Quantitative trend strength (0–100 scale).
- **Trading Signals:** Real-time buy/sell alerts.
- **Strike Analysis:** Historical and real-time metrics for selected strikes.
- **Security:** Google Drive-based password authentication.
- **Robustness:** Comprehensive error handling, logging, and connection monitoring.

---

## 🏗️ Tech Stack

- **Backend:** Python, Cython, Flask, Flask-SocketIO
- **Data Processing:** Pandas, NumPy, nsepython
- **Frontend:** HTML, Jinja2, JavaScript
- **Deployment:** Local server (port 5000), cloud-ready

---

## 📁 Project Structure

```
├── __pycache__/
├── all_functions.cp311-win_amd64.pyd
├── app.py
├── glob_var.cp311-win_amd64.pyd
├── requirements.txt
├── static/
│   ├── favicon.ico
│   └── js/
│       └── navigation.js
└── templates/
    ├── banknifty_analysis.html
    ├── base.html
    ├── ContactUs.html
    ├── disclaimer.html
    ├── nifty_analysis.html
    ├── signals.html
    └── strikes.html
```

---

## ⚡ Quick Start

```bash
git clone https://github.com/Pappa1945-tech/Option-Chain-Analysis.git
cd Option-Chain-Analysis
pip install -r requirements.txt
# Ensure Visual C++ Redistributable is installed for .pyd files
python app.py
```
Access at [http://localhost:5000](http://localhost:5000)

---

## 🔎 Usage

- `/` — Analyze strike prices.
- `/nifty` — Nifty analytics.
- `/banknifty` — BankNifty analytics.
- `/signals` — Real-time trading signals.
- `/disclaimer` — Legal information.
- `/ContactUs` — Support contact.

---

## 📈 Future Enhancements

- Cloud deployment (AWS/GCP)
- Modern React frontend
- PostgreSQL database for history
- Mobile app
- Backtesting analytics

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or PR.

---

## ⚠️ Legal Disclaimer

Option-Chain Analysis is for educational purposes only and does not constitute financial advice. Please consult a SEBI-registered advisor before making trading decisions.

---

## 📬 Contact

- **Email:** harekrishnajoyradhe@gmail.com
- **Phone:** +91 9123779929

© 2025 SB TECH. All rights reserved.
