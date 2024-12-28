from pytest_bdd import given, when, then
from screenplay.actions.login import login
from screenplay.actions.add_candidate import add_candidate
from screenplay.questions.validate_status import validate_status

@given("I log into the OrangeHRM system")
def log_in(actor):
    login(actor, "Admin", "admin123")

@when("I navigate to the Recruitment section")
def navigate_to_recruitment(actor):
    actor.browser.find_element_by_xpath("//span[text()='Recruitment']").click()

@when("I add a candidate with the details:")
def add_candidate_step(actor, data_table):
    for row in data_table:
        add_candidate(actor, row["first_name"], row["last_name"], row["email"])

@then("I should see the candidate's status as 'Hired'")
def validate_hired_status(actor):
    assert validate_status(actor), "The status is not 'Hired'"
