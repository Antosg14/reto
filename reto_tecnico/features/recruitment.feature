Feature: Recruitment process automation
  As an admin
  I want to automate recruitment tasks
  So that I can save time and reduce errors

  Scenario: Add a new candidate
    Given I log into the OrangeHRM system
    When I navigate to the Recruitment section
    And I add a candidate with the details:
      | first_name | last_name | email           |
      | John       | Doe       | johndoe@test.com |
    Then I should see the candidate's status as "Hired"
