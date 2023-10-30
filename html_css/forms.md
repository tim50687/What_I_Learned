# Forms

An HTML form is used to collect user input. The user input is most often sent to a server for processing.

## Creating a basic form

- use `label` to associate a label with an input field
    - `for attribute` of the `label` element should match the `id attribute` of the `input` element
    - This allows assistive technologies to create a linked relationship between the label and the input field

- use `button` to create a submit button

    - `type="submit"` attribute specifies that the button should submit the form data to the server when clicked
    - `type="reset"` attribute specifies that the button should reset all the form fields to their default values when clicked

## Styling forms

> Label is inline by default. We can change it to block level element by setting `display: block;` in CSS.

When styling HTML forms, it's important to create a visually appealing and user-friendly design. Here are some key CSS rules and practices for styling forms, as demonstrated in your example:

1. **Font Styles and Line Height:**
   - Set a suitable font family for the form elements to ensure readability.
   - Define a comfortable line height (`line-height`) for better text spacing.

```css
body {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    line-height: 1.5;
    padding: 1rem;
}
```

2. **Labels:**
   - Use `display: block;` to make labels appear on a new line for better alignment and readability.

```css
label {
    display: block;
}
```

3. **Input Fields (Text and Email):**
   - Apply consistent styling to text and email input fields.
   - Use `border` and `border-radius` properties to create a bordered and slightly rounded appearance.
   - Add padding for comfortable spacing.
   - Use `transition` to create smooth effects when the input fields are focused.

```css
input[type="text"],
input[type="email"] {
    border: 1px solid gold;
    border-radius: 5px;
    padding: 0.5rem 0.7rem;
    transition: border-color 0.15s, box-shadow 0.15s;
}

input[type="text"]:focus,
input[type="email"]:focus {
    border-color: red;
    outline: 0;
    box-shadow: 0 0 0 4px rgba(24, 117, 255, 0.25);
}
```

4. **Buttons:**
   - Style buttons for a consistent and visually appealing look.
   - Use `background-color`, `color`, `border`, `padding`, and `border-radius` properties.
   - Remove the default button border with `border: 0;`.
   - Remove the button outline with `outline: 0;`.

```css
button {
    background-color: dodgerblue;
    color: white;
    border: 0;
    padding: 0.5rem 0.7rem;
    border-radius: 5px;
    outline: 0;
}
```

5. **Form Grouping:**
   - Use the `.form-group` class to group form elements for consistent spacing between them.

```css
.form-group {
    margin-bottom: 1rem;
}
```

These CSS rules help create a clean and visually appealing form while maintaining user-friendly interactivity. It's important to adapt these styles to suit your website's overall design and branding. Additionally, consider accessibility practices, such as using appropriate contrast ratios and providing clear focus indicators, to ensure that your forms are usable by all visitors.


> However, it's really time-consuming to style forms from scratch. So, we can use CSS frameworks like Bootstrap to style forms.

## CSS Frameworks

CSS frameworks are pre-written CSS files that contain a set of common styles and components. They can be used to quickly build and style websites.

### CDN (Content Delivery Network)

A CDN is a network of servers that deliver cached static content from websites to users based on their geographic location. This helps reduce the time it takes to load a website.

- Optimized for delivering web assets like images, CSS, and JavaScript files

#### Clarification on CDN

A CDN (Content Delivery Network) is not a link but a network of distributed servers or data centers. However, in web development, when people refer to "using a CDN," they typically mean including external resources (such as stylesheets, JavaScript libraries, fonts, or images) in their web pages via URLs provided by the CDN.

In your previous code snippet, the following line is an example of using a CDN to include an external stylesheet in your web page:

```html
<link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
    rel="stylesheet"
    integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
    crossorigin="anonymous"
/>
```

Here, the URL `"https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"` points to the Bootstrap CSS file hosted on a CDN (jsDelivr CDN in this case). By including this URL in the `<link>` tag, you are effectively loading the Bootstrap stylesheet from the CDN, which applies Bootstrap styles to your web page.

So, while a CDN itself is a network infrastructure, when people talk about "using a CDN," they are usually referring to the practice of linking to external resources hosted on a CDN to improve the delivery speed and reliability of those resources in web applications.

**Using Bootstrap and HTML Forms**

In the provided code snippet, Bootstrap, a popular front-end framework, is used to style and enhance the appearance of an HTML form. Here's a breakdown of the code and a note on how Bootstrap is utilized:

```html
<link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
    rel="stylesheet"
    integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
    crossorigin="anonymous"
/>
```

- This link element imports the Bootstrap CSS stylesheet from a Content Delivery Network (CDN). It ensures that Bootstrap styles and components are applied to the form and its elements.

```html
<form class="w-50">
```

- This `<form>` element has a Bootstrap class `w-50`, which sets the form's width to 50% of its parent container. Bootstrap provides a wide range of utility classes like `w-50` for quick styling.

```html
<div class="mb-3">
    <label class="form-label" for="name">Name</label>
    <input class="form-control" id="name" type="text" />
</div>
```

- These `<div>` elements with the class `mb-3` create form groups, adding margin below each group for spacing.
- Bootstrap classes like `form-label` and `form-control` style the label and input elements, respectively.
- The `for` attribute in the label associates it with the input element via the `id` attribute.

```html
<button class="btn btn-primary" type="submit">Register</button>
<button class="btn btn-secondary" type="reset">Clear</button>
```

- These `<button>` elements have Bootstrap classes (`btn`, `btn-primary`, and `btn-secondary`) to style them as buttons.
- The `type` attribute specifies the button's behavior (submit or reset) within the form.

**Note:** Bootstrap simplifies the process of creating visually appealing and responsive forms by providing ready-made CSS classes and components. It's important to include the Bootstrap CSS and any necessary JavaScript components to enable full Bootstrap functionality. The `integrity` and `crossorigin` attributes in the `<link>` tag ensure the integrity and security of the linked Bootstrap file.

### Milligram

- [Milligram](https://milligram.io/) is a minimalist CSS framework that provides a set of styles and components for building websites.

`Global Styles`: The CSS framework provides global styles for common HTML elements, so you don't need to specify classes for each element. For example, Milligram defines default styles for `<input>`elements, so once the framework is applied, all `<input>` elements will look styled without needing specific classes.


## Text Fields

- To capture numeric input, we can use `type="number"` attribute in the `input` element.

- We can also do the `password` input field by setting `type="password"` attribute in the `input` element.

- `date` input field is used to capture date input.

- `email` input field is used to capture email input.

### Multiplie Line Text Fields

- We can use `textarea` element to create a multiplie line text field.

```css
textarea {
    resize: none;
}
```

### Input field

- We can set the `value` attribute in the `input` element to set the default value of the input field.

    - **However**, in textarea element, we have to set the default value between the opening and closing tags.

- `placeholder="Hello"` attribute is used to set the placeholder text.

- `readonly` attribute is used to make the input field read-only.

- `disabled` attribute is used to disable the input field.
    - This value will not be sent to the server when we submit the form.

- `maxlength="3"` attribute is used to set the maximum length of the input field.

- `autofocus` attribute is used to set the focus on the input field when the page loads.


## Data Lists

### `datalist`, `option` style will not be applied. 

**Using `<datalist>` for Autocomplete Suggestions**

```html
<form>
    <input type="text" list="country" autocomplete="off" />
    <datalist id="country">
        <!-- set unique identifier -->
        <option data-value="1">Australia</option>
        <option>Canada</option>
        <option>India</option>
        <option>China</option>
    </datalist>
</form>
```

- `<datalist>` is an HTML element that provides a list of predefined options for an `<input>` element, allowing users to choose from a set of suggestions as they type.

- `<input>`: This is the input field where users can type their input. The `type="text"` attribute specifies that it's a text input. The `list` attribute is set to "country," which links this input field to the `<datalist>` with the same `id` value.

- `autocomplete="off"`: This attribute is set to "off" to disable the browser's built-in autocomplete feature. This ensures that the custom autocomplete suggestions provided by the `<datalist>` are used instead.

- `<datalist id="country">`: This is the `<datalist>` element with the `id` attribute set to "country." It serves as the container for the autocomplete options.

- `<option>`: Inside the `<datalist>`, you have a list of `<option>` elements. Each `<option>` represents a suggestion that will appear in the autocomplete dropdown when the user interacts with the `<input>` field.

- `data-value`: The `data-value` attribute is used here as an additional piece of data associated with the "Australia" option. This attribute can be used to store custom data related to the suggestion, which can be accessed via JavaScript if needed.

**Note:**
- The combination of `<input>` and `<datalist>` elements provides a user-friendly way to offer autocomplete suggestions to users, improving the user experience.
- The `autocomplete="off"` attribute on the `<input>` is optional but can be useful to prevent interference from the browser's native autocomplete feature.
- The `datalist` can include as many `<option>` elements as needed, and users will see suggestions based on what they type in the input field.
- The `data-value` attribute is an example of custom data that can be associated with each suggestion for additional functionality or data handling.
- This technique is commonly used in search boxes, location inputs, and other forms where suggesting options can enhance usability.

## Drop Down Lists

- We can use `multiple` attribute to allow users to select multiple options.

**Using `<select>` Element with `<optgroup>`**

In the provided HTML code snippet, the `<select>` element is used in conjunction with the `<optgroup>` element to create a dropdown menu with categorized options. Here's an explanation and note for this code:

```html
<form>
    <select>
        <optgroup label="Front End courses">
            <option value="">Select a Course ...</option>
            <option value="1" selected>HTML</option>
            <option value="2">CSS</option>
            <option value="3">JS</option>
        </optgroup>
        <optgroup label="Back End courses">
            <option value="">Select a Course ...</option>
            <option value="1" selected>Node</option>
            <option value="2">ASP</option>
            <option value="3">Django</option>
        </optgroup>
    </select>
</form>
```

- `<select>`: This is the HTML element that creates a dropdown menu or select box. Users can choose one option from the list.

- `<optgroup>`: The `<optgroup>` element is used to group related options within the `<select>` element. It provides a visual grouping and label for a set of related options.

- `label`: The `label` attribute of the `<optgroup>` element sets the label or title for the group of options. In this example, there are two groups: "Front End courses" and "Back End courses."

- `<option>`: Inside each `<optgroup>`, there are `<option>` elements. These are the individual items that users can select from the dropdown list.

- `value`: The `value` attribute of each `<option>` specifies the value that will be sent to the server when the user selects that option. It represents the data associated with the option.

- `selected`: The `selected` attribute is used to preselect an option when the page loads. In this example, the "HTML" option in the "Front End courses" group and the "Node" option in the "Back End courses" group are preselected.

**Note:**

- The use of `<optgroup>` allows you to categorize and organize options within a `<select>` element, making it easier for users to find and select the option they want.

- The `label` attribute provides a clear title for each group, improving the user experience and the clarity of the dropdown.

- The `value` attribute of each `<option>` is used to specify the value associated with that option, which can be used for form submissions or data processing.

- Preselecting options using the `selected` attribute can be useful when you want to suggest default choices to users.

- Dropdown menus are commonly used for various selection tasks in forms and user interfaces, and `<optgroup>` helps maintain a well-organized and user-friendly design for such menus.


## Checkboxes

**Creating Checkboxes with Labels and Disabled States**

In the provided HTML code snippet, checkboxes are created within a `<form>` element and are associated with corresponding labels. Additionally, one checkbox is disabled while the other is checked. Here's an explanation and note for this code:

```html
<form>
    <div>
        <input type="checkbox" id="frontend" disabled />
        <label class="label-inline" for="frontend">front-end</label>
    </div>
    <div>
        <input type="checkbox" id="backend" checked />
        <label class="label-inline" for="backend">back-end</label>
    </div>
</form>
```

- `<form>`: This is the HTML element that wraps the checkboxes. It represents a form where users can input data or make selections.

- `<input type="checkbox">`: These are checkboxes created using the `<input>` element with the `type` attribute set to "checkbox." Checkboxes allow users to make binary selections (on/off or true/false).

- `id`: The `id` attribute uniquely identifies each checkbox. It is used to associate the `<input>` element with its corresponding `<label>` element using the `for` attribute in the label.

- `disabled`: The `disabled` attribute is applied to the first checkbox (`id="frontend"`). This attribute disables the checkbox, making it unselectable and indicating that the option is not available or applicable.

- `checked`: The `checked` attribute is applied to the second checkbox (`id="backend"`). This attribute preselects the checkbox, indicating that the option is initially chosen or active.

- `<label>`: Labels are associated with each checkbox using the `for` attribute, which matches the `id` of the corresponding checkbox. Labels provide a text description for the checkbox and improve accessibility by allowing users to click the label to toggle the checkbox.

- `class="label-inline"`: This class is applied to the labels to style them in an inline manner, aligning them next to their respective checkboxes.

**Note:**

- Checkboxes are commonly used in forms to allow users to select one or more options.

- The `id` attribute of each checkbox should match the `for` attribute of its corresponding label to create a semantic association between the checkbox and label. Clicking the label toggles the checkbox.

- The `disabled` attribute can be used to prevent users from interacting with a checkbox, making it visually distinct and indicating that the option is not selectable.

- The `checked` attribute can be used to preselect a checkbox when the page loads, indicating that the option is initially chosen.

- Labels provide context and improve usability by making it easier for users to understand the purpose of each checkbox.

- The `class` attribute can be used to apply custom styles to elements, such as labels, for design and layout purposes.


## Radio Buttons

**Creating Radio Buttons with Labels and Default Selection**

In the provided HTML code snippet, radio buttons are created within a `<form>` element and associated with corresponding labels. Additionally, one of the radio buttons is checked by default. Here's an explanation and note for this code:

```html
<form>
    <div>
        <input type="radio" name="membership" id="silver" checked />
        <label for="silver" class="label-inline">Silver</label>
    </div>
    <div>
        <input type="radio" name="membership" id="gold" />
        <label for="gold" class="label-inline">Gold</label>
    </div>
</form>
```

- `<form>`: This is the HTML element that wraps the radio buttons. It represents a form where users can input data or make selections.

- `<input type="radio">`: These are radio buttons created using the `<input>` element with the `type` attribute set to "radio." Radio buttons allow users to select a single option from a group of choices.

- `name`: The `name` attribute is used to group radio buttons together. Radio buttons with the same `name` attribute belong to the same group, and users can select only one option from the group.

- `id`: The `id` attribute uniquely identifies each radio button. It is used to associate the `<input>` element with its corresponding `<label>` element using the `for` attribute in the label.

- `checked`: The `checked` attribute is applied to the first radio button (`id="silver"`). This attribute preselects the radio button, indicating that the "Silver" membership is the default selection.

- `<label>`: Labels are associated with each radio button using the `for` attribute, which matches the `id` of the corresponding radio button. Labels provide a text description for the radio button and improve accessibility by allowing users to click the label to select the radio button.

- `class="label-inline"`: This class is applied to the labels to style them in an inline manner, aligning them next to their respective radio buttons.

**Note:**

- Radio buttons are commonly used in forms when users need to select a single option from a group of choices (e.g., selecting a membership level).

- The `name` attribute is crucial for grouping radio buttons. Radio buttons within the same group (sharing the same `name`) are mutually exclusive, meaning users can select only one option from the group.

- The `checked` attribute can be used to preselect a radio button when the page loads, indicating the default selection.

- Labels improve the usability and accessibility of radio buttons by providing a text description and allowing users to click the label to select the associated radio button.

- The `class` attribute can be used to apply custom styles to elements, such as labels, for design and layout purposes.

## File input

- `multiple` attribute is used to allow users to select multiple files.

- `accept=".jp .png"` attribute is used to allow users to select only image files.

- `accept="image/*"` attribute is used to allow users to select any image files.
    - Or audio files: `accept="audio/*"`

## Grouping Related Fields

- We can use `fieldset` element to group related fields.

- We can use `legend` element to set the title of the fieldset.

## Hidden Fields

- We can use `hidden` attribute to hide the input field.

### Purpose of hidden fields

- To send data to the server that the user does not need to see or interact with.

> Don't put sensitive value, because user can always see the value by inspecting the page.

## Data Validation

Before submitting the form, we can validate the data to make sure that the data is in the correct format.

- `required` attribute is used to make the input field required.

- `minlength="3"` attribute is used to set the minimum length of the input field.
    - `maxlength="10"` attribute is used to set the maximum length of the input field. 

> Always use maxlength attribute to prevent users from entering too much data.

### Numbers

- `min="1"` attribute is used to set the minimum value of the input field.
    - `max="10"` attribute is used to set the maximum value of the input field.

## Submitting Forms

- `action="https://www.google.com"` attribute is used to set the URL where the form data will be sent to.

- `method="get"` attribute is used to set the HTTP method to `GET`.
    - `method="post"` attribute is used to set the HTTP method to `POST`.