Feature: Validate Book Data Table
  As a user
  I want to ensure the data displayed in the Book Table matches the provided data sheet
  So that I can verify the integrity of the displayed data

  Scenario: Verify Book Table data against the provided data sheet
    Given the user is on the Book Table page
    When the user compares the displayed data with the provided data sheet
    Then the data in the Book Table should match the data in the provided data sheet
