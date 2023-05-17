'''
Made by KrakenDev for Web Licensing Protection program.
Acts as a bridge between the manager and the database.
'''

import sqlite3
import uuid
import os

if not os.path.exists('licenses.sqlite'):
    open('licenses.sqlite', 'w').close()
    conn = sqlite3.connect('licenses.sqlite')
    c = conn.cursor()
    c.execute('CREATE TABLE licenses (licenseKey text, active integer, domain text, ipAddress text)')

def addLicense(licenseKey, domain, ipAddress):
    if licenseKey is None or licenseKey == '':
        licenseKey = str(uuid.uuid4())
    conn = sqlite3.connect('licenses.sqlite')
    c = conn.cursor()
    c.execute('INSERT INTO licenses VALUES (?, ?, ?, ?)', (licenseKey, 0, domain, ipAddress))
    conn.commit()
    conn.close()
    return licenseKey

def removeLicense(licenseKey):
    conn = sqlite3.connect('licenses.sqlite')
    c = conn.cursor()
    c.execute('DELETE FROM licenses WHERE licenseKey=?', (licenseKey,))
    conn.commit()
    conn.close()

def activateLicense(licenseKey):
    conn = sqlite3.connect('licenses.sqlite')
    c = conn.cursor()
    c.execute('UPDATE licenses SET active=? WHERE licenseKey=?', (1, licenseKey))
    conn.commit()
    conn.close()

def deactivateLicense(licenseKey):
    conn = sqlite3.connect('licenses.sqlite')
    c = conn.cursor()
    c.execute('UPDATE licenses SET active=? WHERE licenseKey=?', (0, licenseKey))
    conn.commit()
    conn.close()

def getLicense(domain):
    conn = sqlite3.connect('licenses.sqlite')
    c = conn.cursor()
    c.execute('SELECT * FROM licenses WHERE domain=?', (domain,))
    license = c.fetchone()
    if license is None:
        return None
    else:
        return license[0]
    
def getLicenseInfo(licenseKey):
    conn = sqlite3.connect('licenses.sqlite')
    c = conn.cursor()
    c.execute('SELECT * FROM licenses WHERE licenseKey=?', (licenseKey,))
    license = c.fetchone()
    if license is None:
        return None
    else:
        return license



if __name__ == '__main__':
    print('This file is not meant to be run directly.')