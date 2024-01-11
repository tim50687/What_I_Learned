# Keywords and Expressions


## **Variable Assignment and Copies in Java**

In Java, when you assign one variable to another, you are making a copy of the value stored in the source variable. Any changes made to the source variable after the assignment do not affect the destination variable. This behavior is particularly important to understand when working with primitive data types.

For example:

```java
int score = 100;
int finalScore = score; // finalScore gets a copy of the value in score

score = 200; // Changing score doesn't affect finalScore

System.out.println(finalScore); // Output: 100, not 200
```

In this scenario, `finalScore` initially receives a copy of the value in `score`, which is 100. Even when `score` is later updated to 200, `finalScore` remains unchanged. 

Remember that this copy behavior applies to primitive data types like `int`, `double`, `char`, etc. For non-primitive types (objects), assignment works differently and involves references, which can lead to different behavior.



### Avoid A lot of return statements

```java
public static int calculateHighScorePosition(int playerScore) {

    int position = 4;
    if (playerScore >= 1000) {
      position = 1;
    } else if (playerScore >= 500) {
      position = 2;
    } else if (playerScore >= 100) {
      position = 3;
    }
    return position;
  }
```


### Method Overloading

Method overloading is a feature that allows us to have more than one method with the same name, so long as we use different parameters. 

#### Method signature

The method signature is the combination of the method name and the parameter list. 

- A method return type is not part of the signature

- A parameter name is not part of the signature


```java
// These two methods have the different signatures
public static void doSomething(int A, float B) {
    // ...
}
public static void doSomething(float A, int B) {
    // ...
}

// These two methods have the same signature

public static void doSomething(int A) {
    // ...
}
public static void doSomething(int B) {
    // ...
}
```

> But you can not have same method signature with different return type

