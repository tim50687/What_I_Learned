# OOP

## Access Modifiers

- public: can be accessed from anywhere

- private: no other class can access

- protected: protected allows classes in the same package, and any subclass in other packages to access

- no modifier: can only be accessed from within the class and package


## null

- null is a special literal in Java that represents a null reference, one that does not refer to any object. null is the default value for reference-type variables.

- fields with primitive types are never null

## this

It refers to the instance that was created when the object was instantiated.


## Benefits of setters and getters

- You can add validation code inside the setter method.

- You can hide the internal representation of the class.

## Default constructor

If a class does not have any constructor, the Java compiler automatically creates a default constructor during run-time.

## Constructor overloading

- Constructor overloading is a technique in Java in which a class can have any number of constructors that differ in parameter lists.

## Constructor chaining

- Constructor chaining is the process of `calling one constructor from another constructor` with respect to current object.

- First line of any constructor should be a call to either this() or super().

```java

  public BankAccount() {
    this("12345", 2.2, "Default Name", "Default Address", "Phone");
    System.out.println("Empty constructor called");
  }

  public BankAccount(String number, double balance, String customerName, String email,
      String phoneNumber) {
    System.out.println("Account constructor with parameters called");
    this.accountNumber = number;
    this.accountBalance = balance;
    this.customerName = customerName;
    this.email = email;
    this.phoneNumber = phoneNumber;

  }

```

### Why do we need constructor chaining?

**Constructor Chaining in Object-Oriented Programming**

Constructor chaining is a technique used in object-oriented programming, particularly in languages like Java, for various reasons:

1. **Code Reusability:** Constructor chaining allows you to reuse initialization code within different constructors. This helps in adhering to the DRY (Don't Repeat Yourself) principle and maintaining cleaner, more maintainable code.

2. **Overloading:** It enables you to provide multiple constructors with different parameter sets, allowing clients to create objects in different ways by choosing the appropriate constructor based on their needs.

3. **Encapsulation:** Complex initialization logic or common setup tasks can be encapsulated in a single constructor. Other constructors can then chain to it, hiding implementation details and providing a cleaner interface for object creation.

4. **Default Values:** Constructors with fewer parameters can set default values for missing parameters and then chain to constructors with more parameters. This reduces redundant code when creating objects and provides consistency.

5. **Consistency:** By having a "master" constructor that performs comprehensive initialization, you ensure that all objects are initialized consistently, even if some constructors provide shortcuts or omit certain steps.

Example in Java:

```java
public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public Person(String name) {
        this(name, 0); // Chain to the master constructor
    }

    public Person(int age) {
        this("Unknown", age); // Chain to the master constructor
    }
}
```

In this example, constructor chaining ensures consistent object creation while providing flexibility for clients to choose suitable constructors.
