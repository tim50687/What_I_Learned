# Scrapy 

An open source and collaborative framework for extracting the data you need from websites. In a fast, simple, yet extensible way.

## Why use Scrapy?

* Built-in support for **extracting data from HTML/XML sources** using extended [CSS](http://www.w3.org/TR/CSS2/selector.html) [selectors](http://www.w3.org/TR/CSS2/selector.html) and [XPath](http://www.w3.org/TR/xpath/) expressions, with helper methods to extract using regular expressions.

* Built-in support for **extracting data from JSON sources** using XPath expressions.

* automatic retrying of failed requests, **HTTP compression**, **HTTP authentication** and **cookies**.


### What is CSS selector?

CSS selectors are patterns used to select the element(s) you want to style. 

## Create a virtual environment

```bash
python3 -m venv venv
```


The command `python -m venv venv` is used to create a Python virtual environment named "venv" in the current directory. 

Here's what each part of the command means:

- `python`: This is the Python interpreter executable.

- `-m`: This option stands for "module" and is used to run a Python module as a script.

- `venv`: This is the name of the Python module that is used to create virtual environments. It's a standard module in Python 3 and later versions.

- `venv`: This is the name you're giving to your virtual environment. In this case, you've chosen to name the virtual environment "venv," but you can replace it with a different name if you prefer.

When you run this command, it will create a directory named "venv" in your current directory. Inside this "venv" directory, you'll find a self-contained Python environment with its own copy of the Python interpreter and a separate `lib` directory where Python packages and modules can be installed. This isolated environment allows you to work on Python projects without affecting your system-wide Python installation and without conflicting with other project's dependencies.

> Modules are typically not meant to be executed directly as standalone programs. They are designed to be imported and used by other scripts or modules.

## Activate the virtual environment

Activating a virtual environment means making it the currently active Python environment on your system. When you activate a virtual environment, you switch to using the Python interpreter, packages, and environment variables associated with that specific virtual environment.

**macOS and Linux:**
   On macOS and Linux, you use the `source` command to activate the virtual environment. Open a terminal and navigate to your virtual environment directory, then run:

   ```bash
   source myenv/bin/activate
   ```

   Again, replace `myenv` with the name of your virtual environment.

After running the appropriate activation command, your command prompt or terminal will typically change to indicate that the virtual environment is active. You'll see the name of the virtual environment in the command prompt or terminal, which indicates that any Python commands you run will use the Python interpreter and packages within that virtual environment.

While the virtual environment is active, any Python packages you install using `pip` will be installed within that environment, keeping them separate from the global Python installation or other virtual environments you may have.

You can deactivate the virtual environment at any time by simply running the `deactivate` command:

```bash
deactivate
```

Deactivating the virtual environment returns you to your system's default Python environment.

Activating and using virtual environments is a best practice for managing Python projects, isolating dependencies, and keeping your Python environments clean and organized.


## Install Scrapy

```bash
pip3 install scrapy
```

## Setup a new Scrapy project

### How to create a new Scrapy project

```bash
scrapy startproject nba_game_time
```

### items.py

Describe the data you want to extract in `items.py` file.

### pipelines.py

Define the pipeline to store the data in `pipelines.py` file. The pipeline is a Python class that implements methods that define the item processing behavior.

### middlewares.py

Define the middleware to handle the request and response in `middlewares.py` file. The middleware is a Python class that implements methods that define the request and response handling behavior.

### settings.py

It contains all the settings of the project. You can set the user agent, the pipelines, the middlewares, etc.

## Create Scrapy spider

```bash
scrapy genspider books quotes.toscrape.com
```

## ipython

```bash
pip3 install ipython
```

In Scrapy, setting `shell = ipython` in a Spider class is used to specify that you want to use IPython as the interactive shell when you run the `scrapy shell` command. This setting affects how you interact with the Scrapy shell for debugging and testing purposes.

Here's what it does:

1. **Scrapy Shell**:
   - The Scrapy shell is a powerful tool that allows you to interactively test and debug your web scraping code and XPath or CSS selectors.
   - When you run the `scrapy shell` command in your terminal, you enter an interactive environment where you can experiment with Scrapy commands and inspect web pages.

2. **`shell` Attribute**:
   - In a Scrapy Spider class, you can set the `shell` attribute to specify which interactive shell you want to use when running `scrapy shell`.
   - By default, Scrapy uses the standard Python interactive shell (`shell = python`) for the Scrapy shell.

3. **`shell = ipython`**:
   - When you set `shell = ipython` in a Spider class, you are configuring Scrapy to use IPython as the interactive shell when you run `scrapy shell`.
   - IPython is an enhanced interactive Python shell with additional features like tab-completion, history, and more advanced interactive capabilities compared to the standard Python shell.

### fetch()

The `fetch()` method is used to download a web page and store it in a `response` object. The `fetch()` method takes a URL as its only argument and returns a `response` object.

- `response.css('article.product_pod')` : This is a CSS selector that selects the first `article` element with the class `product_pod` and returns the HTML code for that element as a string.

### `book.css('h3 a::text').get()`

The expression `book.css('h3 a::text').get()` is used in Scrapy, a Python web scraping framework, to extract text data from a web page. Let's break down what each part of this expression does:

1. `book`: This is typically a Scrapy `Selector` object, representing a portion of a web page's HTML content. You usually obtain this object by using a Scrapy response object's `css()` method or `xpath()` method to select specific HTML elements.

2. `.css('h3 a::text')`: This part of the expression is a CSS selector query. It is used to select an HTML element or elements within the `book` Selector object. Here's what each part of the CSS selector query does:
   - `h3`: Selects all `<h3>` elements within the `book` Selector.
   - `a`: Selects all `<a>` elements that are descendants of the selected `<h3>` elements.
   - `::text`: Selects the text content of the matched `<a>` elements.

   So, `book.css('h3 a::text')` selects all the text within `<a>` elements that are descendants of `<h3>` elements within the `book` Selector.

3. `.get()`: This is a method used to retrieve the first matching element's text content as a Python string. If multiple elements match the selector, `.get()` will return the text content of the first one.

In summary, `book.css('h3 a::text').get()` is a Scrapy expression that extracts the text content of the first `<a>` element that is a descendant of an `<h3>` element within the `book` Selector object. It returns this text content as a Python string.

### get attribute

- `book.css('h3 a').attrib['href']` : This expression is used to extract the value of the `href` attribute from the first `<a>` element that is a descendant of an `<h3>` element within the `book` Selector object. It returns this attribute value as a Python string.

### Yield 

In the code snippet you provided, the use of `yield` instead of `return` is a fundamental aspect of how Python generators work and is commonly used in Scrapy spiders for web scraping. Let me explain why `yield` is used in this context:

1. **Generator Function**: The code you provided is inside a Python generator function. When you use `yield` within a function, it turns that function into a generator. A generator is a special type of iterable in Python.

2. **Multiple Items**: In web scraping with Scrapy, you often want to extract data from multiple items on a webpage. The `books` in your code appears to be an iterable (perhaps a list or a Scrapy SelectorList) containing multiple book items on a webpage.

3. **Iterative Extraction**: By using `yield`, you are telling Python to yield (return) each extracted book item one at a time as they are processed, rather than returning all the items at once. This is beneficial for several reasons:
   - Memory Efficiency: When scraping large websites, there could be a lot of items to extract. Using `yield` ensures that you don't need to store all items in memory simultaneously, which can save memory.
   - Lazy Evaluation: `yield` allows for lazy evaluation. It means that you can process and yield items as needed, and the next item is only generated when requested, making the code more efficient.
   - Streaming: It's like streaming data. As each item is processed and yielded, it can be processed or saved immediately without waiting for the entire list of items to be collected.

4. **Iteration**: The code that consumes the generator (e.g., a Scrapy pipeline) can iterate over the yielded items one by one and process them individually. This is often more practical when dealing with web scraping because you want to process data as you scrape it, rather than waiting until all data is scraped before processing it.

In contrast, if you were to use `return` instead of `yield`, you would only be able to return a single dictionary containing information about one book, and the function would exit immediately. You'd lose the ability to efficiently handle multiple items and perform iterative processing.

So, in summary, the use of `yield` is a key feature of generator functions and is well-suited for scenarios where you want to process and yield multiple items one at a time, as is often the case in web scraping with Scrapy.


> It's important to understand that the function's state, including variable values, is indeed saved when using yield. When a generator function encounters a yield statement and pauses its execution, it remembers its internal state, such as the values of variables, the position in the code, and more. This allows the generator to resume execution from where it left off when you iterate over it or call next() on it.

> They don't precompute and store all their values in memory at once. Instead, they generate values on-the-fly as you iterate over them, which can be very beneficial when dealing with large datasets.

#### Why use yield instead of return in Scrapy?

The reason Scrapy uses `yield` instead of `return` in this context is because Scrapy is designed for asynchronous and non-blocking web scraping. Using `yield` allows Scrapy to efficiently process multiple requests and responses while minimizing memory usage.

Here's why `yield` is preferred over `return` in Scrapy:

1. Asynchronous Processing: Scrapy is built on top of Twisted, an asynchronous networking framework. When you make HTTP requests and process responses, Scrapy can handle multiple requests concurrently. If you used `return` instead of `yield`, it would block the entire process until all requests are completed, making the scraping process much slower.

2. Memory Efficiency: Scrapy is designed to work with large datasets and websites with many pages. When you use `yield`, the items are generated one by one and can be processed and saved to storage (like a database) without holding all items in memory simultaneously. This is crucial for scraping websites with a large number of items.

3. Streaming Data: `yield` essentially streams the scraped data, which means it can be processed and saved in real-time or in chunks. This is useful for scenarios where you want to process data as soon as it's available, rather than waiting for the entire scraping process to finish.

4. Non-blocking: Using `yield` allows Scrapy to continue processing other pages or items while waiting for network requests to complete. This non-blocking behavior improves the overall efficiency and responsiveness of the scraping process.

In summary, `yield` is used in Scrapy to take advantage of its asynchronous and non-blocking nature, making it more efficient and suitable for web scraping tasks involving multiple pages and large datasets. Using `return` would not provide the same benefits in terms of performance and memory usage.

## If reach the end 

If next page is not `None`, then there is another page.

## GO to next page

### response.follow
In Scrapy, the `response.follow` method is used to create a new request to follow a link or URL found in the current web page (response). Here's what `response.follow` does:

1. **Creates a New Request:** When you call `response.follow(next_page_url, callback=self.parse)`, you're instructing Scrapy to create a new HTTP request to the URL specified in `next_page_url`. This request will be sent to the web server hosting that URL to retrieve the corresponding web page.

2. **Callback Function:** The `callback=self.parse` part indicates that once the response is received from the URL, Scrapy should invoke the specified callback function, which is typically `self.parse` in this case. The callback function defines how Scrapy should parse and extract data from the newly fetched page.

3. **Handling Relative URLs:** `response.follow` is also helpful when dealing with relative URLs. It can handle both absolute and relative URLs correctly. In the example you provided, it constructs the complete URL by appending `next_page` (which often contains a relative URL) to the base URL, ensuring that the correct page is requested.

4. **Automatic Filtering:** Scrapy's `response.follow` method automatically filters and handles duplicate requests. It helps prevent requesting the same URL multiple times, which can be crucial for web scraping efficiency.

Overall, `response.follow` simplifies the process of navigating from one page to another during web scraping. It abstracts the creation of new requests, URL construction, and callback assignment, allowing you to focus on defining how to extract data from different pages of a website while Scrapy manages the request and response flow.



## Handle dynamic content

```bash
scrapy crawl quotes -o quotes.json
```

[good video](https://www.youtube.com/watch?v=Pu3gmdWsLYc&list=PLj4hN6FewnwrQ3Soq1e2MKISnoWyPkWfB)

### scrapy request

The line of code you provided is creating an instance of a `scrapy.Request` object. Let's break down what each part of this line does:

1. `request = scrapy.Request(`: This initializes a new Scrapy Request object and assigns it to the variable `request`.

2. `url=url`: This sets the URL that the request should be sent to. The `url` variable is passed as an argument to specify the URL you want to scrape.

3. `callback=self.parse_schedule`: This specifies the callback function that should be called when the response to this request is received. In this case, it's set to `self.parse_schedule`, which means that when the response is received, Scrapy will call the `parse_schedule` method of the spider to handle and parse the response.

4. `headers=self.headers)`: Here, you are passing a dictionary of HTTP headers to be included in the request. `self.headers` likely contains a set of headers that you want to send with this request, such as user-agent, accept-encoding, etc. These headers can help mimic a real browser request or specify certain preferences for the server.

Overall, this line of code is creating an HTTP request object with a specified URL, callback function, and headers, which Scrapy will use to make the request and handle the response when scraping a website.

