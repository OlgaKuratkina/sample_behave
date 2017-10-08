Feature: Draft Shipments

  Scenario: registered user can select service and save it as draft
  Given a registered client
  When a service has been selected
  Then he will save the shipment as a draft
  And it will appear in the shipment list