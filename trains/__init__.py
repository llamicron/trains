from flask import Flask, render_template

@route('/')
def index():
    return render_template('index.html')

def main():
    return "Here's the entry point"

