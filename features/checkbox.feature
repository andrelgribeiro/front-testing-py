Feature: Checkbox
  Scenario: Selecionar e desmarcar checkbox
    Given que estou na página "https://the-internet.herokuapp.com/checkboxes"
    When eu marco o primeiro checkbox
    Then o primeiro checkbox deve estar marcado
    When eu desmarco o primeiro checkbox
    Then o primeiro checkbox deve estar desmarcado
