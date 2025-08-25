# pytest_nenus

This repository contains a python script that performs the following:

1. Check https://nenus.ai availability
2. Logs into the above website via GitHub OAuth
3. Navigates to Workplace on homepage
4. Initiates a chat with the agent

## Features

- Pytest + Playwright + Loguru
- GitHub login automation (except for the first time)
- Repository input and workspace launching
- Agent chat interaction
- Logging and screenshot capture

## Structure

```bash
pytest_nenus/
├── test_nenus.py            # Main test script
├── logger.py                # Logging utility module
├── utils.py                 # Screenshot/helper functions
├── save_github_status.py    # GitHub login session storage (for initial login)
├── requirements.txt         # Project dependencies
├── .gitignore               # Ignore temporary/unwanted files
├── README.md                # Usage instructions
└── screenshots/             # Saved screenshots
```

## How to use

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   playwright install					#install browsers: Chromium、Firefox、WebKit
   ```

2. **Make sure an empty folder named** `screenshots/` **exists**

   This folder is used to store screenshots captured during the automation process.

3. **Run** `save_github_status.py` **once to manually log in to GitHub and save the session**

   ```bash
   python save_github_status.py
   ```

4. **Run `test_nenus.py` to start the script**

   A log file starts with `test_run_{timestamp}.log` will be generated automatically for each test.

   ```bash
   pytest test_nenus.py
   ```
   
   or the following to see the log content in the console.
   
   ```bash
   pytest -s test_nenus.py
   ```

## Sample screenshot

This is a screenshot for step 4: Initiates a chat with the agent

![04_chat_success_sample](https://github.com/sneering/pytest_nenus/blob/main/screenshots/04_chat_success_sample.png)

## Notes

1. **You may need to manually click the “Authorize” button after logging into GitHub**

   During the first login via `save_login_status.py`, GitHub may prompt you to authorize the session. Please complete this step manually to ensure the login state is saved properly.

2. **Workspace usage is limited**

   The workspace allows only one usage per user. Once a run is completed, you may need to manually delete the existing workspace before running the script again.

3. **Only supports Homepage GitHub repo link entry**

   There are multiple ways for users to enter the workspace, but this script only handles the flow where the user accesses it via the GitHub repository link on the homepage.
