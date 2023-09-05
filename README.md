# WEB AUTOMATION INSTRUCATIONS


## Steps:

1. Create virtual environment: virtualenv venv (optional)
2. Activate virtual environment: source venv/bin/activate (optional)
3. Cd to main folder to locate the requirement.txt file and execute: pip install --no-cache-dir -r requirements.txt. 
4. Run automation: py.test -v -s tests/ --browser=<browser name> --html=report.html
    *  Example: py.test -v -s tests/ --browser=chrome --html=report.html
5. View report in browser: <report_dir>/report.html


### Driver are not longer required provided in driver folder make sure you are running laestes version of Chrome and Firexox.
### Currently Chrome V116 and FireFox V112

## Browser name choices are:
Chrome, Firefox
