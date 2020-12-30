from flask import Flask, render_template

def render_privacypolicy():
    return render_template('logged_out/privacypolicy.html')