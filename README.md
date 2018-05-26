# yyEnglish
###### Help you track and improve your finacial situation

## Features

### SignIn/ SignOut
- Google Account


### Home
Since `Home` screen is very complicated, we break it down into multiple functionality groups


###### Account Management (top left)
- Creating multiple personal/group account
    - The difference between Personal account and Group account is that in group account you are able to invite others and manage expense/income together
- Editing account name (support emoji)
- Inviting members for group account
    - Non-creator members don't have edit/invite permission in group account 


###### Yearly Summary Calendar (top middle)
The yearly summary for your expense/income of currently selected account. In the summary you'll see following items for each month:

- number of transaction
- total expense and income

By tapping the month in the calendar, it refreshes the data in `Home` screen.


###### Total Month Expense/Income (top right)
The total expense and income for currently selected account and month. By tapping it you can switch between showing expense data and income data in `Home` screen.


###### Month Summary Chart (middle up)
A pie chart that break down your expense/income into different categories. It's easily for you to find out expense/income percentage and amount for each category. By tapping each category in the pie chart, you can filter the transaction list by selected category.


###### Transaction List (middle bottom)
A list that shows expense/income details and it can be filtered by selecting the categories in pie chart.


###### Creating Transaction (bottom middle)
Create your transaction (expense/income) with amount, notes, date time and category. You are also able to manage (add, edit) your own categories at here. Category name also supports emjo.

###### Scan Receipt (in creating transaction view)
Scan receipt to automatically extract information and fillout the form when creating transactions. Currently only support extracting total expense amount and purchase date. So far, the issues for scanning receipt are: 1) too slow 2) accuracy still need to be improved.
