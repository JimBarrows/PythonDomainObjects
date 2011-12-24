Feature:  Manage goods a business sells
	As a business owner 
	I need to manage the goods my business sells 
	So that I can know when to re-order, track inventory on hand and other inventory management practices. See http://en.wikipedia.org/wiki/Inventory 

Scenario: Create a good

	Given a logged in user
	And a new good called New Good
	When the user saves
	Then the good should be saved in the database
	And on the list of goods.
