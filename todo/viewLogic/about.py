from flask import Flask, render_template, request

def render_about():
    return render_template('logged_out/about.html')
