# Control flow

## Switch

- Can do multiple switch cases in one line

```java

public class Main {

    public static void main(String[] args) {
        char switchValue = 'A';

        switch (switchValue) {
            case 'A':
            case 'B':
            case 'C':
            case 'D':
            case 'E':
                System.out.println("Found " + switchValue);
                break;

            default:
                System.out.println("Not found");
                break;
        }
    }
}

```


### Valid switch types

- byte
- short
- char
- int
- String
- enum

And the corresponding wrapper classes for the primitive types, Byte, Short, Character, Integer, and String.


### New feature for switch

```java
int switchValue = 2;
switch (switchValue) {
    case 1 -> System.out.println("Value was 1");
    case 2 -> System.out.println("Value was 2");
    case 3, 4, 5 -> {
    System.out.println("Was a 3 , a 4, or a 5");
    System.out.println("Actually was a " + switchValue);
    }
    default -> System.out.println("Was not 1 or 2 3,4,5");
}
``` 

- There is no need for break statement

- Now, switch statement is an expression, so we can assign the result to a variable

```java

  public static String getQuarter(String month) {
    return switch (month) {
      case "January", "February", "March" -> "1st";
      case "April", "May", "June" -> "2nd";
      case "July", "August", "September" -> "3rd";
      case "October", "November", "December" -> "4th";
      default -> "bad";
    };
  }
```

- Need to cover all cases, otherwise, it will not compile.


> We can also do something in the case branch before returning a value

YIELD!!!!

- yield has to be in the code block

```java

-> "1st"; 

// is implicitly transalted to

-> { yield "1st"; }

```

### Tips

You can also use switch in the for loop
  
```java

  for (int i = 1; i <= 5; i++) {
      Student s = new Student("S12345" + i, switch (i) {
        case 1 -> "Mary";
        case 2 -> "Carol";
        case 3 -> "Tim";
        case 4 -> "Harry";
        case 5 -> "Lisa";
        default -> "Anonymous";
      }, "01/04/2022", "Java Class");
    }

```

## Local variable and scope

### Narrowest scope

In programming, the "narrowest scope" refers to limiting the visibility or lifespan of a variable to the smallest portion of the code where it is actually needed. This practice is important for several reasons:

1. **Minimizing Bugs:** A variable with a narrow scope reduces the chances of bugs and unintended side effects. It ensures that the variable is only used in the specific part of the code where it's necessary, making it easier to reason about the code's behavior.

2. **Readability and Maintainability:** Narrowly scoped variables improve code readability and maintainability. When a variable is declared close to where it's used, it's easier for someone reading the code to understand its purpose and context.

3. **Resource Efficiency:** Variables with narrower scope also consume memory and resources for a shorter duration, which can be important in resource-constrained environments.

For example, consider this code snippet:

```java
for (int i = 0; i < 10; i++) {
    // ...
}
```

In this case, the variable `i` has a narrow scope limited to the `for` loop. It's created when the loop begins and is automatically destroyed when the loop ends. This is a good practice because you don't need `i` outside of the loop.

Conversely, if you declared `i` outside the loop and used it elsewhere in the code, it would have a broader scope than necessary and could lead to potential issues and decreased code clarity.

### Switch statement

The scope of the variable declared in the switch statement is limited to the switch block.



## Static and instances field

### Static field

- Value of the field is stored in special memory location and only in one place.

### Instance field

- Value of the field is not allocated any memory and has no value until the object is created


## Get user input

- `Integer.parseInt` : convert string to integer

1. You cannot use System.console() in intellij, this is because IDE disables it. You can use it in the terminal.

- `scanner.nextLine()` :  It will read the input string unless the line changes or a new line and then ends the input with \n or pressing enter.