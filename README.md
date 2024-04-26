# Financial Tracker 
    #### Video Demo:  <URL HERE>
    #### Description: expense tracker


This is my simple expense tracker python application. I track my budget in excel for years now, so I thought it would be a good idea to implement it in python. 

I am using sqlite3 for database handling. The first couple of line is to create the connection to the database. I tried to keep the expense table simple inside of the database, I think there is no need for a relational database, because there are no repetitive information. 

It can be used by prompting from the terminal. There is a two level menu, the base option is to add an item instantly, because this is the most frequent action to take. Every entry consists of a description, cost, category and timestamp of the spending. I implemented this so cost has to be a valid number and category hast to be a valid category.  The categories cannot be changed(yet), these are the categories I use for years in excel. 

Otherwise we end up in the sub menu where we have multiple options. In case of typos, we can check the last three entry and delete the items if we want to. Or it is possible to make querys for different time periods. I defined these periods that I am interested usually. 

Since it was my very first project there are plenty of ways of improving it. One of them is building a better structure of the main function, it could be better organized by putting some of the logic outside of main. Also I am thinking about creating a budget tracker as a new class so it would be more succint and stable. 

Finally adding a user interface would make this application very usable.
