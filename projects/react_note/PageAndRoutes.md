# Adding pages and routes

## node.js

node.js is a runtime environment for executing JavaScript code. 

We will have npm and npx installed with node.js.

- npm: Node Package Manager
    - It is used to install and manage packages.

- npx: Node Package Runner
    - It is used to run packages.
    - It is an npm package runner that can execute any package that you want from the `npm registry without even installing that package`.


## App.js

App.js is the root component of the application.

- `ReactDOM.createRoot` 

is a method provided by React DOM, which is a package that serves as the entry point to the DOM and server-rendering features for React. This method is used to create a new root instance for a React application.

Here's what it does:

1. **Creates a Root Instance**: When you call `ReactDOM.createRoot`, you're creating a root instance for displaying content inside a browser DOM element.

2. **Attaches to a DOM Element**: The `createRoot` method takes a DOM element as an argument. This DOM element serves as the container where the React application will be mounted and rendered. Typically, this is an existing HTML element in your document. `React will create a root for this container, and take over managing the DOM inside it.`

3. **Returns a Root Instance**: After creating the root instance and associating it with the specified DOM element, `createRoot` returns this root instance. This instance can then be used to render React components into the specified container.

> After you’ve created a root, you need to call root.render to display a React component inside of it

> When you wrap components in <React.StrictMode>, React performs additional checks and logs warnings to the console for common issues

## ListItem

We can seperate the ListItem component into a new file called ListItem.js so that we can use it in other components.

Why?

- **Reusability**: By separating the ListItem component into its own file, we can use it in other components. This makes our code more modular and easier to maintain.

- **Readability**: Separating the ListItem component into its own file makes our code easier to read and understand. We can see the ListItem component in isolation, without having to scroll through a large file.

- **Organization**: Separating the ListItem component into its own file helps us organize our code. We can group related components together in separate files, making it easier to find and work with them.


> Don't forget to import CSS files if you are using them in the new file.

## Import icon as a component

We can import an icon as a component and use it in our application.

Why?


- **Reusability**: By importing an icon as a component, we can use it in multiple places in our application. This makes our code more modular and easier to maintain.

- **Readability**: Importing an icon as a component makes our code easier to read and understand. We can see the icon component in isolation, without having to scroll through a large file.

- **Organization**: Importing an icon as a component helps us organize our code. We can group related components together in separate files, making it easier to find and work with them.


## State 

State is javascript object that represents information about the component.