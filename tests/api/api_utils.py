import allure

def attach_request_response_to_allure(response, request_info=None):
    """
    Attach request and response details to Allure report.
    Args:
        response: requests.Response object
        request_info: Optional string for request details (e.g., payload for POST)
    """
    if request_info:
        allure.attach(
            request_info,
            name="Request",
            attachment_type=allure.attachment_type.TEXT
        )
    else:
        allure.attach(
            str(response.request.url),
            name="Request URL",
            attachment_type=allure.attachment_type.TEXT
        )
    allure.attach(
        str(response.status_code),
        name="Response Status Code",
        attachment_type=allure.attachment_type.TEXT
    )
    allure.attach(
        response.text,
        name="Response Body",
        attachment_type=allure.attachment_type.JSON
    )
