import pytest
from module import get_application_status_response  # Adjust this import to your module's name

# Test cases for different statuses
@pytest.mark.parametrize("status, expected_response", [
    ("filled", "Your application has been filled. We will review it soon."),
    ("under review", "Your application is under review."),
    ("verified", "Your application has been verified."),
    ("pending", "Your application is pending. Please wait."),
    ("approved", "Your application has been approved. Congratulations!"),
    ("invalid_status", "Invalid status")
])
def test_get_application_status_response(status, expected_response):
    # Test the function with various status values
    assert get_application_status_response(status) == expected_response
    assert not get_application_status_response(status) == expected_response