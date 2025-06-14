
# 📊 Option‑Chain Analysis

## 🎥 Demo

[![Watch the demo](https://img.youtube.com/vi/l4e37CqCvUc/0.jpg)](https://youtu.be/l4e37CqCvUc)

---
Options Analyzer
A real-time web application for analyzing Nifty and BankNifty options, providing support/resistance levels, Put-Call Ratio (PCR) analysis, trend indicators, and trading signals. Built with Python, Flask, SocketIO, and Pandas, it leverages NSE option chain data to deliver actionable insights for traders.
Project Overview
Options Analyzer is a robust tool for options traders, fetching real-time Nifty and BankNifty option chain data from the National Stock Exchange (NSE) via the nsepython library. It processes this data to compute key metrics and visualizes results through an interactive web interface. Key features include:

Support/Resistance Levels: Identifies critical price points using open interest (OI) and volume.
PCR Analysis: Calculates Put-Call Ratios to assess market sentiment.
Trend Indicators: Quantifies bullish/bearish trends based on PCR and Last Traded Price (LTP).
Trading Signals: Generates real-time buy/sell signals for specific strike prices.
Strike Price Analysis: Provides detailed historical and real-time data for selected strikes.

This project showcases advanced Python and Cython skills, real-time data processing, and web development, making it a strong portfolio piece for a Python developer role.
I convert two python file to .pyd file, which is Windows DLL (Dynamic Link Library) file that contains compiled Python code, created using through Cython (C++ extensions) for Python. It's a way to package compiled Python code for use in Python modules, for performance reasons (because speed matters) 

Features

Real-Time Data: Fetches and processes NSE option chain data every second using multithreading.
Interactive UI: Flask and SocketIO enable dynamic, real-time updates.
Advanced Analytics:
Support/resistance based on OI and volume.
PCR metrics with hybrid averages (simple moving to rolling mean).
Trend strength (0–100 scale) using LTP and PCR.
Signals driven by straddle LTP, implied volatility (IV), and trends.


Robustness: Comprehensive error handling and logging.
Security: Google Drive-based password authentication.
Monitoring: Real-time connection status updates.

Tech Stack

Backend: Python, Cython, Flask, Flask-SocketIO
Data Processing: Pandas, NumPy
Data Source: nsepython for NSE option chain data
Concurrency: ThreadPoolExecutor for parallel tasks
Frontend: HTML, Jinja2
Deployment: Local server (port 5000), cloud-ready
Dependencies: See requirements.txt

Project Structure
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

Workflow

Initialization:

app.py launches Flask and SocketIO.
run_option_chain_fetchers() authenticates via Google Drive.
glob_var.py initializes state variables.


Data Fetching:

fetch_nifty_oc() and fetch_banknifty_oc() retrieve option chain data.
Filters strikes (±20 from ATM) and adds computed columns (e.g., PCR_OI, straddleLtp).


Data Processing:

calculate_pcr_data() computes PCR metrics with hybrid averages.
find_sup_resis() determines support/resistance levels.
give_signals() generates trading signals.
get_strike_price() fetches strike-specific data.


Real-Time Updates:

background_thread() updates data every 5 seconds.
SocketIO emits events for expiry, trends, signals, strikes, support/resistance, and PCR charts.


Frontend:

Templates render static content.
SocketIO updates UI with real-time data.



Dataflow

Input:

NSE option chain data via nsepython.
User-selected strike prices via SocketIO.


Processing:

Stores raw data in nifty_mother_list and banknifty_mother_list.
Computes metrics (PCR, signals, support/resistance) stored in glob_var.
Applies hybrid averages for trend smoothing.


Output:

Emits data to frontend via SocketIO for:
Support/resistance levels
PCR charts
Trend indicators
Trading signals
Strike analytics (LTP, IV, bid/ask)





Installation

Clone the repository:
git clone https://github.com/your-username/options-analyzer.git
cd options-analyzer


Install dependencies:
pip install -r requirements.txt and don't forget to install Visual C++ Redistributable

Note: Create requirements.txt with flask, flask-socketio, pandas, numpy, nsepython, requests.
** Need Visual C++ Redistributable installed to run .pyd files

Run the app:
python app.py


Access at http://localhost:5000.


Usage

Home (/): Analyze strike prices.
Nifty Analysis (/nifty): View Nifty metrics.
BankNifty Analysis (/banknifty): View BankNifty metrics.
Signals (/signals): Monitor trading signals.
Disclaimer (/disclaimer): Legal terms.
Contact (/ContactUs): Support contact.

Future Enhancements

Cloud Deployment: AWS/GCP for public access.
Frontend Upgrade: React for enhanced UI.
Database: PostgreSQL for historical data.
Mobile App: Cross-platform trading app.
Backtesting: Signal performance analysis.

Legal Disclaimer
Options Analyzer is for educational purposes only and not financial advice. Consult SEBI-registered advisors for trading decisions. See disclaimer.html for details.
Contact

Email: researchonastrology@gmail.com
Phone: +91 9123779929

© 2025 SB TECH. All rights reserved.
