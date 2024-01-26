# Getting the detail of the page 

## Using XPath

If no class name or id is available, we can use XPath to get the content we want.

```python
response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get()

response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
```


Regarding the `//` in XPath:

- `//` is an XPath axis specifier that is used to search for elements anywhere in the document, regardless of their position in the HTML tree. It is often used to perform searches that are not constrained to a specific location in the document hierarchy.

For example, the XPath expression `//div` would select all `<div>` elements in the entire document, not just the ones that are direct children of a specific parent element. It's a way to perform a global search for elements.

So, in the context of the XPath expression you provided earlier:

```xpath
//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()
```

The `//` at the beginning of the expression indicates that the search starts from the root of the document and looks for the specified elements (`ul`, `li`, `a`, etc.) anywhere in the document. It's used to perform a broad search across the entire HTML structure.

## Table

The code you provided:

```python
table_rows = response.css('table tr')
```

will select all the `<tr>` (table row) elements within any `<table>` element on the page. It will not limit the selection to just the first matching table row. Instead, it will capture all `<tr>` elements that match the CSS selector `'table tr'`.

If there are multiple tables on the page, this code will select all the table rows from all those tables.

If you want to limit the selection to only the first matching table row, you can use the `:first-child` pseudo-class like this:

```python
first_table_row = response.css('table tr:first-child')
```

This will select the first `<tr>` element within any `<table>` element on the page.


## Two classes

```html
<p class="star-rating Three">
```

"Three" is also a CSS class. Both "star-rating" and "Three" are classes assigned to the `<p>` element using the `class` attribute. It means that this element has two CSS classes: "star-rating" and "Three." These classes can be used for styling or selecting the element in CSS or JavaScript.

--- 

In HTML, `class` is indeed an attribute. The `class` attribute is used to assign one or more CSS classes to an HTML element. These CSS classes are used for styling or selecting elements using CSS or JavaScript.

So, in the code `response.css("p.star-rating").attrib['class']`, we are using Scrapy (a web scraping framework) to select a `<p>` element with the class `"star-rating"` from the HTML content of a web page. Once we have selected that element, we are using the `.attrib['class']` part to access the `class` attribute of that specific `<p>` element and retrieve its value.

To clarify:

- `class` is an HTML attribute.
- `"star-rating"` is a CSS class assigned to an HTML element using the `class` attribute.
- `response.css("p.star-rating").attrib['class']` selects an element with the class `"star-rating"` and retrieves the value of its `class` attribute.

## ways to get attributes

Yes, you can retrieve attributes from HTML elements using Scrapy in two ways:

1. Using `.attrib['attribute_name']`: You can use `.attrib['attribute_name']` to directly access the value of an attribute. For example:
   
   ```python
   href_value = response.css('li.next a').attrib['href']
   ```

2. Using `::attr(attribute_name)`: You can also use the `::attr(attribute_name)` pseudo-selector to directly extract the value of an attribute. For example:

   ```python
   href_value = response.css('li.next a::attr(href)').get()
   ```

Both methods achieve the same result of retrieving the value of the specified attribute, but the second method with `::attr(attribute_name)` is often preferred for its brevity and clarity when working with Scrapy selectors.

## Use scrapy pipe line to clean data

### Items

When you generate scrapy project, you will see a file called `items.py`. This file is used to define the data structure of the data you want to scrape. 

- Use item.py to prevent from typo
### `scrapy.Field()`

`scrapy.Field()` is a class provided by the Scrapy framework for defining fields in Scrapy Item classes. In Scrapy, Item classes are used to define the structure of the data that you want to extract from web pages. Each field in an Item class corresponds to a specific piece of information you want to scrape from a web page.

When you define a field using `scrapy.Field()`, you are essentially telling Scrapy what type of data should be stored in that field. Scrapy provides several field types that you can use based on the type of data you are extracting. Some common field types include:

- `scrapy.Field()`: Used for generic text data.
- `scrapy.IntField()`: Used for integer data.
- `scrapy.FloatField()`: Used for floating-point (decimal) data.
- `scrapy.DateField()`: Used for date data.
- `scrapy.BoolField()`: Used for boolean (True/False) data.

By defining fields in your Item classes, you specify the structure of the data that your spider will collect. This structured data can then be populated with scraped information during the spider's execution.

Here's an example of how you might define a field in a Scrapy Item class:

```python
import scrapy

class MyItem(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.IntField()
    rating = scrapy.FloatField()
```

In this example, `name` is a field that can store text data, `age` is a field for integer data, and `rating` is a field for floating-point data. When you populate an instance of `MyItem` with scraped data, you assign values to these fields accordingly.


## Serializing

> If small amount of post processing, use serializer. Or else use `pipeline`

In Scrapy, the `serializer` argument in a Field allows you to specify a function that will be used to serialize (format or transform) the data before it's stored in the item attribute. 

In your example, the `price_excl_tax` field is associated with the `serialize_price` function as its serializer. This means that when you assign a value to `price_excl_tax` in a Scrapy Item, the value will be passed through the `serialize_price` function to format it before storing it in the `price_excl_tax` attribute of the item.

Here's how it works:

```python
def serialize_price(value):
    return f'£ {str(value)}'

# Define the Scrapy Item with a serialized field
class BookItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()
    price_excl_tax = scrapy.Field(serializer=serialize_price)
```

Now, when you set a value for `price_excl_tax` in a Scrapy spider, it will be automatically formatted using the `serialize_price` function before being stored in the item:

```python
item = BookItem()
item['price_excl_tax'] = 10  # The value is automatically formatted as '£ 10'
```

This is useful when you want to apply a specific transformation or formatting to the data before storing it in the item. In this case, it's adding the '£' symbol to the price.


## Pipeline

### What is pipeline

A pipeline is a component of Scrapy that is used to process the items scraped by the spider. It provides a convenient mechanism for storing, cleaning, and processing the scraped data before it's sent to the database or other storage destination.

### Need to go to setting to make sure the pipeline is enabled

### How pipeline works

In Scrapy, item pipelines are used to process and manipulate items (data) after they are scraped but before they are saved or further processed. The item pipeline you've provided will be invoked for each item scraped by the spider. Here's an overview of when the pipeline gets involved:

1. Spider Scrapes Data: When your spider scrapes a web page and extracts data, it creates `Item` objects that hold that data. These `Item` objects are Python dictionaries with specific fields.

2. Yield Items: In your spider's `parse` method (or other callback methods), you use `yield` to send these `Item` objects (or other items you create) back to Scrapy. For example:
   
   ```python
   yield item
   ```

   This sends the `Item` to the Scrapy engine for further processing.

3. Item Pipeline Processing: After an item is yielded, it goes through the item pipeline(s) you've configured. In your case, you've defined a custom item pipeline class `BookstorePipeline`. The `process_item` method of this class is called for each yielded item.

4. Custom Processing: In the `process_item` method of your pipeline, you can apply custom transformations, cleaning, and formatting to the item's fields. For example, you might convert string prices to floats, lowercase text fields, or extract specific information.

5. Return Item: After processing, you can modify the item as needed, and then you typically return the modified item. The returned item will continue through the pipeline or be saved to the output (e.g., JSON or CSV file) if it's the last step in the pipeline.

6. Further Processing or Storage: Once the item has passed through the pipeline(s), it can be saved to a file or database, or you can perform additional processing on it as needed.

The pipelines are defined in your project's settings, and the order in which they are applied is determined by their priority values. In your case, the `BookstorePipeline` is given a priority of 300 (`"bookstore.pipelines.BookstorePipeline": 300`), which means it will be applied after other pipelines with lower priorities.

So, to summarize, the pipeline gets involved with Scrapy data after the spider scrapes data from web pages, and it allows you to perform custom data processing and transformations on the scraped items before they are saved or further processed.


## set where data will be save in our setting file 

```python
FEEDS = {
    'clean.json' : {'format' : 'json'}
}
```

