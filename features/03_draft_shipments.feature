Feature: Draft Shipments

  Scenario: registered user can select service and save it as draft
  Given a registered client logged in
  When a service has been selected
  Then he will save the shipment as a draft
  And it will appear in the shipment list


# TODO could be implemented
#  Scenario: registered user can delete sending from drafts
#  Given a registered client
#  When on the shipments page
#  Then he can delete shipment
#  And it will disappear from the list