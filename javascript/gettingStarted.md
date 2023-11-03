# JS Introduction

## Where to add script element

1. Inside head section

2. Inside body section
    - Best practice is to put it at the end of body section
        - This is because `a.` the browser will load the HTML first, then the script. If the script is at the top, the browser will have to wait for the script to load before it can load the HTML. This will slow down the loading of the page.
        - `b.` Code needs to talk to the element of the webpage. If the script is at the top, the element may not be loaded yet. So the script will not be able to find the element.



