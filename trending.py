# Databricks notebook source
from flask import Flask, jsonify, render_template_string
import os
import time
import uuid
import socket
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# Twitter credentials
TWITTER_USERNAME = "jdager1004"
TWITTER_PASSWORD = "9876@zyxA"

app = Flask(__name__)

@app.route('/')
def home():
    """
    Serve the HTML page.
    """
    return render_template_string(open('python/trending.html').read())

@app.route('/fetch-trends', methods=['GET'])
def get_trends():
    """
    Fetch trends and return the results as JSON.
    """
    trends = fetch_trending_topics()
    if "error" in trends:
        return jsonify(trends)

    # Add unique ID, end time, and IP address
    trends.update({
        "unique_id": str(uuid.uuid4()),
        "end_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ip_address": fetch_ip_address(),
    })
    return jsonify(trends)

if __name__ == '__main__':
    app.run(debug=True)