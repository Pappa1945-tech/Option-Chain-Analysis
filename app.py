from collections import deque
import time
import signal
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
from all_functions import get_strike_price,run_option_chain_fetchers
import glob_var
import threading
import json
import sys
from datetime import datetime
maxlen=1000 
#nifty_exp,banknifty_exp=None,None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='threading', manage_session=False, ping_timeout=60, ping_interval=25)

ret=run_option_chain_fetchers()
nifty_exp,banknifty_exp,tm_nifty,tm_banknifty,nifty_updated,banknifty_updated=ret['nifty_exp'],ret['banknifty_exp'],ret['tm_nifty'],ret['tm_banknifty'],ret['nifty_updated'],ret['banknifty_updated']

@socketio.on('request_expiry')
def send_expiry_info():
    socketio.emit('expiry_update', {
        'nifty_exp': nifty_exp,
        'banknifty_exp': banknifty_exp
    })

@socketio.on('request_nifty_pcr_chart_data')
def handle_pcr_chart_data_request():
    try:
        if hasattr(glob_var, 'nifty_pcrs') and glob_var.nifty_pcrs is not None:
            # Convert the dataframe to a dictionary of lists for easier chart handling
            chart_data = {
                'timestamps': glob_var.nifty_pcrs['tm'].astype(str).tolist(),
                'PCR_OI': glob_var.nifty_pcrs['PCR_OI'].tolist(),
                'avg_PCR_OI': glob_var.nifty_pcrs['avg_PCR_OI'].tolist(),
                'PCR_OICNG': glob_var.nifty_pcrs['PCR_OICNG'].tolist(),
                'avg_PCR_OICNG': glob_var.nifty_pcrs['avg_PCR_OICNG'].tolist(),
                'PCR_OI_UPPER': glob_var.nifty_pcrs['PCR_OI_UPPER'].tolist(),
                'avg_PCR_OI_UPPER': glob_var.nifty_pcrs['avg_PCR_OI_UPPER'].tolist(),
                'PCR_OICNG_UPPER': glob_var.nifty_pcrs['PCR_OICNG_UPPER'].tolist(),
                'avg_PCR_OICNG_UPPER': glob_var.nifty_pcrs['avg_PCR_OICNG_UPPER'].tolist(),
                'PCR_OI_LOWER': glob_var.nifty_pcrs['PCR_OI_LOWER'].tolist(),
                'avg_PCR_OI_LOWER': glob_var.nifty_pcrs['avg_PCR_OI_LOWER'].tolist(),
                'PCR_OICNG_LOWER': glob_var.nifty_pcrs['PCR_OICNG_LOWER'].tolist(),
                'avg_PCR_OICNG_LOWER': glob_var.nifty_pcrs['avg_PCR_OICNG_LOWER'].tolist()
            }
            
            socketio.emit('pcr_chart_data', chart_data)
    except Exception as e:
        print(f"Error in handle_pcr_chart_data_request: {str(e)}")
        socketio.emit('error', {'message': 'Error in handle_pcr_chart_data_request'})

@socketio.on('request_banknifty_pcr_chart_data')
def handle_bankpcr_chart_data_request():
    try:
        if hasattr(glob_var, 'banknifty_pcrs') and glob_var.banknifty_pcrs is not None:
            # Convert the dataframe to a dictionary of lists for easier chart handling
            chart_data = {
                'timestamps': glob_var.banknifty_pcrs['tm'].astype(str).tolist(),
                'PCR_OI': glob_var.banknifty_pcrs['PCR_OI'].tolist(),
                'avg_PCR_OI': glob_var.banknifty_pcrs['avg_PCR_OI'].tolist(),
                'PCR_OICNG': glob_var.banknifty_pcrs['PCR_OICNG'].tolist(),
                'avg_PCR_OICNG': glob_var.banknifty_pcrs['avg_PCR_OICNG'].tolist(),
                'PCR_OI_UPPER': glob_var.banknifty_pcrs['PCR_OI_UPPER'].tolist(),
                'avg_PCR_OI_UPPER': glob_var.banknifty_pcrs['avg_PCR_OI_UPPER'].tolist(),
                'PCR_OICNG_UPPER': glob_var.banknifty_pcrs['PCR_OICNG_UPPER'].tolist(),
                'avg_PCR_OICNG_UPPER': glob_var.banknifty_pcrs['avg_PCR_OICNG_UPPER'].tolist(),
                'PCR_OI_LOWER': glob_var.banknifty_pcrs['PCR_OI_LOWER'].tolist(),
                'avg_PCR_OI_LOWER': glob_var.banknifty_pcrs['avg_PCR_OI_LOWER'].tolist(),
                'PCR_OICNG_LOWER': glob_var.banknifty_pcrs['PCR_OICNG_LOWER'].tolist(),
                'avg_PCR_OICNG_LOWER': glob_var.banknifty_pcrs['avg_PCR_OICNG_LOWER'].tolist()
            }
            
            socketio.emit('pcr_bankchart_data', chart_data)
    except Exception as e:
        print(f"Error in handle_bankpcr_chart_data_request: {str(e)}")
        socketio.emit('error', {'message': 'Error in handle_pcr_chart_data_request'})

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'nifty_connected': hasattr(glob_var, 'nifty_mother_list') and len(glob_var.nifty_mother_list) > 0,
        'banknifty_connected': hasattr(glob_var, 'banknifty_mother_list') and len(glob_var.banknifty_mother_list) > 0,
        'timestamp': time.time()
    })

def shutdown_handler(signum, frame):
    print("Shutting down gracefully...")
    socketio.stop()
    sys.exit(0)

def monitor_connections():
    while True:
        try:
            status = {
                'nifty_connected': hasattr(glob_var, 'nifty_mother_list') and len(glob_var.nifty_mother_list) > 0,
                'banknifty_connected': hasattr(glob_var, 'banknifty_mother_list') and len(glob_var.banknifty_mother_list) > 0,
                'timestamp': time.time()
            }
            socketio.emit('connection_status', status)
            time.sleep(10)
        except Exception as e:
            print(f"Connection monitoring error: {str(e)}")
            time.sleep(10)

signal.signal(signal.SIGINT, shutdown_handler)
signal.signal(signal.SIGTERM, shutdown_handler)

@socketio.on('request_signals_data')
def handle_signals_data_request():
    try:
        if hasattr(glob_var, 'signal_list'):
            # Send the complete signal_list
            socketio.emit('signal_list_update', {
                'signal_list': glob_var.signal_list,
                'is_full_update': True  # Flag to indicate this is a complete refresh
            })
    except Exception as e:
        print(f"Error in handle_signals_data_request: {str(e)}")
        socketio.emit('error', {'message': 'Error in handle_signals_data_request'})

@socketio.on('request_nifty_data')
def handle_nifty_data_request():
    try:
        if hasattr(glob_var, 'nifty_mother_list') and glob_var.nifty_mother_list:
            latest_nifty = glob_var.nifty_mother_list[-1]
            result=glob_var.niftysup_res_result
        
            # Prepare OI data for sending
            oi_data = latest_nifty['oi_data'].to_dict('records')
        
            socketio.emit('nifty_update', {
                'atm_strike': result['atm_strike'],
                'support': result['support'],
                'resistance': result['resistance'],
                'oi_data': oi_data,
                'timestamp': latest_nifty['tm']
            })
    
        
    except Exception as e:
        print(f"Error in handle_nifty_data_request: {str(e)}")
        socketio.emit('error', {'message': 'Error in handle_nifty_data_request'})

@socketio.on('request_banknifty_data')
def handle_banknifty_data_request():
    try:
        if hasattr(glob_var, 'banknifty_mother_list') and glob_var.banknifty_mother_list:
            latest_banknifty = glob_var.banknifty_mother_list[-1]
            result=glob_var.bankniftysup_res_result
        
            # Prepare OI data for sending
            oi_data = latest_banknifty['oi_data'].to_dict('records')
        
            socketio.emit('banknifty_update', {
                'atm_strike': result['atm_strike'],
                'support': result['support'],
                'resistance': result['resistance'],
                'oi_data': oi_data,
                'timestamp': latest_banknifty['tm']
            })
    
        
    except Exception as e:
        print(f"Error in request_banknifty_data: {str(e)}")
        socketio.emit('error', {'message': 'Error in request_banknifty_data'})

# Change the BankNifty trend handler to match Nifty's implementation
@socketio.on('request_banknifty_trend_data')
def handle_banknifty_trend_data_request():
    try:
        socketio.emit('banknifty_trend_update', {
            'trend': glob_var.banknifty_trend,
            'timestamp': time.time(),
            'history': glob_var.banknifty_trend_list
        })
    except Exception as e:
        print(f"Error in handle_banknifty_trend_data_request: {str(e)}")
        socketio.emit('error', {'message': 'Error in handle_banknifty_trend_data_request'})

# Then modify your handle_trend_data_request:
@socketio.on('request_trend_data')
def handle_trend_data_request():
    try:
        socketio.emit('trend_update', {
            'trend': glob_var.nifty_trend,
            'timestamp': time.time(),
            'history': glob_var.nifty_trend_list
        })
    except Exception as e:
        print(f"Error in handle_trend_data_request: {str(e)}")
        socketio.emit('error', {'message': 'Error in handle_trend_data_request'})

def background_thread():
    
    while True:
        try:
            ret=run_option_chain_fetchers()
            
            nifty_exp,banknifty_exp,tm_nifty,tm_banknifty,nifty_updated,banknifty_updated=ret['nifty_exp'],ret['banknifty_exp'],ret['tm_nifty'],ret['tm_banknifty'],ret['nifty_updated'],ret['banknifty_updated']
            dt = datetime.strptime(tm_nifty, '%d-%b-%Y %H:%M:%S')
            tm_nifty = dt.strftime('%H:%M:%S')
            dt = datetime.strptime(tm_banknifty, '%d-%b-%Y %H:%M:%S')
            tm_banknifty = dt.strftime('%H:%M:%S')
            
            nifty_timestamp,banknifty_timestamp=tm_nifty,tm_banknifty
       
            socketio.emit('expiry_update', {
                'nifty_exp': nifty_exp,
                'banknifty_exp': banknifty_exp
            })

            if hasattr(glob_var, 'banknifty_trend') and banknifty_updated:
                socketio.emit('banknifty_trend_update', {
                    'trend': glob_var.banknifty_trend,
                    'timestamp': banknifty_timestamp
                })

            if hasattr(glob_var, 'nifty_trend') and nifty_updated:
                socketio.emit('trend_update', {
                    'trend': glob_var.nifty_trend,
                    'timestamp': nifty_timestamp
                })

            send_signal=False
            if hasattr(glob_var, 'signal_list'):
                if len(glob_var.signal_list)==1:
                    send_signal=True
                elif len(glob_var.signal_list)>1 and glob_var.signal_list[-1]!=glob_var.signal_list[-2]:
                    send_signal=True 

            if send_signal:
                # Emit complete list on each update
                socketio.emit('signal_list_update', {
                    'signal_list': glob_var.signal_list,
                    'is_full_update': True  # Always send full list
                })
            
            # Push strike data updates automatically
            if hasattr(glob_var, 'nifty_mother_list') and glob_var.nifty_mother_list and nifty_updated:
                for strike in glob_var.nifty_strikes:
                    p, atm_strike_print = get_strike_price("Nifty", strike)
                    if not p.empty:
                        p['tm'] = p['tm'].astype(str)
                        socketio.emit('strike_update', {
                            'index': 'Nifty',
                            'strike': strike,
                            'atm': atm_strike_print,
                            'data': p.to_dict('records')[-1]  # Send only the latest data point
                        })
        
            if hasattr(glob_var, 'banknifty_mother_list') and glob_var.banknifty_mother_list and banknifty_updated:
                for strike in glob_var.banknifty_strikes:
                    p, atm_strike_print = get_strike_price("Banknifty", strike)
                    if not p.empty:
                        p['tm'] = p['tm'].astype(str)
                        socketio.emit('strike_update', {
                            'index': 'Banknifty',
                            'strike': strike,
                            'atm': atm_strike_print,
                            'data': p.to_dict('records')[-1]  # Send only the latest data point
                        })
        
            if hasattr(glob_var, 'nifty_mother_list') and glob_var.nifty_mother_list and nifty_updated:
                latest_nifty = glob_var.nifty_mother_list[-1]
                result = glob_var.niftysup_res_result
            
                oi_data = latest_nifty['oi_data'].to_dict('records')
            
                socketio.emit('nifty_update', {
                    'atm_strike': result['atm_strike'],
                    'support': result['support'],
                    'resistance': result['resistance'],
                    'oi_data': oi_data,
                    'timestamp': latest_nifty['tm']
                })

            if hasattr(glob_var, 'banknifty_mother_list') and glob_var.banknifty_mother_list and banknifty_updated:
                latest_banknifty = glob_var.banknifty_mother_list[-1]
                result = glob_var.bankniftysup_res_result
            
                oi_data = latest_banknifty['oi_data'].to_dict('records')
            
                socketio.emit('banknifty_update', {
                    'atm_strike': result['atm_strike'],
                    'support': result['support'],
                    'resistance': result['resistance'],
                    'oi_data': oi_data,
                    'timestamp': latest_banknifty['tm']
                })

            if hasattr(glob_var, 'nifty_pcrs') and glob_var.nifty_pcrs is not None:
            # Convert the dataframe to a dictionary of lists for easier chart handling
                chart_data = {
                    'timestamps': glob_var.nifty_pcrs['tm'].astype(str).tolist(),
                    'PCR_OI': glob_var.nifty_pcrs['PCR_OI'].tolist(),
                    'avg_PCR_OI': glob_var.nifty_pcrs['avg_PCR_OI'].tolist(),
                    'PCR_OICNG': glob_var.nifty_pcrs['PCR_OICNG'].tolist(),
                    'avg_PCR_OICNG': glob_var.nifty_pcrs['avg_PCR_OICNG'].tolist(),
                    'PCR_OI_UPPER': glob_var.nifty_pcrs['PCR_OI_UPPER'].tolist(),
                    'avg_PCR_OI_UPPER': glob_var.nifty_pcrs['avg_PCR_OI_UPPER'].tolist(),
                    'PCR_OICNG_UPPER': glob_var.nifty_pcrs['PCR_OICNG_UPPER'].tolist(),
                    'avg_PCR_OICNG_UPPER': glob_var.nifty_pcrs['avg_PCR_OICNG_UPPER'].tolist(),
                    'PCR_OI_LOWER': glob_var.nifty_pcrs['PCR_OI_LOWER'].tolist(),
                    'avg_PCR_OI_LOWER': glob_var.nifty_pcrs['avg_PCR_OI_LOWER'].tolist(),
                    'PCR_OICNG_LOWER': glob_var.nifty_pcrs['PCR_OICNG_LOWER'].tolist(),
                    'avg_PCR_OICNG_LOWER': glob_var.nifty_pcrs['avg_PCR_OICNG_LOWER'].tolist()
                }
            
                socketio.emit('pcr_chart_data', chart_data)

            if hasattr(glob_var, 'banknifty_pcrs') and glob_var.banknifty_pcrs is not None:
            # Convert the dataframe to a dictionary of lists for easier chart handling
                chart_data = {
                    'timestamps': glob_var.banknifty_pcrs['tm'].astype(str).tolist(),
                    'PCR_OI': glob_var.banknifty_pcrs['PCR_OI'].tolist(),
                    'avg_PCR_OI': glob_var.banknifty_pcrs['avg_PCR_OI'].tolist(),
                    'PCR_OICNG': glob_var.banknifty_pcrs['PCR_OICNG'].tolist(),
                    'avg_PCR_OICNG': glob_var.banknifty_pcrs['avg_PCR_OICNG'].tolist(),
                    'PCR_OI_UPPER': glob_var.banknifty_pcrs['PCR_OI_UPPER'].tolist(),
                    'avg_PCR_OI_UPPER': glob_var.banknifty_pcrs['avg_PCR_OI_UPPER'].tolist(),
                    'PCR_OICNG_UPPER': glob_var.banknifty_pcrs['PCR_OICNG_UPPER'].tolist(),
                    'avg_PCR_OICNG_UPPER': glob_var.banknifty_pcrs['avg_PCR_OICNG_UPPER'].tolist(),
                    'PCR_OI_LOWER': glob_var.banknifty_pcrs['PCR_OI_LOWER'].tolist(),
                    'avg_PCR_OI_LOWER': glob_var.banknifty_pcrs['avg_PCR_OI_LOWER'].tolist(),
                    'PCR_OICNG_LOWER': glob_var.banknifty_pcrs['PCR_OICNG_LOWER'].tolist(),
                    'avg_PCR_OICNG_LOWER': glob_var.banknifty_pcrs['avg_PCR_OICNG_LOWER'].tolist()
                }
            
                socketio.emit('pcr_bankchart_data', chart_data)

        except Exception as e:
            print(f"Error in background_thread: {str(e)}")
            socketio.emit('error', {'message': 'Error in background_thread'})

        time.sleep(5)  # Update every 5 seconds

@app.route('/signals')
def signals_analysis():
    return render_template('signals.html')

@app.route('/disclaimer')
def disclaimer_analysis():
    return render_template('disclaimer.html')

@app.route('/ContactUs')
def ContactUs_analysis():
    return render_template('ContactUs.html')

# Add new route for BankNifty Analysis
@app.route('/banknifty')
def banknifty_analysis():
    return render_template('banknifty_analysis.html',
                         niftyStrikes=glob_var.nifty_strikes,
                         bankniftyStrikes=glob_var.banknifty_strikes,
                         banknifty_exp=banknifty_exp
                         )


@app.route('/nifty')
def nifty_analysis():
    return render_template('nifty_analysis.html',
                         niftyStrikes=glob_var.nifty_strikes,
                         bankniftyStrikes=glob_var.banknifty_strikes,
                         nifty_exp=nifty_exp
                         )

@app.route('/get_strikes')
def get_strikes():
    return jsonify({
        'niftyStrikes': glob_var.nifty_strikes,
        'bankniftyStrikes': glob_var.banknifty_strikes
    })

@app.route('/')
def index():
    return render_template('strikes.html', 
                         niftyStrikes=glob_var.nifty_strikes,
                         bankniftyStrikes=glob_var.banknifty_strikes)

@socketio.on('get_strike_data')
def handle_strike_data(message):
    index = message['index']
    strike = message['strike']
    
    p, atm_strike_print = get_strike_price(index, strike)
    
    if not p.empty:
        p['tm'] = p['tm'].astype(str)
        socketio.emit('strike_data', {
            'index': index,
            'strike': strike,
            'atm': atm_strike_print,
            'data': p.to_dict('records')
        })

if __name__ == '__main__':
    
    threading.Thread(target=background_thread, daemon=True).start()
    threading.Thread(target=monitor_connections, daemon=True).start()
    
    socketio.run(app, debug=False, host='0.0.0.0', port=5000)