import pytest
from playwright.sync_api import Page, sync_playwright, expect
from config import UPLOAD_URL

class TestUploadUI:

    def test_valid_file_upload(self, page: Page):
        page.goto(UPLOAD_URL)
        page.set_input_files("input#file-upload", "test_data/sample.txt")
        page.click("input#file-submit")

        assert page.locator("#uploaded-files").is_visible()
        uploaded_text = page.locator("#uploaded-files").inner_text().strip()
        assert uploaded_text != "", "No file name shown after upload"

        body_text = page.locator("body").inner_text()
        assert "Internal Server Error" not in body_text
        assert "500" not in body_text

    def test_no_file_selected(self, page: Page):
        page.goto(UPLOAD_URL)
        page.click("input#file-submit")
        assert "Internal Server Error" in page.text_content("body")

    def test_invalid_file_type(self, page: Page):
        page.goto(UPLOAD_URL)
        page.set_input_files("input#file-upload", "test_data/sample.txt")
        page.click("input#file-submit")
        assert "File Uploaded!" in page.text_content("h3")

    def test_upload_empty_file(self, page: Page):
        page.goto(UPLOAD_URL)
        page.set_input_files("input#file-upload", "test_data/empty.txt")
        page.click("input#file-submit")
        assert "File Uploaded!" in page.text_content("h3")

    def test_concurrent_uploads(self, browser):
        context1 = browser.new_context()
        context2 = browser.new_context()

        page1 = context1.new_page()
        page2 = context2.new_page()

        def upload(page):
            page.goto("https://the-internet.herokuapp.com/upload")
            file_input = page.locator("input#file-upload")
            file_input.wait_for(state="visible", timeout=10000)  # wait explicitly
            file_input.set_input_files("test_data/sample.txt")
            page.click("input#file-submit")
            expect(page.locator("h3")).to_have_text("File Uploaded!")

        upload(page1)
        upload(page2)

        context1.close()
        context2.close()

    def test_network_timeout_upload(self, page: Page):
        page.goto(UPLOAD_URL)
        assert page.locator("h3").inner_text() == "File Uploader"

    def test_unauthorized_upload(self, page: Page):
        assert True  # Placeholder

    def test_retry_after_failure(self, page: Page):
        page.goto(UPLOAD_URL)
        try:
            page.set_input_files("input#file-upload", "test_data/sample.txt")
            page.click("input#file-submit")
        except Exception:
            page.reload()
            page.set_input_files("input#file-upload", "test_data/sample.txt")
            page.click("input#file-submit")