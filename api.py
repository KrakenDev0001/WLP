'''
Made by KrakenDev

A program to keep track of active and unpaid licenses to websites
that KrakenDev has made for clients, in order to disable websites
that are in violation of payment agreements.
'''

from flask import Flask, request, jsonify
import sqlite3
import os

if not os.path.exists('licenses.sqlite'):
    open('licenses.sqlite', 'w').close()
    conn = sqlite3.connect('licenses.sqlite')
    c = conn.cursor()
    c.execute('CREATE TABLE licenses (licenseKey text, active integer, domain text, ipAddress text)')

app = Flask(__name__)

@app.route('/api/v1/getPaymentStatus', methods=['GET'])
def getPaymentStatus():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'No data provided.'}), 400
    if 'licenseKey' not in data:
        return jsonify({'error': 'No license key provided.'}), 400
    if 'domain' not in data:
        return jsonify({'error': 'No domain provided.'}), 400
    if 'ip' not in data:
        return jsonify({'error': 'No IP provided.'}), 400
    
    licenseKey = data['licenseKey']
    domain = data['domain']

    conn = sqlite3.connect('licenses.sqlite')
    c = conn.cursor()

    c.execute('SELECT * FROM licenses WHERE licenseKey=?', (licenseKey,))
    license = c.fetchone()
    if license is None:
        return jsonify({'error': 'Invalid license key.'}), 400
    
    c.execute('SELECT * FROM domains WHERE domain=?', (domain,))
    domain = c.fetchone()
    if domain is None:
        return jsonify({'error': 'Invalid domain.'}), 400
    
    ip = request.remote_addr
    
    if license[0] != domain[1] or license[0] != ip[1]:
        return jsonify({'error': 'Invalid license key.'}), 400
    
    if license[2] == 1:
        return jsonify({'status': 'active'}), 200
    else:
        return jsonify({'status': 'inactive'}), 402
    
    conn.close()

@app.route('/api/v1/getLicenseInfo', methods=['GET'])
def getLicenseInfo():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'No data provided.'}), 400
    if 'licenseKey' not in data:
        return jsonify({'error': 'No license key provided.'}), 400
    
    licenseKey = data['licenseKey']

    conn = sqlite3.connect('licenses.sqlite')
    c = conn.cursor()

    c.execute('SELECT * FROM licenses WHERE licenseKey=?', (licenseKey,))
    license = c.fetchone()
    if license is None:
        return jsonify({'error': 'Invalid license key.'}), 400
    
    return jsonify({'licenseKey': license[0], 'active': license[2], 'domain': license[3], 'ipAddress': license[4]}), 200