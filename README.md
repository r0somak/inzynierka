<h1>Installation guide</h1>
<ol>
    <li>Make sure you have <code>pip</code>, <code>python 3.7</code> and <code>npm</code> with <code>@vue/cli</code> installed in your system</li>
    <li>Clone repository</li>
    <li>Cd to project directory</li>
    <li>Create python virtual enviroment with <code>$ virtualenv venv</code></li>
    <li>Run <code>$ source ./venv/bin/activate</code> to activate virtual enviroment</li>
    <li>Run <code>$ which python</code> to ensure that you are using python in virtualenv</li>
    <li>Run <code>$ pip install -r requirements.txt</code> to install necessary python dependencies</li>
    <li>Execute <code>$ ./manage.py runserver</code> to start Django server</li>
    <li>Cd to <code>frontend</code> dir</li>
    <li>Run <code>$ npm install</code> to install Vue dependencies</li>
    <li>Execute <code>$ npm run serve</code> to start Vue dev server</li>
    <li>Go to <code>http://localhost:8000/</code> to browse API endpoints (Django with DRF)</li>
    <li>Go to <code>http://localhost:8080/</code> to use app (Vue.js)</li>
</ol>