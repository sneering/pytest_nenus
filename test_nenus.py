import pytest
from logger import logger
from playwright.sync_api import sync_playwright
from utils import take_screenshot, open_site, login_with_github, launch_workspace, chat_with_agent

# Test GitHub repo link
TEST_REPO = "https://github.com/imrahulr/adversarial_robustness_pytorch.git"
TEST_MSG = "Hello"

@pytest.fixture(scope = "module")
def page():
    with sync_playwright() as p:
        logger.info("Launching browser...")
        browser = p.chromium.launch(headless = False) # Set headless=True to hide the browser (run without UI)
        context = browser.new_context(storage_state="github_state.json") # saved login cookies/tokens 
        page = context.new_page()
        yield page
        browser.close()

def test_full_flow(page):
    # Step 1: Open
    assert open_site(page) is True, "Step 1 failed: open site failed"

    # Step 2: Login via GitHub
    assert login_with_github(page) is True, "Step 2 failed: GitHub login failed"

    # Step 3: Enter repo link and launch workspace
    result, new_tab = launch_workspace(page, TEST_REPO)
    assert result is True, "Step 3 failed: Workspace launch failed"
    assert new_tab is not None, "Step 3 failed: New tab for workspace was not opened"

    # Step 4: Initiate a chat with agent
    assert chat_with_agent(new_tab, TEST_MSG) is True, "Step 4 failed: Chat with agent failed"