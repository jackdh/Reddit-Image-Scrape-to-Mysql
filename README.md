Reddit-Image-Scrape
===================

A reddit image scraper to mysql.

A app I created for my web game, so you think you know reddit. This app will scrape the given subreddits for subbreddit, title, image_url, post_url. Although these can be easily edit to collect which ever information is needed.

How to use.

1) Create a Mysql database,
2) Add the required config for the database at the top.
3) Choose your subbreddits!
4) Firstly run the tableCreate() function.
5) Run the main program!


How to edit (noob friendly) to select more / less information.

Line 21 - Add more coloumns for the information
line 40/41/43 - Add the new columns and increase / decrease the %s for each item.
Line 64/65/66 - Here you can choose which information you wish to collect, it needs to match up with the new columns, 
Line 76 - Make sure you pass the new variables which contain the data.

How to increase the amount of images collected from each subreddit. Or change sample size?

These options can be set just under neath the config.

How do I select images from more unique subreddit data?

You can read on how to get the correct JSON url here.

http://www.reddit.com/dev/api#section_listings

Can I take / use this for whoever/whatever?

Yes! It's opensource do as you wish!

