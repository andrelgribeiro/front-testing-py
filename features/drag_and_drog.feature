Feature: Drag and Drop
  Scenario: Mover elemento A para a posição de B
    Given que estou na página "https://the-internet.herokuapp.com/drag_and_drop"
    When eu arrasto o elemento A para a posição do elemento B
    Then os elementos devem trocar de posição
