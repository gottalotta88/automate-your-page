PROGRAM NAME: HTML Generator
AUTHOR: Ravi Gottumukkala

SUMMARY: This program will take make HTML code for notes that were taken over an entire single stage of the nanodegree.

PREFACE:
I prefer taking notes in google docs. Thus my procedure to transferring them is via pasting from a google doc into a text file called "dirtytext.txt”. Following this transfer there are invisible characters that are non-ASCII such as "xe2" which represent quotes. These create errors so I created a function called del_ASCII to remove these characters and replace with normal quotes. The cleaned text is then transfered the into a file called “cleantext.txt”, which this code will read from when creating HTML. I have included the del_ASCII function it in this code as an example but note it is NOT called in this particular module.

My notes taken in google docs for a single stage are split into lessons, concepts, and bulleted details within a concept. I have included a jpeg SCREENSHOT of this format titled google_doc_image in the submitted zip file.

In order to allow me to easily transfer notes from my bulleted google doc format to a raw text format that allows easy HTML generation, I created a simple tagging system that I can quickly add to my raw txt file to indicate the start of a lesson, the start of a concept, and the start of a bulleted list of details. Respectively these are indicated by three tags: L*, C*, B*. My HTML Generator program then recognizes these tags and knows exactly how to parse the text. With the tools we’ve covered thus far, this was the most efficient means of going from google doc notes to HTML notes.

BRIEF NOTES ON GENERAL FUNCTIONALITY:
The program will start by storing the entire “cleantext.txt” file in a string. The code_stage function will then run. This function will utilize all the other functions present to do as follows.

It will first grab lesson 1 of the text and sequentially walk through its concepts. It will grab each concept and split it into a concept title and bulleted details. It will store each bulleted detail into a list which will contain all the bullets under one concept. It will then generate HTML code for this concept based on its title and bulleted details. It will do the same for all concepts within a lesson and then add all this HTML code together, beginning with a title for that lesson.

It will then do the same for each lesson in the stage and ultimately add all of those together to form the HTML code for an entire stage.

