import os
import time
from datetime import datetime
from playwright.sync_api import Page
from logger import logger


# Take screenshot for each step
def take_screenshot(page: Page, step_name: str):
    try:
        # time.sleep(3)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)
        path = f"{folder}/{timestamp}_{step_name}.png"
        page.screenshot(path=path)
        logger.info(f"Screenshot saved: {path}")
        return True
    except Exception as e:
        logger.error(f"Screenshot failed for {step_name}: {e}")
        return False

# Check website availability and open
def open_site(page: Page):
    try:
        response = page.goto("https://nenus.ai", timeout=15000, wait_until="load")
        if response and response.status == 200:
            take_screenshot(page, "01_homepage_success")
            return True
        else:
            logger.error("Failed to get response")  
            take_screenshot(page, "901_homepage_site_status_error")
            return False
      
    except Exception as e:
        logger.error(f"Step 1 (Open): FAILED - {e}")
        take_screenshot(page, "901_homepage_error")
        return False

# Log in with GitHub
def login_with_github(page: Page):
    try:
        logger.info("Logging in via GitHub...")

        page.goto("https://nenus.ai")
        # Click main login button
        time.sleep(3) # Wait for the page to be fully loaded
        page.wait_for_selector("text=Login")
        page.click("text=Login")
        logger.info("Clicked main Login button")

        # Click github login button
        page.wait_for_selector("text=Log In With Github")
        page.click("text=Log In with GitHub")
        logger.info("Clicked GitHub Login button")

        take_screenshot(page, "02_logged_in_success")
        return True
    
    except Exception as e:
        logger.error(f"GitHub login failed: {e}")
        take_screenshot(page, "902_login_error")
        return False

# Launch workspace
def launch_workspace(page: Page, repo_url: str):
    try:
        logger.info(f"Launching workspace with repo:{repo_url}")
        time.sleep(1)
        
        # Repo input find, fill, launch
        repo_input = page.wait_for_selector("input[placeholder='Enter a GitHub repository URL to launch']")
        repo_input.fill(repo_url)
        # logger.info("Filled GitHub repo link")
        with page.expect_popup() as popup_page:
            page.get_by_role("button", name="Launch").click()
        logger.info("Clicked Launch button")
        # handle new page
        new_page = popup_page.value
        new_page.wait_for_load_state()

        take_screenshot(page, "03_workspace_success")
        return True, new_page
    
    except Exception as e:
        logger.error(f"Workspace launch failed: {e}")
        take_screenshot(page, "903_workspace_launch_error")
        return False, None  

# Initiate a chat with agent
def chat_with_agent(page: Page, message: str):
    try:
        # page.wait_for_load_state('networkidle')
        logger.info("Sending message to agent...")
        
        # Wait for the system to be ready
        time.sleep(60)
        input = page.wait_for_selector('[data-testid="chat-input"] textarea')
        # input = page.wait_for_selector("textarea[placeholder='What do you want to build?']", timeout=80000)
        input.fill(message)
        page.locator('button[aria-label="Send"]').click()

        time.sleep(5)
        take_screenshot(page, "04_chat_success")
        return True
    
    except Exception as e:
        logger.error(f"Chat with agent failed: {e}")
        take_screenshot(page, "904_chat_error")
    return False