# Allowance Handler

Script for automatically adding the kid's allownance to a pre-formatted Google sheet each week.
* The kid's get allowance once a week, every Friday
* They receive an amount equivalent to their current age, 1 year = $1.
* One row for each child will be added to the "Transactions" sheet for each allowance insert

Requires:
* `credentials.json` file with Google Sheets API credentials
* `birthdays.json` file with each child's birthday

