#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask

# Instantiate the Flask app
app = Flask(__name__)

@app.route('/') # Home Directory
def hello():
    return "Hello DS C29 learners. Welcome to the class on Deployment-1"

# If you want to run this app, you must call the run()
if __name__=='__main__':
    app.run(debug=True)

