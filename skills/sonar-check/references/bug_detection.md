# Sonar-Check - Bug Detection

**Pages:** 100

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-4973/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

It’s almost always a mistake to compare two instances of java.lang.String or boxed types like java.lang.Integer using reference equality == or !=, because it is not comparing actual value but locations in memory.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
java.lang.String
```

Example 2 (unknown):
```unknown
java.lang.Integer
```

Example 3 (unknown):
```unknown
String firstName = getFirstName(); // String overrides equals
String lastName = getLastName();

if (firstName == lastName) { ... }; // Non-compliant; false even if the strings have the same value
```

Example 4 (unknown):
```unknown
String firstName = getFirstName();
String lastName = getLastName();

if (firstName != null && firstName.equals(lastName)) { ... };
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6073/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Mockito provides argument matchers and argument captors for flexibly stubbing or verifying method calls.

Mockito.verify(), Mockito.when(), Stubber.when() and BDDMockito.given() each have overloads with and without argument matchers.

However, if argument matchers or captors are used only on some of the parameters, all the parameters need to have matchers as well, otherwise an InvalidUseOfMatchersException will be thrown.

This rule consequently raises an issue every time matchers are not used on all the parameters of a stubbed/verified method.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
Mockito.verify()
```

Example 2 (unknown):
```unknown
Mockito.when()
```

Example 3 (unknown):
```unknown
Stubber.when()
```

Example 4 (unknown):
```unknown
BDDMockito.given()
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5996/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

In regular expressions the boundaries ^ and \A can only match at the beginning of the input (or, in case of ^ in combination with the MULTILINE flag, the beginning of the line) and $, \Z and \z only at the end.

These patterns can be misused, by accidentally switching ^ and $ for example, to create a pattern that can never match.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
// This can never match because $ and ^ have been switched around
Pattern.compile("$[a-z]+^"); // Noncompliant
```

Example 2 (unknown):
```unknown
Pattern.compile("^[a-z]+$");
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6817/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

@Configuration is a class-level annotation indicating that an object is a source of bean definitions. @Configuration classes declare beans through @Bean-annotated methods. Calls to @Bean methods on @Configuration classes can also be used to define inter-bean dependencies. The @Bean annotation indicates that a method instantiates, configures, and initializes a new object to be managed by the Spring IoC container.

Annotating a method of a bean with @Async will make it execute in a separate thread. In other words, the caller will not wait for the completion of the called method.

The @Async annotation is not supported on methods declared within a @Configuration class. This is because @Async methods are typically used for asynchronous processing, and they require certain infrastructure to be set up, which may not be available or appropriate in a @Configuration class.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
@Configuration
```

Example 2 (unknown):
```unknown
@Configuration
```

Example 3 (unknown):
```unknown
@Configuration
```

Example 4 (unknown):
```unknown
@Configuration
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6816/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

SpEL, the Spring Expression Languages allows developers fine-grained control over the values injected into fields and parameters. Using the @Value annotation, it is possible to inject values from sources such as system properties.

The @Value annotation does not guarantee that the property is defined. Particularly if a field or parameter is annotated as nullable, it indicates that the developer assumes that the property may be undefined.

An undefined property may lead to runtime exceptions when the Spring framework tries to inject the autowired dependency during bean creation.

This rule raises an issue when a nullable field or parameter is annotated with @Value and no default value is provided.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5779/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Assertion methods are throwing a "java.lang.AssertionError". If this call is done within the try block of a try-catch cathing a similar error, you should make sure to test some properties of the exception. Otherwise, the assertion will never fail.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
java.lang.AssertionError
```

Example 2 (unknown):
```unknown
@Test
public void should_throw_assertion_error() {
  try {
    throwAssertionError();
    Assert.fail("Expected an AssertionError!"); // Noncompliant, the AssertionError will be caught and the test will never fail.
  } catch (AssertionError e) {}
}

private void throwAssertionError() {
  throw new AssertionError("My assertion error");
}
```

Example 3 (unknown):
```unknown
assertThrows(AssertionError.class, () -> throwAssertionError());
```

Example 4 (unknown):
```unknown
try {
   throwAssertionError();
   Assert.fail("Expected an AssertionError!"); // Compliant, we made sure to test that the correct error is raised
 } catch (AssertionError e) {
   Assert.assertThat(e.getMessage(), is("My assertion error"));
 }
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6320/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

This issue indicates that a cast operation will fail and throw a ClassCastException. To fix it, make sure only references to objects with a compatible type can be cast.

A cast operation allows an object to be "converted" from one type to another. The compiler raises an error if it can determine that the target type is incompatible with the declared type of the object, otherwise it accepts the cast. However, depending on the actual runtime type of the object, a cast operation may fail at runtime. When a cast operation fails, a ClassCastException is thrown.

This type of exception is usually unexpected. It causes the program to crash or puts it into an inconsistent state. Therefore, this issue might impact the availability and reliability of your application, or even result in data loss.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
ClassCastException
```

Example 2 (unknown):
```unknown
ClassCastException
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5863/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Assertions comparing an object to itself are more likely to be bugs due to developer’s carelessness.

This rule raises an issue when the actual expression matches the expected expression.

In a unit test validating the equals(...) and hashCode() methods, it’s legitimate to compare an object to itself. This rule does not raise an issue for isEqualTo, assertEquals or hasSameHashCodeAs when the unit test name contains (case insensitive): equal, hash_?code, object_?method. For example, in tests with the following names: test_equals, testEqual, test_hashCode, test_hash_code, test_object_methods.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
assertThat(actual).isEqualTo(actual); // Noncompliant
```

Example 2 (unknown):
```unknown
assertThat(actual).isEqualTo(expected);
```

Example 3 (unknown):
```unknown
equals(...)
```

Example 4 (unknown):
```unknown
assertEquals
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5790/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

If not annotated with @Nested, an inner class containing some tests will never be executed during tests execution. While you could still be able to manually run its tests in an IDE, it won’t be the case during the build. By contrast, a static nested class containing some tests should not be annotated with @Nested, JUnit5 will not share setup and state with an instance of its enclosing class.

This rule raises an issue on inner classes and static nested classes containing JUnit5 test methods which has a wrong usage of @Nested annotation.

Note: This rule does not check if the context in which JUnit 5 is running (e.g. Maven Surefire Plugin) is properly configured to execute static nested classes, it could not be the case using the default configuration.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
import org.junit.jupiter.api.Test;

class MyJunit5Test {
  @Test
  void test() { /* ... */ }

  class InnerClassTest { // Noncompliant, missing @Nested annotation
    @Test
    void test() { /* ... */ }
  }

  @Nested
  static class StaticNestedClassTest { // Noncompliant, invalid usage of @Nested annotation
    @Test
    void test() { /* ... */ }
  }
}
```

Example 2 (unknown):
```unknown
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Nested;

class MyJunit5Test {
  @Test
  void test() { /* ... */ }

  @Nested
  class InnerClassTest {
    @Test
    void test() { /* ... */ }
  }

  static class StaticNestedClassTest {
    @Test
    void test() { /* ... */ }
  }
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6906/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Java virtual threads enable the JVM to optimize the use of OS threads by mounting and unmounting them as needed. This makes them more efficient when dealing with blocking operations such as I/O or HTTP requests.

This rule applies only to code running on Java versions older than 24. Since Java 24, virtual threads are no longer pinned when executing synchronized code.

For Java version 21 to 23, when code is executed inside a synchronized block or method, the virtual thread remains pinned to its underlying OS thread and cannot be unmounted during a blocking operation. This causes the OS thread to be blocked, which can impact the scalability of the application.

Therefore, in environments running a Java version below 24, virtual threads should not execute code that contains synchronized blocks or invokes synchronized methods. Platform threads should be used in these cases instead.

This rule raises an issue when a virtual thread contains synchronized blocks or invokes synchronized methods.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
synchronized
```

Example 2 (unknown):
```unknown
synchronized
```

Example 3 (unknown):
```unknown
synchronized
```

Example 4 (unknown):
```unknown
synchronized
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6416/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

This issue indicates that an exception will be thrown because a method is used incorrectly. To fix it, check the requirements of the method and fulfill them.

It is common for methods to check the value of their parameters or the state of their associated object and throw an exception when one of them does not match a given condition. Those conditions are usually mentioned in the javadoc of the method.

This rule raises an issue when it detects that a method call will trigger one of the following exceptions:

Issues of this type interrupt the normal execution of a program, causing it to crash or putting it into an inconsistent state. Therefore, this issue might impact the availability and reliability of your application, or even result in data loss.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
java.lang.IllegalArgumentException
```

Example 2 (unknown):
```unknown
java.lang.IllegalStateException
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5967/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Annotating unit tests with more than one test-related annotation is not only useless but could also result in unexpected behavior like failing tests or unwanted side-effects.

This rule reports an issue when a test method is annotated with more than one of the following competing annotation:

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
@Test
@RepeatedTest(2) // Noncompliant, this test will be repeated 3 times
void test() { }

@ParameterizedTest
@Test
@MethodSource("methodSource")
void test2(int argument) { } // Noncompliant, this test will fail with ParameterResolutionException
```

Example 2 (unknown):
```unknown
@RepeatedTest(2)
void test() { }

@ParameterizedTest
@MethodSource("methodSource")
void test2(int argument) { }
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5783/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

When verifying that code raises an exception, a good practice is to avoid having multiple method calls inside the tested code, to be explicit about what is exactly tested.

When two of the methods can raise the same checked exception, not respecting this good practice is a bug, since it is not possible to know what is really tested.

You should make sure that only one method can raise the expected checked exception in the tested code.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
@Test
public void testG() {
  // Do you expect g() or f() throwing the exception?
  assertThrows(IOException.class, () -> g(f(1)) ); // Noncompliant
}

@Test
public void testGTryCatchIdiom() {
  try { // Noncompliant
    g(f(1));
    Assert.fail("Expected an IOException to be thrown");
  } catch (IOException e) {
    // Test exception message...
  }
}

int f(int x) throws IOException {
  // ...
}

int g(int x) throws IOException {
  // ...
}
```

Example 2 (unknown):
```unknown
@Test
public void testG() {
  int y = f(1);
  // It is explicit that we expect an exception from g() and not f()
  assertThrows(IOException.class, () -> g(y) );
}

@Test
public void testGTryCatchIdiom() {
  int y = f(1);
  try {
    g(y);
    Assert.fail("Expected an IOException to be thrown");
  } catch (IOException e) {
    // Test exception message...
  }
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5979/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Objects annotated with Mockito annotations @Mock, @Spy, @Captor, or @InjectMocks need to be initialized explicitly.

There are several ways to do this:

Test using uninitialized mocks will fail.

Note that this only applies to annotated Mockito objects. It is not necessary to initialize objects instantiated via Mockito.mock() or Mockito.spy().

This rule raises an issue when a test class uses uninitialized mocks.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
@InjectMocks
```

Example 2 (unknown):
```unknown
MockitoAnnotations.openMocks(this)
```

Example 3 (unknown):
```unknown
MockitoAnnotations.initMocks(this)
```

Example 4 (unknown):
```unknown
@RunWith(MockitoJUnitRunner.class)
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5810/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

JUnit5 is more tolerant regarding the visibilities of Test classes and methods than JUnit4, which required everything to be public. JUnit5 supports default package, public and protected visibility, even if it is recommended to use the default package visibility, which improves the readability of code.

But JUnit5 ignores without any warning:

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (csharp):
```csharp
import org.junit.jupiter.api.Test;

class MyClassTest {
  @Test
  private void test1() { // Noncompliant - ignored by JUnit5
    // ...
  }
  @Test
  static void test2() { // Noncompliant - ignored by JUnit5
    // ...
  }
  @Test
  boolean test3() { // Noncompliant - ignored by JUnit5
    // ...
  }
  @Nested
  private class MyNestedClass { // Noncompliant - ignored by JUnit5
    @Test
    void test() {
      // ...
    }
  }
}
```

Example 2 (unknown):
```unknown
import org.junit.jupiter.api.Test;

class MyClassTest {
  @Test
  void test1() {
    // ...
  }
  @Test
  void test2() {
    // ...
  }
  @Test
  void test3() {
    // ...
  }
  @Nested
  class MyNestedClass {
    @Test
    void test() {
      // ...
    }
  }
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3436/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

According to the documentation,

A program may produce unpredictable results if it attempts to distinguish two references to equal values of a value-based class, whether directly via reference equality or indirectly via an appeal to synchronization…​

This is because value-based classes are intended to be wrappers for value types, which will be primitive-like collections of data (similar to structs in other languages) that will come in future versions of Java.

Instances of a value-based class …​

This means that you can’t be sure you’re the only one trying to lock on any given instance of a value-based class, opening your code up to contention and deadlock issues.

Under Java 8 breaking this rule may not actually break your code, but there are no guarantees of the behavior beyond that.

This rule raises an issue when a known value-based class is used for synchronization. That includes all the classes in the java.time package except Clock; the date classes for alternate calendars, HijrahDate, JapaneseDate, MinguoDate, ThaiBuddhistDate; and the optional classes: Optional, OptionalDouble, OptionalLong, OptionalInt.

Note that this rule is automatically disabled when the project’s sonar.java.source is lower than 8.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
JapaneseDate
```

Example 2 (unknown):
```unknown
ThaiBuddhistDate
```

Example 3 (unknown):
```unknown
OptionalDouble
```

Example 4 (unknown):
```unknown
OptionalLong
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-2789/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Optional acts as a container object that may or may not contain a non-null value. It is introduced in Java 8 to help avoid NullPointerException. It provides methods to check if a value is present and retrieve the value if it is present.

Optional is used instead of null values to make the code more readable and avoid potential errors.

It is a bad practice to use null with Optional because it is unclear whether a value is present or not, leading to confusion and potential NullPointerException errors.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
NullPointerException
```

Example 2 (unknown):
```unknown
NullPointerException
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-7185/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Spring provides the @EventListener annotation as a simpler alternative to implementing the ApplicationListener interface for handling events. The @EventListener annotation registers a method as an event handler. This allows to skip the implementation of the ApplicationListener interface, making it easier to handle events.

The @EventListener annotation can only be used on methods that have at most one parameter, which should be the specific event that we want to handle. To listen to several types of events, use the classes argument of the @EventListener annotation.

This rule raises an issue on all methods annotated with @EventListener that have more than one parameter.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
@EventListener
```

Example 2 (unknown):
```unknown
ApplicationListener
```

Example 3 (unknown):
```unknown
@EventListener
```

Example 4 (unknown):
```unknown
ApplicationListener
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3546/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Leaking resources in an application is never a good idea, as it can lead to memory issues, and even the crash of the application. This rule template allows you to specify which constructions open a resource and how it is closed in order to raise issue within a method scope when custom resources are leaked.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6070/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

In regular expressions the escape sequence \cX, where the X stands for any character that’s either @, any capital ASCII letter, [, \, ], ^ or _, represents the control character that "corresponds" to the character following \c, meaning the control character that comes 64 bytes before the given character in the ASCII encoding.

In some other regex engines (for example in that of Perl) this escape sequence is case insensitive and \cd produces the same control character as \cD. Further using \c with a character that’s neither @, any ASCII letter, [, \, ], ^ nor _, will produce a warning or error in those engines. Neither of these things is true in Java, where the value of the character is always XORed with 64 without checking that this operation makes sense. Since this won’t lead to a sensible result for characters that are outside of the @ to _ range, using \c with such characters is almost certainly a mistake.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
Pattern.compile("\\ca"); // Noncompliant, 'a' is not an upper case letter
Pattern.compile("\\c!"); // Noncompliant, '!' is outside of the '@'-'_' range
```

Example 2 (unknown):
```unknown
Pattern.compile("\\cA"); // Compliant, this will match the "start of heading" control character
Pattern.compile("\\c^"); // Compliant, this will match the "record separator" control character
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-2677/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

The Reader.read() and the BufferedReader.readLine() are used for reading data from a data source. The return value of these methods is the data read from the data source, or null when the end of the data source is reached. If the return value is ignored, the data read from the source is thrown away and may indicate a bug.

This rule raises an issue when the return values of Reader.read() and BufferedReader.readLine() and their subclasses are ignored or merely null-checked.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
Reader.read()
```

Example 2 (unknown):
```unknown
BufferedReader.readLine()
```

Example 3 (unknown):
```unknown
Reader.read()
```

Example 4 (unknown):
```unknown
BufferedReader.readLine()
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3034/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

In Java, numeric promotions happen when two operands of an arithmetic expression have different sizes. More specifically, narrower operands get promoted to the type of wider operands. For instance, an operation between a byte and an int, will trigger a promotion of the byte operand, converting it into an int.

When this happens, the sequence of 8 bits that represents the byte will need to be extended to match the 32-bit long sequence that represents the int operand. Since Java uses two’s complement notation for signed number types, the promotion will fill the missing leading bits with zeros or ones, depending on the sign of the value. For instance, the byte 0b1000_0000 (equal to -128 in decimal notation), when promoted to int, will become 0b1111_1111_1111_1111_1111_1111_1000_0000.

When performing shifting or bitwise operations without considering that bytes are signed, the bits added during the promotion may have unexpected effects on the final result of the operations.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
0b1000_0000
```

Example 2 (unknown):
```unknown
0b1111_1111_1111_1111_1111_1111_1000_0000
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6915/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Java 21 adds new String.indexOf methods that accept ranges (beginIndex, to endIndex) rather than just a start index. A StringIndexOutOfBounds can be thrown when indicating an invalid range, namely when:

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
String.indexOf
```

Example 2 (unknown):
```unknown
StringIndexOutOfBounds
```

Example 3 (unknown):
```unknown
beginIndex > endIndex
```

Example 4 (unknown):
```unknown
beginIndex < 0
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6901/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

The Thread class has some methods that are used to monitor and manage its execution. With the introduction of virtual threads in Java 21, there are three of these methods that behave differently between the standard platform threads and the virtual ones.

This rule reports an issue when one of these methods is invoked on a virtual thread.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
Thread.setDaemon(boolean)
```

Example 2 (unknown):
```unknown
IllegalArgumentException
```

Example 3 (unknown):
```unknown
Thread.setPriority(int priority)
```

Example 4 (unknown):
```unknown
Thread.NORM_PRIORITY
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6218/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

In records, the default behavior of the equals() method is to check the equality by field values. This works well for primitive fields or fields, whose type overrides equals(), but this behavior doesn’t work as expected for array fields.

By default, array fields are compared by their reference, and overriding equals() is highly appreciated to achieve the deep equality check. The same strategy applies to hashCode() and toString() methods.

This rule reports an issue if a record class has an array field and is not overriding equals(), hashCode() or toString() methods.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
record Person(String[] names, int age) {} // Noncompliant
```

Example 2 (unknown):
```unknown
record Person(String[] names, int age) {
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return age == person.age && Arrays.equals(names, person.names);
    }

    @Override
    public int hashCode() {
        int result = Objects.hash(age);
        result = 31 * result + Arrays.hashCode(names);
        return result;
    }

    @Override
    public String toString() {
        return "Person{" +
                "names=" + Arrays.toString(names) +
                ", age=" + age +
                '}';
    }
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-2886/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

A synchronized method is a method marked with the synchronized keyword, meaning it can only be accessed by one thread at a time. If multiple threads try to access the synchronized method simultaneously, they will be blocked until the method is available.

Synchronized methods prevent race conditions and data inconsistencies in multi-threaded environments. Ensuring that only one thread can access a method at a time, prevents multiple threads from modifying the same data simultaneously, and causing conflicts.

When one part of a getter/setter pair is synchronized the other should be too. Failure to synchronize both sides may result in inconsistent behavior at runtime as callers access an inconsistent method state.

This rule raises an issue when either the method or the contents of one method in a getter/setter pair are synchronized, but the other is not.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
synchronized
```

Example 2 (unknown):
```unknown
synchronized
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6806/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Spring Expression Language (SpEL) is an expression language used in the Spring Framework for evaluating and manipulating objects, properties, and conditions within Spring-based applications.

org.springframework.ui.Model is an interface in the Spring Framework that represents a container for data that can be passed between a controller and a view in a Spring MVC web application, allowing for data sharing during the request-response cycle.

Attributes added to the org.springframework.ui.Model should follow the Java identifier naming convention, which means they must start with a letter a-z, A-Z, underscore _, or a dollar sign $ and may be followed by letters, digits, underscores, or dollar signs.

Failure to do so may result in SpEL parsing errors when using these attributes in template engines.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
org.springframework.ui.Model
```

Example 2 (unknown):
```unknown
org.springframework.ui.Model
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-2689/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

An ObjectOutputStream writes primitive data types and graphs of Java objects to an OutputStream. The objects can be read (reconstituted) using an ObjectInputStream.

When ObjectOutputStream is used with files opened in append mode, it can cause data corruption and unexpected behavior. This is because when ObjectOutputStream is created, it writes metadata to the output stream, which can conflict with the existing metadata when the file is opened in append mode. This can lead to errors and data loss.

When used with serialization, an ObjectOutputStream first writes the serialization stream header. This header should appear once per file at the beginning. When you’re trying to read your object(s) back from the file, only the first one will be read successfully, and a StreamCorruptedException will be thrown after that.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
ObjectOutputStream
```

Example 2 (unknown):
```unknown
OutputStream
```

Example 3 (unknown):
```unknown
ObjectInputStream
```

Example 4 (unknown):
```unknown
ObjectOutputStream
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3551/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

When @Overrides of synchronized methods are not themselves synchronized, the result can be improper synchronization as callers rely on the thread-safety promised by the parent class.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
synchronized
```

Example 2 (unknown):
```unknown
synchronized
```

Example 3 (csharp):
```csharp
public class Parent {

  synchronized void foo() {
    //...
  }
}

public class Child extends Parent {

 @Override
  public void foo () {  // Noncompliant
    // ...
    super.foo();
  }
}
```

Example 4 (csharp):
```csharp
public class Parent {

  synchronized void foo() {
    //...
  }
}

public class Child extends Parent {

  @Override
  synchronized void foo () {
    // ...
    super.foo();
  }
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6976/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Stream operations are divided into intermediate and terminal operations, and are combined to form stream pipelines. A stream should be operated on (invoking an intermediate or terminal stream operation) only once.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
Stream<Widget> pipeline = widgets.stream().filter(b -> b.getColor() == Color.RED);
var res1 = pipeline.findAny();
var res2 = pipeline.mapToInt(b -> b.getWeight()).sum(); // Noncompliant
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-4143/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Storing a value inside a collection at a given key or index and then unconditionally overwriting it without reading the initial value is a case of a "dead store".

This practice is redundant and will cause confusion for the reader. More importantly, it is often an error and not what the developer intended to do.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
letters.put("a", "Apple");
letters.put("a", "Boy");  // Noncompliant

towns[i] = "London";
towns[i] = "Chicago";  // Noncompliant
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5841/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

AssertJ assertions allMatch and doesNotContain on an empty list always returns true whatever the content of the predicate. Despite being correct, you should make explicit if you expect an empty list or not, by adding isEmpty()/isNotEmpty() in addition to calling the assertion, or by testing the list’s content further. It will justify the useless predicate to improve clarity or increase the reliability of the test.

This rule raises an issue when any of the methods listed are used without asserting that the list is empty or not and without testing the content.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
doesNotContain
```

Example 2 (unknown):
```unknown
isNotEmpty()
```

Example 3 (unknown):
```unknown
doesNotContain
```

Example 4 (unknown):
```unknown
doesNotContainSequence
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3020/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

The Collection.toArray() method returns an Object[] when no arguments are provided to it. This can lead to a ClassCastException at runtime if you try to cast the returned array to an array of a specific type. Instead, use this method by providing an array of the desired type as the argument.

Note that passing a new T[0] array of length zero as the argument is more efficient than a pre-sized array new T[size].

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
Collection.toArray()
```

Example 2 (unknown):
```unknown
ClassCastException
```

Example 3 (unknown):
```unknown
new
T[size]
```

Example 4 (unknown):
```unknown
public String [] getStringArray(List<String> strings) {
  return (String []) strings.toArray();  // Noncompliant, a ClassCastException will be thrown here
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6838/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Spring proxies are based on the Proxy design pattern and serve as intermediaries to other resources, offering extra features at a slight performance penalty. For example, they facilitate lazy resource initialization and data caching.

The @Configuration annotation enables this mechanism by default through the proxyBeanMethods attribute set to true. This ensures that the @Bean methods are proxied in order to enforce bean lifecycle behavior, e.g. to return shared singleton bean instances even in case of direct @Bean method calls in user code. This functionality is achieved via method interception, implemented through a runtime-generated CGLIB subclass.

When setting the proxyBeanMethods attribute to false the @Bean methods are not proxied and this is similar to removing the @Configuration stereotype. In this scenario, @Bean methods within the @Configuration annotated class operate in lite mode, resulting in a new bean creation each time the method is invoked.

For Singleton beans, this could cause unexpected outcomes as the bean is created multiple times instead of being created once and cached.

The rule raises an issue when the proxyBeanMethods attribute is set to false and the @Bean method of a Singleton bean is directly invoked in the @Configuration annotated class code.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
@Configuration
```

Example 2 (unknown):
```unknown
proxyBeanMethods
```

Example 3 (unknown):
```unknown
proxyBeanMethods
```

Example 4 (unknown):
```unknown
@Configuration
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-2885/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

When an object is marked as static, it means that it belongs to the class rather than any class instance. This means there is only one copy of the static object in memory, regardless of how many class instances are created. Static objects are shared among all instances of the class and can be accessed using the class name rather than an instance of the class.

A data type is considered thread-safe if it can be used correctly by multiple threads, regardless of how those threads are executed, without requiring additional coordination from the calling code. In other words, a thread-safe data type can be accessed and modified by multiple threads simultaneously without causing any issues or requiring extra work from the programmer to ensure correct behavior.

Non-thread-safe objects are objects that are not designed to be used in a multi-threaded environment and can lead to race conditions and data inconsistencies when accessed by multiple threads simultaneously. Using them in a multi-threaded manner is highly likely to cause data problems or exceptions at runtime.

When a non-thread-safe object is marked as static in a multi-threaded environment, it can cause issues because the non-thread-safe object will be shared across different instances of the containing class.

This rule raises an issue when any of the following instances and their subtypes are marked as static:

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
java.util.Calendar
```

Example 2 (unknown):
```unknown
java.text.DateFormat
```

Example 3 (unknown):
```unknown
javax.xml.xpath.XPath
```

Example 4 (unknown):
```unknown
javax.xml.validation.SchemaFactory
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6831/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

In Spring Framework, the @Qualifier annotation is typically used to disambiguate between multiple beans of the same type when auto-wiring dependencies. It is not necessary to use @Qualifier when defining a bean using the @Bean annotation because the bean’s name can be explicitly specified using the name attribute or derived from the method name. Using @Qualifier on @Bean methods can lead to confusion and redundancy. Beans should be named appropriately using either the name attribute of the @Bean annotation or the method name itself.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (csharp):
```csharp
@Configuration
public class MyConfiguration {
  @Bean
  @Qualifier("myService")
  public MyService myService() {
    // ...
    return new MyService();
  }

  @Bean
  @Qualifier("betterService")
  public MyService aBetterService() {
    // ...
    return new MyService();
  }

  @Bean
  @Qualifier("evenBetterService")
  public MyService anEvenBetterService() {
    // ...
    return new MyService();
  }

  @Bean
  @Qualifier("differentService")
  public MyBean aDifferentService() {
    // ...
    return new MyBean();
  }
}
```

Example 2 (csharp):
```csharp
@Configuration
public class MyConfiguration {
  @Bean
  public MyService myService() {
    // ...
    return new MyService();
  }

  @Bean(name="betterService")
  public MyService aBetterService() {
    // ...
    return new MyService();
  }

  @Bean(name="evenBetterService")
  public MyService anEvenBetterService() {
    // ...
    return new MyService();
  }

  @Bean(name="differentService")
  public MyBean aDifferentService() {
    // ...
    return new MyBean();
  }
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3959/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Stream operations are divided into intermediate and terminal operations, and are combined to form stream pipelines. After the terminal operation is performed, the stream pipeline is considered consumed, and cannot be used again. Such a reuse will yield unexpected results.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
Stream<Widget> pipeline = widgets.stream().filter(b -> b.getColor() == RED);
int sum1 = pipeline.sum();
int sum2 = pipeline.mapToInt(b -> b.getWeight()).sum(); // Noncompliant
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3032/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Using the standard getClassLoader() may not return the right class loader in a JEE context. Instead, go through the currentThread.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
getClassLoader()
```

Example 2 (unknown):
```unknown
currentThread
```

Example 3 (unknown):
```unknown
ClassLoader cl = this.getClass().getClassLoader();  // Noncompliant
```

Example 4 (unknown):
```unknown
ClassLoader cl = Thread.currentThread().getContextClassLoader();
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5866/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

By default case insensitivity only affects letters in the ASCII range. This can be changed by either passing Pattern.UNICODE_CASE or Pattern.UNICODE_CHARACTER_CLASS as an argument to Pattern.compile or using (?u) or (?U) within the regex.

If not done, regular expressions involving non-ASCII letters will still handle those letters as being case sensitive.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
Pattern.UNICODE_CASE
```

Example 2 (unknown):
```unknown
Pattern.UNICODE_CHARACTER_CLASS
```

Example 3 (unknown):
```unknown
Pattern.compile
```

Example 4 (unknown):
```unknown
Pattern.compile("söme pättern", Pattern.CASE_INSENSITIVE);
str.matches("(?i)söme pättern");
str.matches("(?i:söme) pättern");
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5868/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

When placing Unicode Grapheme Clusters (characters which require to be encoded in multiple Code Points) inside a character class of a regular expression, this will likely lead to unintended behavior.

For instance, the grapheme cluster c̈ requires two code points: one for 'c', followed by one for the umlaut modifier '\u{0308}'. If placed within a character class, such as [c̈], the regex will consider the character class being the enumeration [c\u{0308}] instead. It will, therefore, match every 'c' and every umlaut that isn’t expressed as a single codepoint, which is extremely unlikely to be the intended behavior.

This rule raises an issue every time Unicode Grapheme Clusters are used within a character class of a regular expression.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
[c\u{0308}]
```

Example 2 (unknown):
```unknown
"cc̈d̈d".replaceAll("[c̈d̈]", "X"); // Noncompliant, print "XXXXXX" instead of expected "cXXd".
```

Example 3 (unknown):
```unknown
"cc̈d̈d".replaceAll("c̈|d̈", "X"); // print "cXXd"
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6862/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Naming conventions play a crucial role in maintaining code clarity and readability. The uniqueness of bean names in Spring configurations is vital to the clarity and readability of the code. When two beans share the same name within a configuration, it is not obvious to the reader which bean is being referred to. This leads to potential misunderstandings and errors.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3986/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Few developers are aware of the difference between Y for "Week year" and y for Year when formatting and parsing a date with SimpleDateFormat or DateTimeFormatter. That’s likely because for most dates, Week year and Year are the same, so testing at any time other than the first or last week of the year will yield the same value for both y and Y. But in the last week of December and the first week of January, you may get unexpected results.

According to the Javadoc:

A week year is in sync with a WEEK_OF_YEAR cycle. All weeks between the first and last weeks (inclusive) have the same week year value. Therefore, the first and last days of a week year may have different calendar year values.

For example, January 1, 1998 is a Thursday. If getFirstDayOfWeek() is MONDAY and getMinimalDaysInFirstWeek() is 4 (ISO 8601 standard compatible setting), then week 1 of 1998 starts on December 29, 1997, and ends on January 4, 1998. The week year is 1998 for the last three days of calendar year 1997. If, however, getFirstDayOfWeek() is SUNDAY, then week 1 of 1998 starts on January 4, 1998, and ends on January 10, 1998; the first three days of 1998 then are part of week 53 of 1997 and their week year is 1997.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
SimpleDateFormat
```

Example 2 (unknown):
```unknown
DateTimeFormatter
```

Example 3 (unknown):
```unknown
Date date = new SimpleDateFormat("yyyy/MM/dd").parse("2015/12/31");
String result = new SimpleDateFormat("YYYY/MM/dd").format(date);   //Noncompliant; yields '2016/12/31'
result = DateTimeFormatter.ofPattern("YYYY/MM/dd").format(date); //Noncompliant; yields '2016/12/31'
```

Example 4 (unknown):
```unknown
Date date = new SimpleDateFormat("yyyy/MM/dd").parse("2015/12/31");
String result = new SimpleDateFormat("yyyy/MM/dd").format(date);   //Yields '2015/12/31' as expected
result = DateTimeFormatter.ofPattern("yyyy/MM/dd").format(date); //Yields '2015/12/31' as expected
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3046/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

When two locks are held simultaneously, a wait call only releases one of them. The other will be held until some other thread requests a lock on the awaited object. If no unrelated code tries to lock on that object, then all other threads will be locked out, resulting in a deadlock.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
synchronized (this.mon1) {  // threadB can't enter this block to request this.mon2 lock & release threadA
	synchronized (this.mon2) {
		this.mon2.wait();  // Noncompliant; threadA is stuck here holding lock on this.mon1
	}
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6002/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

This rule raises an issue when a regex lookahead contradicts the rest of the regex.

Lookahead assertions are a regex feature that makes it possible to look ahead in the input without consuming it. It is often used at the end of regular expressions to make sure that substrings only match when they are followed by a specific pattern.

For example, the following pattern will match an "a" only if it is directly followed by a "b". This does not consume the "b" in the process:

However, lookaheads can also be used in the middle (or at the beginning) of a regex. In that case there is the possibility that what comes after the lookahead contradicts the pattern inside the lookahead. Since the lookahead does not consume input, this makes the lookahead impossible to match and is a sign that there’s a mistake in the regular expression that should be fixed.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
Pattern.compile("a(?=b)");
```

Example 2 (unknown):
```unknown
Pattern.compile("(?=a)b"); // Noncompliant, the same character can't be equal to 'a' and 'b' at the same time
```

Example 3 (unknown):
```unknown
Pattern.compile("(?<=a)b");
Pattern.compile("a(?=b)");
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5917/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

When creating a DateTimeFormatter using the WeekFields.weekBasedYear() temporal field, the resulting year number may be off by 1 at the beginning of a new year (when the date to format is in a week that is shared by two consecutive years).

Using this year number in combination with an incompatible week temporal field yields a result that may be confused with the first week of the previous year.

Instead, when paired with a week temporal field, the week-based year should only be used with the week of week-based year temporal field WeekFields.weekOfWeekBasedYear().

Alternatively the temporal field ChronoField.ALIGNED_WEEK_OF_YEAR can be used together with a regular year (but not the week based year).

Here the first two formatters would wrongly format the 1st of January 2016 as "2016-53" while the last one would format it as "2015-01"

Here the first formatter would format the 1st of January 2016 as "2015-53" while the last two would produce "2016-01", both of which are correct depending on how you count the weeks.

No issue is raised when week-based year is not used in combination with a week temporal field.

Similarly, no issue is raised if week of week-based year is not used in combination with a year temporal field.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
DateTimeFormatter
```

Example 2 (unknown):
```unknown
WeekFields.weekBasedYear()
```

Example 3 (unknown):
```unknown
WeekFields.weekOfWeekBasedYear()
```

Example 4 (unknown):
```unknown
ChronoField.ALIGNED_WEEK_OF_YEAR
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6810/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

The Spring framework provides the annotation Async to mark a method (or all methods of a type) as a candidate for asynchronous execution.

Asynchronous methods do not necessarily, by their nature, return the result of their calculation immediately. Hence, it is unexpected and in clear breach of the Async contract for such methods to have a return type that is neither void nor a Future type.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6103/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

AssertJ assertions taking Consumer objects as arguments are expected to contain "requirements", which should themselves be expressed as assertions. This concerns the following methods: allSatisfy, anySatisfy, hasOnlyOneElementSatisfying, isInstanceOfSatisfying, noneSatisfy, satisfies, satisfiesAnyOf, zipSatisfy.

These methods are assuming the Consumer will do the assertions itself. If you do not do any assertion in the Consumer, it probably means that you are inadvertently only partially testing your object.

This rule raises an issue when a Consumer argument of any of the above methods does not contain any assertion.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
assertThat(myObject).isInstanceOfSatisfying(String.class, s -> "Hello".equals(s)); // Noncompliant - not testing the string value
assertThat(myObject).satisfies("Hello"::equals); // Noncompliant - not testing the string value
```

Example 2 (unknown):
```unknown
assertThat(myObject).isInstanceOfSatisfying(String.class, s -> assertThat(s).isEqualTo("Hello"));
assertThat(myObject).satisfies(obj -> assertThat(obj).isEqualTo("Hello"));
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6466/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

An array index out-of-bounds exception is a bug class that occurs in Java when a program tries to access an array element that does not exist. This bug can cause your program to crash or behave unexpectedly. To fix an array index out of bounds exception in Java, you should always ensure that you are accessing array elements within the bounds of the array.

An array index out-of-bounds exception indicates a bug or a logical error in the code.

In Java, arrays have a fixed size, and their elements are indexed starting from 0, counting up to the last index that is still smaller than the size. When trying to access an array outside of this range, an ArrayIndexOutOfBoundsException will be thrown and the operation will fail.

Issues of this type interrupt the normal execution of a program, causing it to crash or putting it into an inconsistent state. Therefore, this issue might impact the availability and reliability of your application, or even result in data loss.

If the computation of an index value is tied to user input data, this issue can potentially even be exploited by attackers to disrupt your application.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
ArrayIndexOutOfBoundsException
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3067/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

getClass should not be used for synchronization in non-final classes because child classes will synchronize on a different object than the parent or each other, allowing multiple threads into the code block at once, despite the synchronized keyword.

Instead, hard code the name of the class on which to synchronize or make the class final.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
synchronized
```

Example 2 (csharp):
```csharp
public class MyClass {
  public void doSomethingSynchronized(){
    synchronized (this.getClass()) {  // Noncompliant
      // ...
    }
  }
```

Example 3 (csharp):
```csharp
public class MyClass {
  public void doSomethingSynchronized(){
    synchronized (MyClass.class) {
      // ...
    }
  }
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6863/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

The request handler function in a Controller should set the appropriate HTTP status code based on the operation’s success or failure. This is done by returning a Response object with the appropriate status code.

If an exception is thrown during the execution of the handler, the status code should be in the range of 4xx or 5xx. Examples of such codes are BAD_REQUEST, UNAUTHORIZED, FORBIDDEN, NOT_FOUND, INTERNAL_SERVER_ERROR, BAD_GATEWAY, SERVICE_UNAVAILABLE, etc.

The status code should be 1xx, 2xx, or 3xx if no exception is thrown and the operation is considered successful. Such codes include OK, CREATED, MOVED_PERMANENTLY, FOUND, etc.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
BAD_REQUEST
```

Example 2 (unknown):
```unknown
UNAUTHORIZED
```

Example 3 (unknown):
```unknown
INTERNAL_SERVER_ERROR
```

Example 4 (unknown):
```unknown
BAD_GATEWAY
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5856/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Regular expressions have their own syntax that is understood by regular expression engines. Those engines will throw an exception at runtime if they are given a regular expression that does not conform to that syntax.

To avoid syntax errors, special characters should be escaped with backslashes when they are intended to be matched literally and references to capturing groups should use the correctly spelled name or number of the group.

To match a literal string instead of a regular expression, either all special characters should be escaped, the Pattern.LITERAL flag or methods that don’t use regular expressions should be used.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
Pattern.LITERAL
```

Example 2 (unknown):
```unknown
Pattern.compile("([");
str.matches("([");
str.replaceAll("([", "{");
str.matches("(\\w+-(\\d+)");
```

Example 3 (unknown):
```unknown
Pattern.compile("\\(\\[");
Pattern.compile("([", Pattern.LITERAL);
str.equals("([");
str.replace("([", "{");
str.matches("(\\w+)-(\\d+)");
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6913/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Java 21 introduces the new method Math.clamp(value, min, max) that fits a value within a specified interval. Before Java 21, this behavior required explicit calls to the Math.min and Math.max methods, as in Math.min(max, Math.max(value, min)).

If min > max, Math.clamp throws an IllegalArgumentException, indicating an invalid interval. This can occur if the min and max arguments are mistakenly reversed.

Note that Math.clamp is not a general substitute for Math.min or Math.max, but for the combination of both. If value is the same as min or max, using Math.clamp is unnecessary and Math.min or Math.max should be used instead.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
Math.clamp(value, min, max)
```

Example 2 (unknown):
```unknown
Math.min(max, Math.max(value,
min))
```

Example 3 (unknown):
```unknown
IllegalArgumentException
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3958/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

There are two types of stream operations: intermediate operations, which return another stream, and terminal operations, which return something other than a stream. Intermediate operations are lazy, meaning they aren’t actually executed until and unless a terminal stream operation is performed on their results. Consequently, if the result of an intermediate stream operation is not fed to a terminal operation, it serves no purpose, which is almost certainly an error.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
widgets.stream().filter(b -> b.getColor() == RED); // Noncompliant
```

Example 2 (unknown):
```unknown
int sum = widgets.stream()
                      .filter(b -> b.getColor() == RED)
                      .mapToInt(b -> b.getWeight())
                      .sum();
Stream<Widget> pipeline = widgets.stream()
                                 .filter(b -> b.getColor() == GREEN)
                                 .mapToInt(b -> b.getWeight());
sum = pipeline.sum();
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-4275/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Getters and setters provide a way to enforce encapsulation by providing public methods that give controlled access to private fields. However, in classes with multiple fields, it is not unusual that copy and paste is used to quickly create the needed getters and setters, which can result in the wrong field being accessed by a getter or setter.

This rule raises an issue in any of these cases:

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
class A {
  private int x;
  private int y;

  public void setX(int val) { // Noncompliant: field 'x' is not updated
    this.y = val;
  }

  public int getY() { // Noncompliant: field 'y' is not used in the return value
    return this.x;
  }
}
```

Example 2 (unknown):
```unknown
class A {
  private int x;
  private int y;

  public void setX(int val) {
    this.x = val;
  }

  public int getY() {
    return this.y;
  }
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3984/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Creating a new Throwable without actually throwing it is useless and is probably due to a mistake.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
if (x < 0)
  new IllegalArgumentException("x must be nonnegative");
```

Example 2 (unknown):
```unknown
if (x < 0)
  throw new IllegalArgumentException("x must be nonnegative");
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3306/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Field injection seems like a tidy way to get your classes what they need to do their jobs, but it’s really a NullPointerException waiting to happen unless all your class constructors are private. That’s because any class instances that are constructed by callers, rather than instantiated by a Dependency Injection framework compliant with the JSR-330 (Spring, Guice, …​), won’t have the ability to perform the field injection.

Instead @Inject should be moved to the constructor and the fields required as constructor parameters.

This rule raises an issue when classes with non-private constructors (including the default constructor) use field injection.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
NullPointerException
```

Example 2 (unknown):
```unknown
class MyComponent {  // Anyone can call the default constructor

  @Inject MyCollaborator collaborator;  // Noncompliant

  public void myBusinessMethod() {
    collaborator.doSomething();  // this will fail in classes new-ed by a caller
  }
}
```

Example 3 (unknown):
```unknown
class MyComponent {

  private final MyCollaborator collaborator;

  @Inject
  public MyComponent(MyCollaborator collaborator) {
    Assert.notNull(collaborator, "MyCollaborator must not be null!");
    this.collaborator = collaborator;
  }

  public void myBusinessMethod() {
    collaborator.doSomething();
  }
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6209/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

In Records, serialization is not done the same way as for ordinary serializable or externalizable classes. The serialized representation of a record object will be a sequence of values (record components). During the deserialization of records, the stream of components is read and components are constructed. Then the record object is recreated by invoking the record’s canonical constructor with the component values serving as arguments (or default values for absent arguments).

This process cannot be customized, so any class-specific writeObject, readObject, readObjectNoData, writeExternal, and readExternal methods or serialPersistentFields fields in record classes are ignored during serialization and deserialization.

However, there is a way to substitute serialized/deserialized objects in writeReplace and readResolve.

This rule raises an issue when any of writeObject, readObject, readObjectNoData, writeExternal, readExternal or serialPersistentFields are present as members in a Record class.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
writeObject
```

Example 2 (unknown):
```unknown
readObjectNoData
```

Example 3 (unknown):
```unknown
writeExternal
```

Example 4 (unknown):
```unknown
readExternal
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5845/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Assertions comparing incompatible types always fail, and negative assertions always pass. At best, negative assertions are useless. At worst, the developer loses time trying to fix his code logic before noticing wrong assertions.

Dissimilar types are:

This rule also raises issues for unrelated class and interface or unrelated interface types in negative assertions. Because except in some corner cases, those types are more likely to be dissimilar. And inside a negative assertion, there is no test failure to inform the developer about this unusual comparison.

Supported test frameworks:

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
interface KitchenTool {}
interface Plant {}
class Spatula implements KitchenTool {}
class Tree implements Plant {}

void assertValues(int size,
                  Spatula spatula, KitchenTool tool,  KitchenTool[] tools,
                  Tree    tree,    Plant       plant, Tree[]        trees) {

  // Whatever the given values, those negative assertions will always pass due to dissimilar types:
  assertThat(size).isNotNull();           // Noncompliant; primitives can not be null
  assertThat(spatula).isNotEqualTo(tree); // Noncompliant; unrelated classes
  assertThat(tool).isNotSameAs(tools);    // Noncompliant; array & non-array
  assertThat(trees).isNotEqualTo(tools);  // Noncompliant; incompatible arrays

  // Those assertions will always fail
  assertThat(size).isNull();                       // Noncompliant
  assertThat(spatula).isEqualTo(tree);             // Noncompliant

  // Those negative assertions are more likely to always pass
  assertThat(spatula).isNotEqualTo(plant); // Noncompliant; unrelated class and interface
  assertThat(tool).isNotEqualTo(plant);    // Noncompliant; unrelated interfaces
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3077/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Marking an array volatile means that the array itself will always be read fresh and never thread cached, but the items in the array will not be. Similarly, marking a mutable object field volatile means the object reference is volatile but the object itself is not, and other threads may not see updates to the object state.

This can be salvaged with arrays by using the relevant AtomicArray class, such as AtomicIntegerArray, instead. For mutable objects, the volatile should be removed, and some other method should be used to ensure thread-safety, such as synchronization, or ThreadLocal storage.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
AtomicIntegerArray
```

Example 2 (unknown):
```unknown
private volatile int [] vInts;  // Noncompliant
private volatile MyObj myObj;  // Noncompliant
```

Example 3 (unknown):
```unknown
private AtomicIntegerArray vInts;
private MyObj myObj;
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-2757/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Using operator pairs (=+, =-, or =!) that look like reversed single operators (+=, -= or !=) is confusing. They compile and run but do not produce the same result as their mirrored counterpart.

This rule raises an issue when =+, =-, or =! are used without any space between the operators and when there is at least one whitespace after.

Replace the operators with a single one if that is the intention

Or fix the spacing to avoid confusion

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
int target = -5;
int num = 3;

target =- num;  // Noncompliant: target = -3. Is that the intended behavior?
target =+ num; // Noncompliant: target = 3
```

Example 2 (unknown):
```unknown
int target = -5;
int num = 3;

target -= num;  // target = -8
```

Example 3 (unknown):
```unknown
int target = -5;
int num = 3;

target = -num;  // target = -3
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3753/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

A Spring @Controller that uses @SessionAttributes is designed to handle a stateful / multi-post form. Such @Controllers use the specified @SessionAttributes to store data on the server between requests. That data should be cleaned up when the session is over, but unless setComplete() is called on the SessionStatus object from a @RequestMapping method, neither Spring nor the JVM will know it’s time to do that. Note that the SessionStatus object must be passed to that method as a parameter.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
@Controller
```

Example 2 (unknown):
```unknown
@SessionAttributes
```

Example 3 (unknown):
```unknown
@Controller
```

Example 4 (unknown):
```unknown
@SessionAttributes
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3599/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Because Double Brace Initialization (DBI) creates an anonymous class with a reference to the instance of the owning object, its use can lead to memory leaks if the anonymous inner class is returned and held by other objects. Even when there’s no leak, DBI is so obscure that it’s bound to confuse most maintainers.

For collections, use Arrays.asList instead, or explicitly add each item directly to the collection.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
Arrays.asList
```

Example 2 (unknown):
```unknown
Map source = new HashMap(){{ // Noncompliant
    put("firstName", "John");
    put("lastName", "Smith");
}};
```

Example 3 (unknown):
```unknown
Map source = new HashMap();
// ...
source.put("firstName", "John");
source.put("lastName", "Smith");
// ...
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-2676/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

This rule involves the use of Math.abs and negation on numbers that could be MIN_VALUE. It is a problem because it can lead to incorrect results and unexpected behavior in the program.

When Math.abs and negation are used on numbers that could be MIN_VALUE, the result can be incorrect due to integer overflow. Common methods that can return a MIN_VALUE and raise an issue when used together with Math.abs are:

Alternatively, the absExact() method throws an ArithmeticException for MIN_VALUE.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
Random.nextInt()
```

Example 2 (unknown):
```unknown
Random.nextLong()
```

Example 3 (unknown):
```unknown
compareTo()
```

Example 4 (unknown):
```unknown
ArithmeticException
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-4602/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

@ComponentScan is used to determine which Spring Beans are available in the application context. The packages to scan can be configured thanks to the basePackageClasses or basePackages (or its alias value) parameters. If neither parameter is configured, @ComponentScan will consider only the package of the class annotated with it. When @ComponentScan is used on a class belonging to the default package, the entire classpath will be scanned.

This will slow-down the start-up of the application and it is likely the application will fail to start with an BeanDefinitionStoreException because you ended up scanning the Spring Framework package itself.

This rule raises an issue when:

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
@ComponentScan
```

Example 2 (unknown):
```unknown
basePackageClasses
```

Example 3 (unknown):
```unknown
basePackages
```

Example 4 (unknown):
```unknown
@ComponentScan
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5998/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

The Java regex engine uses recursive method calls to implement backtracking. Therefore when a repetition inside a regular expression contains multiple paths (i.e. the body of the repetition contains an alternation (|), an optional element or another repetition), trying to match the regular expression can cause a stack overflow on large inputs. This does not happen when using a possessive quantifier (such as *+ instead of *) or when using a character class inside a repetition (e.g. [ab]* instead of (a|b)*).

The size of the input required to overflow the stack depends on various factors, including of course the stack size of the JVM. One thing that significantly increases the size of the input that can be processed is if each iteration of the repetition goes through a chain of multiple constant characters because such consecutive characters will be matched by the regex engine without invoking any recursion.

For example, on a JVM with a stack size of 1MB, the regex (?:a|b)* will overflow the stack after matching around 6000 characters (actual numbers may differ between JVM versions and even across multiple runs on the same JVM) whereas (?:abc|def)* can handle around 15000 characters.

Since often times stack growth can’t easily be avoided, this rule will only report issues on regular expressions if they can cause a stack overflow on realistically sized inputs. You can adjust the maxStackConsumptionFactor parameter to adjust this.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
(?:abc|def)*
```

Example 2 (unknown):
```unknown
maxStackConsumptionFactor
```

Example 3 (unknown):
```unknown
Pattern.compile("(a|b)*"); // Noncompliant
Pattern.compile("(.|\n)*"); // Noncompliant
Pattern.compile("(ab?)*"); // Noncompliant
```

Example 4 (unknown):
```unknown
Pattern.compile("[ab]*"); // Character classes don't cause recursion the way that '|' does
Pattern.compile("(?s).*"); // Enabling the (?s) flag makes '.' match line breaks, so '|\n' isn't necessary
Pattern.compile("(ab?)*+"); // Possessive quantifiers don't cause recursion because they disable backtracking
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5960/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Assertions are intended to be used in test code, but not in production code. It is confusing, and might lead to ClassNotFoundException when the build tools only provide the required dependency in test scope.

In addition, assertions will throw a sub-class of Error: AssertionError, which should be avoided in production code.

This rule raises an issue when any assertion intended to be used in test is used in production code.

Supported frameworks:

Note: this does not apply for assert from Java itself or if the source code package name is related to tests (contains: test or assert or junit).

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
ClassNotFoundException
```

Example 2 (unknown):
```unknown
AssertionError
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3039/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

There are various String operations that take one or more character indexes as arguments and return a portion of the original string. Indexing in this context is zero-based, meaning that the first character’s index is 0. As a result, given a string myString, its last character is at index myString.length() - 1.

The String operation methods throw a StringIndexOutOfBoundsException when one of their index argument is smaller than 0 (E.G.: -1). String::substring also throws this exception when the beginIndex or endIndex argument is larger than myString.length(), and String::charAt when the index argument is larger than myString.length() - 1 For instance, it is not possible to use String::charAt to retrieve a value before the start or after the end of a string. Furthermore, it is not possible to use String::substring with beginIndex > endIndex to reverse the order of characters in a string.

This rule raises an issue when a negative literal or an index that is too large is passed as an argument to the String::substring, String::charAt, and related methods. It also raises an issue when the start index passed to String::substring is larger than the end index.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
myString.length() - 1
```

Example 2 (unknown):
```unknown
StringIndexOutOfBoundsException
```

Example 3 (unknown):
```unknown
String::substring
```

Example 4 (unknown):
```unknown
myString.length()
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5855/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

This rule raises an issue when multiple branches of a regex alternative match the same input.

If an alternative in a regular expression only matches things that are already matched by another alternative, that alternative is redundant and serves no purpose.

In the best case this means that the offending subpattern is merely redundant and should be removed. In the worst case it’s a sign that this regex does not match what it was intended to match and should be reworked.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
"[ab]|a"   // Noncompliant: the "|a" is redundant because "[ab]" already matches "a"
".*|a"     // Noncompliant: .* matches everything, so any other alternative is redundant
```

Example 2 (unknown):
```unknown
"[ab]"
".*"
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-4351/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

When implementing the Comparable<T>.compareTo method, the parameter’s type has to match the type used in the Comparable declaration. When a different type is used this creates an overload instead of an override, which is unlikely to be the intent.

This rule raises an issue when the parameter of the compareTo method of a class implementing Comparable<T> is not same as the one used in the Comparable declaration.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
Comparable<T>.compareTo
```

Example 2 (unknown):
```unknown
Comparable<T>
```

Example 3 (csharp):
```csharp
public class Foo {
  static class Bar implements Comparable<Bar> {
    public int compareTo(Bar rhs) {
      return -1;
    }
  }

  static class FooBar extends Bar {
    public int compareTo(FooBar rhs) {  // Noncompliant: Parameter should be of type Bar
      return 0;
    }
  }
}
```

Example 4 (csharp):
```csharp
public class Foo {
  static class Bar implements Comparable<Bar> {
    public int compareTo(Bar rhs) {
      return -1;
    }
  }

  static class FooBar extends Bar {
    public int compareTo(Bar rhs) {
      return 0;
    }
  }
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-2695/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

PreparedStatement is an object that represents a precompiled SQL statement, that can be used to execute the statement multiple times efficiently.

ResultSet is the Java representation of the result set of a database query obtained from a Statement object. A default ResultSet object is not updatable and has a cursor that moves forward only.

The parameters in PreparedStatement and ResultSet are indexed beginning at 1, not 0. When an invalid index is passed to the PreparedStatement or ResultSet methods, an IndexOutOfBoundsException is thrown. This can cause the program to crash or behave unexpectedly, leading to a poor user experience.

This rule raises an issue for the get methods in PreparedStatement and the set methods in ResultSet.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
PreparedStatement
```

Example 2 (unknown):
```unknown
PreparedStatement
```

Example 3 (unknown):
```unknown
PreparedStatement
```

Example 4 (unknown):
```unknown
IndexOutOfBoundsException
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3981/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

The size of a collection and the length of an array are always greater than or equal to zero. Testing it doesn’t make sense, since the result is always true.

Similarly testing that it is less than zero will always return false.

Fix the code to properly check for emptiness if it was the intent, or remove the redundant code to keep the current behavior.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
if (myList.size() >= 0) {...} // Noncompliant: always true

boolean result = myArray.length >= 0; // Noncompliant: true
```

Example 2 (unknown):
```unknown
if (myList.size() < 0) {...} // Noncompliant: always false
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6104/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Map computeIfAbsent and computeIfPresent methods are convenient to avoid the cumbersome process to check if a key exists or not, followed by the addition of the entry. However, when the function used to compute the value returns null, the entry key->null will not be added to the Map. Furthermore, in the case of computeIfPresent, if the key is present the entry will be removed. These methods should therefore not be used to conditionally add an entry with a null value. The traditional way should be used instead.

This rule raises an issue when computeIfAbsent or computeIfPresent is used with a lambda always returning null.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
computeIfPresent
```

Example 2 (unknown):
```unknown
computeIfAbsent
```

Example 3 (unknown):
```unknown
computeIfPresent
```

Example 4 (unknown):
```unknown
map.computeIfAbsent(key, k -> null); // Noncompliant, the map will not contain an entry key->null.
map.computeIfPresent(key, (k, oldValue) -> null); // Noncompliant
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3923/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Having all branches of a switch or if chain with the same implementation indicates a problem.

In the following code:

Either there is a copy-paste error that needs fixing or an unnecessary switch or if chain that should be removed.

This rule does not apply to if chains without else, nor to switch without a default clause.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
if (b == 0) {  // Noncompliant
  doOneMoreThing();
} else {
  doOneMoreThing();
}

int b = a > 12 ? 4 : 4;  // Noncompliant

switch (i) {  // Noncompliant
  case 1:
    doSomething();
    break;
  case 2:
    doSomething();
    break;
  case 3:
    doSomething();
    break;
  default:
    doSomething();
}
```

Example 2 (unknown):
```unknown
if(b == 0) {    //no issue, this could have been done on purpose to make the code more readable
  doSomething();
} else if(b == 1) {
  doSomething();
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3750/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Spring @Controllers, @Services, and @Repositorys have singleton scope by default, meaning only one instance of the class is ever instantiated in the application. Defining any other scope for one of these class types will result in needless churn as new instances are created and destroyed. In a busy web application, this could cause a significant amount of needless additional load on the server.

This rule raises an issue when the @Scope annotation is applied to a @Controller, @Service, or @Repository with any value but "singleton". @Scope("singleton") is redundant, but ignored.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
@Controller
```

Example 2 (unknown):
```unknown
@Repository
```

Example 3 (unknown):
```unknown
@Controller
```

Example 4 (unknown):
```unknown
@Repository
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-2761/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

The repetition of a unary operator is usually a typo. The second operator invalidates the first one in most cases:

On the other hand, while repeating the increment and decrement operators is technically correct, it obfuscates the meaning:

Using += or -= improves readability:

This rule raises an issue for repetitions of !, ~, -, +, prefix increments ++ and prefix decrements --.

Overflow handling for GWT compilation using ~~ is ignored.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
int i = 1;

int j = - - -i;  // Noncompliant: equivalent to "-i"
int k = ~~~i;    // Noncompliant: equivalent to "~i"
int m = + +i;    // Noncompliant: equivalent to "i"

boolean b = false;
boolean c = !!!b;   // Noncompliant
```

Example 2 (unknown):
```unknown
int i = 1;
int j = ++ ++i;  // Noncompliant
int k = i-- --; // Noncompliant
```

Example 3 (unknown):
```unknown
int i = 1;
i += 2;
int j = i;
int k = i;
i -=2;
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6881/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

With the introduction of virtual threads in Java 21, it is now possible to optimize the usage of the operating system threads by avoiding blocking them for asynchronous operations. Furthermore, virtual threads’s instantiation has very little overhead and they can be created in large quantities. This means that it can be more efficient to use them over the default platform threads for tasks that involve I/O or some other blocking operations.

Whenever a virtual thread is started, the JVM will mount it on an OS thread. As soon as the virtual thread runs into a blocking operation like an HTTP request or a filesystem read/write operation, the JVM will detect this and unmount the virtual thread. This allows another virtual thread to take over the OS thread and continue its execution.

This is why virtual threads should be preferred to platform threads for tasks that involve blocking operations. By default, a Java thread is a platform thread. To use a virtual thread it must be started either with Thread.startVirtualThread(Runnable) or Thread.ofVirtual().start(Runnable).

This rule raises an issue when a platform thread is created with a task that includes heavy blocking operations.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
Thread.startVirtualThread(Runnable)
```

Example 2 (unknown):
```unknown
Thread.ofVirtual().start(Runnable)
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6857/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

This rule reports syntax errors in Spring Expression Language (SpEL) expressions and property placeholders. It verifies that every SpEL expression and property placeholder is properly closed and that the content of each expression or placeholder is syntactically correct.

Only the Spring framework, not the Java compiler, parses SpEL expression inside Spring annotations. This means that the Java compiler does not detect invalid SpEL expressions during compile time. They will cause exceptions during runtime instead, or even fail silently when Spring interprets the expression as a simple string literal.

This rule reports syntactical errors in SpEL expressions but does not consider semantic errors, such as unknown identifiers or incompatible operand data types.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5994/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Possessive quantifiers in Regex patterns like below improve performance by eliminating needless backtracking:

But because possessive quantifiers do not keep backtracking positions and never give back, the following sub-patterns should not match only similar characters. Otherwise, possessive quantifiers consume all characters that could have matched the following sub-patterns and nothing remains for the following sub-patterns.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
?+ , *+ , ++ , {n}+ , {n,}+ , {n,m}+
```

Example 2 (unknown):
```unknown
Pattern pattern1 = Pattern.compile("a++abc");       // Noncompliant, the second 'a' never matches
Pattern pattern2 = Pattern.compile("\\d*+[02468]"); // Noncompliant, the sub-pattern "[02468]" never matches
```

Example 3 (unknown):
```unknown
Pattern pattern1 = Pattern.compile("aa++bc");            // Compliant, for example it can match "aaaabc"
Pattern pattern2 = Pattern.compile("\\d*+(?<=[02468])"); // Compliant, for example it can match an even number like "1234"
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-4517/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

According to the Java documentation, any implementation of the InputSteam.read() method is supposed to read the next byte of data from the input stream. The value byte must be an int in the range 0 to 255. If no byte is available because the end of the stream has been reached, the value -1 is returned.

But in Java, the byte primitive data type is an 8-bit signed two’s complement integer. It has a minimum value of -128 and a maximum value of 127. So by contract, the implementation of an InputSteam.read() method should never directly return a byte primitive data type. A conversion into an unsigned byte must be done before by applying a bitmask.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
InputSteam.read()
```

Example 2 (unknown):
```unknown
InputSteam.read()
```

Example 3 (unknown):
```unknown
@Override
public int read() throws IOException {
  if (pos == buffer.length()) {
    return -1;
  }
  return buffer.getByte(pos++); // Noncompliant, a signed byte value is returned
}
```

Example 4 (unknown):
```unknown
@Override
public int read() throws IOException {
  if (pos == buffer.length()) {
    return -1;
  }
  return buffer.getByte(pos++) & 0xFF; // The 0xFF bitmask is applied
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3346/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Since assert statements aren’t executed by default (they must be enabled with JVM flags) developers should never rely on their execution the evaluation of any logic required for correct program function.

© 2025 SonarSource S àrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
assert myList.remove(myList.get(0));  // Noncompliant
```

Example 2 (unknown):
```unknown
boolean removed = myList.remove(myList.get(0));
assert removed;
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-7184/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

According to Spring documentation, the @Scheduled annotation can only be applied to methods without arguments. Applying @Scheduled to a method with arguments will result in a runtime error.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

When the return value of a function call contains the operation status code, this value should be tested to make sure the operation completed successfully.

This rule raises an issue when the return values of the following are ignored:

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
java.io.File
```

Example 2 (unknown):
```unknown
Iterator.hasNext()
```

Example 3 (unknown):
```unknown
Enumeration.hasMoreElements()
```

Example 4 (unknown):
```unknown
Lock.tryLock()
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-899/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

When the return value of a function call contains the operation status code, this value should be tested to make sure the operation completed successfully.

This rule raises an issue when the return values of the following are ignored:

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
java.io.File
```

Example 2 (unknown):
```unknown
Iterator.hasNext()
```

Example 3 (unknown):
```unknown
Enumeration.hasMoreElements()
```

Example 4 (unknown):
```unknown
Lock.tryLock()
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-4348/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

An Iterable should not implement the Iterator interface or return this as an Iterator. The reason is that Iterator represents the iteration process itself, while Iterable represents the object we want to iterate over.

The Iterator instance encapsulates state information of the iteration process, such as the current and next element. Consequently, distinct iterations require distinct Iterator instances, for which Iterable provides the factory method Iterable.iterator().

This rule raises an issue when the Iterable.iterator() of a class implementing both Iterable and Iterator returns this.

The Iterable.iterator() method returning the same Iterator instance many times would have the following effects:

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
Iterable.iterator()
```

Example 2 (unknown):
```unknown
Iterable.iterator()
```

Example 3 (unknown):
```unknown
Iterable.iterator()
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5842/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

A regex should never include a repetitive pattern whose body would match the empty string. This is usually a sign that a part of the regex is redundant or does not do what the author intended.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
"(?:)*"      // same as the empty regex, the '*' accomplishes nothing
"(?:|x)*"    // same as the empty regex, the alternative has no effect
"(?:x|)*"    // same as 'x*', the empty alternative has no effect
"(?:x*|y*)*" // same as 'x*', the first alternative would always match, y* is never tried
"(?:x?)*"    // same as 'x*'
"(?:x?)+"    // same as 'x*'
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5831/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

A org.assertj.core.configuration.Configuration will be effective only once you call Configuration.apply() or Configuration.applyAndDisplay().

This rule raises an issue when configurations are set without the appropriate call to apply them.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
org.assertj.core.configuration.Configuration
```

Example 2 (unknown):
```unknown
Configuration.apply()
```

Example 3 (unknown):
```unknown
Configuration.applyAndDisplay()
```

Example 4 (unknown):
```unknown
Configuration configuration = new Configuration(); // Noncompliant, this configuration will not be applied.
configuration.setComparingPrivateFields(true);
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6417/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

This rule raises an issue when a method modifies the size of a collection, while the same collection is iterated.

Iterating over a collection using a for-each loop in Java relies on iterators.

An iterator is an object that allows you to traverse a collection of elements, such as a list or a dictionary. Iterators are used in for-each loops to iterate over the elements of a collection one at a time.

It is important to note that iterators are designed to be read-only. Modifying a collection while iterating over it can cause unexpected behavior, as the iterator may skip over or repeat elements. Therefore, it is important to avoid modifying a collection while iterating over it to ensure that your code behaves as expected.

Most JDK collection implementations don’t support such modification and may throw a ConcurrentModificationException. Even if no such exception is thrown, attempting to modify a collection during iteration could be the source of incorrect or unspecified behaviors in the code.

If you still want to modify the collection, it is best to refactor the code and use a second collection (e.g by using streams and filter operations).

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
ConcurrentModificationException
```

Example 2 (csharp):
```csharp
public static void foo(List<String> lst) {
    for (String element : lst) {
      if (element.startsWith("x")) {
        lst.remove(element); // Noncompliant: lst size has been modified by "remove" call while it's iterated.
      }
    }
  }
```

Example 3 (csharp):
```csharp
public static void foo(List<String> lst) {
    List<String> toRemove = new ArrayList<>();
    for (String element : lst) {
      if (element.startsWith("x")) {
        toRemove.add(element);
      }
    }
    lst.removeAll(toRemove);
  }
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6322/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Many modification methods in the collection interfaces are optional. Some implementations do not implement those methods and throw a runtime exception (UnsupportedOperationException). To fix this issue, make sure you call modification methods on a collection implementation that supports them.

The Java Collections framework defines interfaces such as java.util.List or java.util.Map. Several implementation classes are provided for each of those interfaces to fill different needs: some of the implementations guarantee a few given performance characteristics, some others ensure a given behavior, for example immutability.

Among the methods defined by the interfaces of the Collections framework, some are declared as "optional": an implementation class may choose to throw an UnsupportedOperationException when one of those methods is called. For example, java.util.Collections.emptyList() returns an implementation of java.util.List which is documented as "immutable". Calling the add method on this object triggers an UnsupportedOperationException.

Issues of this type interrupt the normal execution of a program, causing it to crash or putting it into an inconsistent state. Therefore, this issue might impact the availability and reliability of your application, or even result in data loss.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
UnsupportedOperationException
```

Example 2 (unknown):
```unknown
java.util.List
```

Example 3 (unknown):
```unknown
java.util.Map
```

Example 4 (unknown):
```unknown
UnsupportedOperationException
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3078/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Using compound operators as well as increments and decrements (and toggling, in the case of booleans) on primitive fields are not atomic operations. That is, they don’t happen in a single step. For instance, when a volatile primitive field is incremented or decremented you run the risk of data loss if threads interleave in the steps of the update. Instead, use a guaranteed-atomic class such as AtomicInteger, or synchronize the access.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
AtomicInteger
```

Example 2 (unknown):
```unknown
private volatile int count = 0;
private volatile boolean boo = false;

public void incrementCount() {
  count++;  // Noncompliant
}

public void toggleBoo(){
  boo = !boo;  // Noncompliant
}
```

Example 3 (unknown):
```unknown
private AtomicInteger count = 0;
private boolean boo = false;

public void incrementCount() {
  count.incrementAndGet();
}

public synchronized void toggleBoo() {
  boo = !boo;
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6216/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

In general, altering or bypassing the accessibility of classes, methods, or fields violates the encapsulation principle and could lead to runtime errors. For records the case is even trickier: you cannot change the visibility of records’s fields and trying to update the existing value will lead to IllegalAccessException at runtime.

This rule raises an issue when reflection is used to change the visibility of a record’s field, and when it is used to directly update a record’s field value.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
IllegalAccessException
```

Example 2 (unknown):
```unknown
record Person(String name, int age) {}

Person person = new Person("A", 26);
Field field = Person.class.getDeclaredField("name");
field.setAccessible(true); // secondary
field.set(person, "B"); // Noncompliant
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6001/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

When a back reference in a regex refers to a capturing group that hasn’t been defined yet (or at all), it can never be matched. Named back references throw a PatternSyntaxException in that case; numeric back references fail silently when they can’t match, simply making the match fail.

When the group is defined before the back reference but on a different control path (like in (.)|\1 for example), this also leads to a situation where the back reference can never match.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
PatternSyntaxException
```

Example 2 (unknown):
```unknown
Pattern.compile("\\1(.)"); // Noncompliant, group 1 is defined after the back reference
Pattern.compile("(.)\\2"); // Noncompliant, group 2 isn't defined at all
Pattern.compile("(.)|\\1"); // Noncompliant, group 1 and the back reference are in different branches
Pattern.compile("(?<x>.)|\\k<x>"); // Noncompliant, group x and the back reference are in different branches
```

Example 3 (unknown):
```unknown
Pattern.compile("(.)\\1");
Pattern.compile("(?<x>.)\\k<x>");
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5164/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

ThreadLocal variables are supposed to be garbage collected once the holding thread is no longer alive. Memory leaks can occur when holding threads are re-used which is the case on application servers using pool of threads.

To avoid such problems, it is recommended to always clean up ThreadLocal variables using the remove() method to remove the current thread’s value for the ThreadLocal variable.

In addition, calling set(null) to remove the value might keep the reference to this pointer in the map, which can cause memory leak in some scenarios. Using remove is safer to avoid this issue.

Rule will not detect non-private ThreadLocal variables, because remove() can be called from another class.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
ThreadLocal
```

Example 2 (unknown):
```unknown
ThreadLocal
```

Example 3 (unknown):
```unknown
ThreadLocal
```

Example 4 (csharp):
```csharp
public class ThreadLocalUserSession implements UserSession {

  private static final ThreadLocal<UserSession> DELEGATE = new ThreadLocal<>();

  public UserSession get() {
    UserSession session = DELEGATE.get();
    if (session != null) {
      return session;
    }
    throw new UnauthorizedException("User is not authenticated");
  }

  public void set(UserSession session) {
    DELEGATE.set(session);
  }

   public void incorrectCleanup() {
     DELEGATE.set(null); // Noncompliant
   }

  // some other methods without a call to DELEGATE.remove()
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3065/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

When using Math.min() and Math.max() together for bounds checking, it’s important to feed the right operands to each method. Math.min() should be used with the upper end of the range being checked, and Math.max() should be used with the lower end of the range. Get it backwards, and the result will always be the same end of the range.

Swapping method min() and max() invocations without changing parameters.

or swapping bounds UPPER and LOWER used as parameters without changing the invoked methods.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
private static final int UPPER = 20;
  private static final int LOWER = 0;

  public int doRangeCheck(int num) {    // Let's say num = 12
    int result = Math.min(LOWER, num);  // result = 0
    return Math.max(UPPER, result);     // Noncompliant; result is now 20: even though 12 was in the range
  }
```

Example 2 (unknown):
```unknown
private static final int UPPER = 20;
  private static final int LOWER = 0;

  public int doRangeCheck(int num) {    // Let's say num = 12
    int result = Math.max(LOWER, num);  // result = 12
    return Math.min(UPPER, result);     // Compliant; result is still 12
  }
```

Example 3 (unknown):
```unknown
private static final int UPPER = 20;
  private static final int LOWER = 0;

  public int doRangeCheck(int num) {    // Let's say num = 12
    int result = Math.min(UPPER, num);  // result = 12
    return Math.max(LOWER, result);     // Compliant; result is still 12
  }
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6856/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

The @PathVariable annotation in Spring extracts values from the URI path and binds them to method parameters in a Spring MVC controller. It is commonly used with @GetMapping, @PostMapping, @PutMapping, and @DeleteMapping to capture path variables from the URI. These annotations map HTTP requests to specific handler methods in a controller. They are part of the Spring Web module and are commonly used to define the routes for different HTTP operations in a RESTful API.

If a method has a path template containing a placeholder, like "/api/resource/{id}", and there’s no @PathVariable annotation on a method parameter to capture the id path variable, Spring will disregard the id variable.

This rule will raise an issue if a method has a path template with a placeholder, but no corresponding @PathVariable, or vice-versa.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
@PathVariable
```

Example 2 (unknown):
```unknown
@GetMapping
```

Example 3 (unknown):
```unknown
@PostMapping
```

Example 4 (unknown):
```unknown
@PutMapping
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-6818/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

@Autowired is an annotation in the Spring Framework for automatic dependency injection. It tells Spring to automatically provide the required dependencies (such as other beans or components) to a class’s fields, methods, or constructors, allowing for easier and more flexible management of dependencies in a Spring application. In other words, it is a way to wire up and inject dependencies into Spring components automatically, reducing the need for manual configuration and enhancing modularity and maintainability.

In any bean class, only one constructor is permitted to declare @Autowired with the required attribute set to true. This signifies the constructor to be automatically wired when used as a Spring bean. Consequently, when the required attribute remains at its default value (true), only a singular constructor can bear the @Autowired annotation. In cases where multiple constructors have this annotation, they must all specify required=false to be eligible as candidates for auto-wiring.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
required=false
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5833/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Describing, setting error message or adding a comparator in AssertJ must be done before calling the assertion, otherwise, settings will not be taken into account.

This rule raises an issue when one of the method (with all similar methods):

is called without calling an AssertJ assertion afterward.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
describedAs
```

Example 2 (unknown):
```unknown
withFailMessage
```

Example 3 (unknown):
```unknown
overridingErrorMessage
```

Example 4 (unknown):
```unknown
usingComparator
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3064/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Double-checked locking can be used for lazy initialization of volatile fields, but only if field assignment is the last step in the synchronized block. Otherwise you run the risk of threads accessing a half-initialized object.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
synchronized
```

Example 2 (csharp):
```csharp
public class MyClass {

  private volatile List<String> strings;

  public List<String> getStrings() {
    if (strings == null) {  // check#1
      synchronized(MyClass.class) {
        if (strings == null) {
          strings = new ArrayList<>();  // Noncompliant
          strings.add("Hello");  //When threadA gets here, threadB can skip the synchronized block because check#1 is false
          strings.add("World");
        }
      }
    }
    return strings;
  }
}
```

Example 3 (csharp):
```csharp
public class MyClass {

  private volatile List<String> strings;

  public List<String> getStrings() {
    if (strings == null) {  // check#1
      synchronized(MyClass.class) {
        if (strings == null) {
          List<String> tmpList = new ArrayList<>();
          tmpList.add("Hello");
          tmpList.add("World");
          strings = tmpList;
        }
      }
    }
    return strings;
  }
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-5850/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

In regular expressions, anchors (^, $, \A, \Z and \z) have higher precedence than the | operator. So in a regular expression like ^alt1|alt2|alt3$, alt1 would be anchored to the beginning, alt3 to the end and alt2 wouldn’t be anchored at all. Usually the intended behavior is that all alternatives are anchored at both ends. To achieve this, a non-capturing group should be used around the alternatives.

In cases where it is intended that the anchors only apply to one alternative each, adding (non-capturing) groups around the anchors and the parts that they apply to will make it explicit which parts are anchored and avoid readers misunderstanding the precedence or changing it because they mistakenly assume the precedence was not intended.

or, if you do want the anchors to only apply to a and c respectively:

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
^alt1|alt2|alt3$
```

Example 2 (unknown):
```unknown
^(?:a|b|c)$
```

Example 3 (unknown):
```unknown
^a$|^b$|^c$
```

Example 4 (unknown):
```unknown
(?:^a)|b|(?:c$)
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3518/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

If the denominator to an integer division or remainder operation is zero, a ArithmeticException is thrown.

This error will crash your program in most cases. To fix it, you need to ensure that the denominator value in all division operations is always non-zero, or check the value against zero before performing the division.

A division (/) or remainder operation (%) by zero indicates a bug or logical error. This is because in Java, a division or remainder operation where the denominator is zero and not a floating point value always results in an ArithmeticException being thrown.

Issues of this type interrupt the normal execution of a program, causing it to crash or putting it into an inconsistent state. Therefore, this issue might impact the availability and reliability of your application, or even result in data loss.

If the computation of the denominator is tied to user input data, this issue can potentially even be exploited by attackers to disrupt your application.

No issue is raised when the denominator is the constant zero, as it is considered an intentional failure.

When working with double or float values, no exception will be thrown, and the operation will result in special floating point values representing either positive infinity, negative infinity, or NaN. Thus, the rule does not apply to floating point division or remainder operations.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
ArithmeticException
```

Example 2 (unknown):
```unknown
ArithmeticException
```

Example 3 (unknown):
```unknown
void test_divide() {
  int z = 0;
  if (unknown()) {
    // ..
    z = 3;
  } else {
    // ..
  }
  z = 1 / z; // Noncompliant, possible division by zero
}
```

Example 4 (unknown):
```unknown
void test_divide() {
  int z = 0;
  if (unknown()) {
    // ..
    z = 3;
  } else {
    // ..
    z = 1;
  }
  z = 1 / z;
}
```

---

## Java static code analysis | Bug

**URL:** https://rules.sonarsource.com/java/type/Bug/RSPEC-3655/

**Contents:**
  - In-IDE
  - SaaS
  - Self-Hosted
- Java static code analysis
  - Unique rules to find Bugs, Vulnerabilities, Security Hotspots, and Code Smells in your JAVA code
  - Return values should not be ignored when they contain the operation status code
  - @EventListener methods should have one parameter at most
  - "@Scheduled" annotation should only be applied to no-arg methods
  - Consumed Stream pipelines should not be reused
  - "String.indexOf" should be used with correct ranges

IDE extension that lets you fix coding issues before they exist!

Setup is effortless and analysis is automatic for most languages

Fast, accurate analysis; enterprise scalability

Optional value can hold either a value or not. The value held in the Optional can be accessed using the get() method, but it will throw a

NoSuchElementException if there is no value present. To avoid the exception, calling the isPresent() or ! isEmpty() method should always be done before any call to get().

Alternatively, note that other methods such as orElse(...), orElseGet(...) or orElseThrow(...) can be used to specify what to do with an empty Optional.

© 2025 SonarSource Sàrl. All rights reserved.Privacy Policy | Cookie Policy | Terms of Use

**Examples:**

Example 1 (unknown):
```unknown
NoSuchElementException
```

Example 2 (unknown):
```unknown
isPresent()
```

Example 3 (unknown):
```unknown
!
isEmpty()
```

Example 4 (unknown):
```unknown
orElse(...)
```

---
