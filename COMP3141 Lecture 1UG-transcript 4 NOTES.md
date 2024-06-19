Summary of chunk 1:
Summary start from 'SPEAKER 0 um, she was the person who made this voice. Yeah, actually, yes. SPEAKER 1 Some of the exe' 
### Haskell Programming Lecture Notes

#### Organisational Information
- Assignment work spaces and collaboration:
  - Workspaces can be private/shared.
  - Collaboration is allowed during assignments but exams must be individual work.
  - Lecture notes/code will be available from last year.
  - Follow current lecturer's instructions for any discrepancies as they will be assessing the course.

#### Types and Data Types in Haskell

**Data Types:**
- Enumerated Data Types:
  - Similar to `enum` in C or Java.
  - Used to define a list of possible outcomes.
  ```
  data Document = Passport | BirthCertificate | DriverLicense | IDCard | SocialSecurityNumber
  ```

**Type Synonyms:**
- Type synonyms make code more comprehensible.
  - Make the purpose of the data clearer.
  - Example:
  ```
  type Document = String
  ```
  - Using a synonym like `Document` instead of `String` aids in maintainability and readability.

**Enumerated Types:**
- Using enumerated types helps prevent invalid data.
- Define valid items explicitly.
  ```
  data Document = Passport | BirthCertificate | DriverLicense | IDCard | SocialSecurityNumber
  ```

**Defining Data Types with Constructors:**
- Constructors used to create data with associated data.
- Structures without associated data don't distinguish data types.
- Example of `Coordinate` as a pair of integers:
  ```
  type Coordinate = (Int, Int)
  ```

**Customized Data Types:**
- Customized data types can combine data and structure.
- Example: unambiguous `MonthDay` type:
  ```
  data MonthDay = MDay (Int, Int)
  ```

**Code Snippets:**
- Type synonym for a list of documents:
  ```
  type Documents = [String]
  ```

- Function taking a list of `Document` synonyms to integers:
  ```
  points :: [Document] -> [Int]
  ```

#### Examples of Data Type Usage:
- Coordinate as a type synonym:
  ```
  type Coordinate = (Int, Int)
  ```

- MonthDay example with controlled data:
  ```
  data MonthDay = MonthDay (Int, Int)
  ```

**Practical Example:**
- To differentiate between a `Coordinate` and `MonthDay`, use constructors:
  ```
  data Coordinate = Coord Int Int
  data MonthDay = MDay Int Int
  ```

- Example instance definitions:
  ```
  coordinateExample = Coord 3 4
  monthDayExample = MDay 7 6
  ```

- Printing data:
  ```haskell
  instance Show Coordinate where
      show (Coord x y) = "(" ++ show x ++ "," ++ show y ++ ")"

  instance Show MonthDay where
      show (MDay m d) = show m ++ "/" ++ show d
  ```

These structured notes summarise the key concepts covered in the lecture, providing concise explanations along with relevant coding examples to illustrate the usage and syntax flexibly used in Haskell for defining and dealing with data types.

Summary of chunk 2:
Summary start from 'INTs. So in in, like, so and so this is a a data type with associated data. And so I could say, um s' 
### Data Types in Haskell

- **Definition and Construction**:
  ```haskell
  data MonthDay = MDay Int Int
  ```
  Example instances:
  ```haskell
  monthDayExample = MDay 7 6
  ```

- **Instance Definitions**:
  ```haskell
  instance Show MonthDay where
      show (MDay m d) = show m ++ "/" ++ show d
  ```

- **Printing Data**:
  ```haskell
  today = MDay 7 6
  ```

- **Type Explanation**:
  - By defining `MonthDay`, we can be precise about what `MonthDay` represents rather than just using a pair of `Int`s.
  - This precision allows us to, for example, differentiate between the month and day in the `MonthDay` type.

- **Maintaining Type Consistency**:
  - Better to associate data by using specific types (e.g., `Int` for days and a new type for months) for clarity and correctness.

### Limiting the Range of Types

- **Specific Range Constraints**:
  - Direct constraints on `Int` types (e.g., ensuring a value is between 1 and 12) are not directly enforceable within the type itself.
  - Better approach: Define a custom type to represent constrained values rather than using a general `Int`.

### Custom Types and Constructors

- **Defining Custom Types**:
  - Specify exact valid values and avoid errors during construction.
  ```haskell
  data Month = January | February | March | April | May | June
             | July | August | September | October | November | December

  data MonthDay = MDay Int Month
  ```

- **Show Instance for Custom Types**:
  ```haskell
  instance Show Month where
      show January   = "January"
      show February  = "February"
      show March     = "March"
      show April     = "April"
      show May       = "May"
      show June      = "June"
      show July      = "July"
      show August    = "August"
      show September = "September"
      show October   = "October"
      show November  = "November"
      show December  = "December"
      
  instance Show MonthDay where
      show (MDay d m) = show d ++ " " ++ show m
  ```

### Intuitively Understanding Data Representation

- **Internal Representation**:
  - `MDay` constructor internally represented as an object pointing to another object for `Int` and `Month`.
  - Intuitive understanding: An instance of `MonthDay` holds pointers to the specific day and month values.

### Combining Sum Types and Data Types

- **Type Definitions**:
  ```haskell
  data Coordinate 
    = TwoD (Int, Int) 
    | ThreeD (Int, Int, Int)
  ```

- **Example of Sum and Compound Types**:
  ```haskell
  twoDCoord  = TwoD (1, 2)
  threeDCoord = ThreeD (1, 2, 3)
  ```

### Generics and Type Parameters

- **Polymorphic Types in Haskell and Java**:
  - Similar to Java's generics (e.g., `List<Integer>`), Haskell can have type parameters.
  - Example with lists:
    ```haskell
    data MyList a = Empty | Cons a (MyList a)
    ```

- **Instances of Polymorphic Types**:
  ```haskell
  exampleList = Cons 1 (Cons 2 (Cons 3 Empty))  -- MyList of integers
  ```

Remember, the distinct advantage of defining specific custom types and using appropriate type constraints aids not just in maintainability and readability of the code but also in ensuring that invalid states are unrepresentable.

Summary of chunk 3:
Summary start from 'it mean? It means the objects are an A, um and so what? What are my options? What are my constructs?' 
- **Recursive Data Structures in Haskell**:
  - Lists are either empty or an object `Cons` with a smaller list.
    ```haskell
    data MyList a = Empty | Cons a (MyList a)
    exampleList = Cons 1 (Cons 2 (Cons 3 Empty))  -- MyList of integers
    ```
- **Recursive Nature**:
  - Lists in Haskell are recursively defined.
  - An example: a list of integers or strings.
  - The first element of a list is an object of type `A`.
  - The second element is a pointer to another list.

- **Defining Useful Data Types: Maybe**:
  - `Maybe` type is defined to handle nullability.
    ```haskell
    data Maybe a = Nothing | Just a
    ```
  - Represents an object that can be either `Nothing` or `Just` some value `A`.
  - Example usage:
    ```haskell
    x = Just 3
    y = Nothing
    -- x is a Maybe Int
    -- y is a Maybe Int
    ```
  - Helps deal with nullable types explicitly.

- **Advantages of `Maybe`**:
  - Ensures functions handle possible null values.
  - Removes side effects, such as null pointer exceptions.
  - Functions should explicitly define behavior for `Nothing` and `Just` cases.

- **Example Function Using Maybe**:
  - Handling nullable input.
    ```haskell
    myFunc :: Maybe Int -> Int
    myFunc (Just x) = x + 1
    myFunc Nothing  = 0
    ```

  - Returning nullable output (e.g., head of a list):
    ```haskell
    safeHead :: [a] -> Maybe a
    safeHead []     = Nothing
    safeHead (x:xs) = Just x
    ```
  - `safeHead` avoids exceptions for empty lists by using `Maybe`.

- **Constructors for Maybe**:
  - `Just` serves as a wrapper confirming the existence of a value.
  - Example:
    ```haskell
    data Maybe a = Nothing | Just a

    -- Just is a wrapper creator
    example = Just 5  -- Makes 5 a Maybe Int
    ```
  
- **Type Parameters and Recursive Types**:
  - Type parameters like list and maybe can be recursive.
  - Example: Natural numbers definition.
    ```haskell
    data Nat = Zero | Succ Nat
    ```
  - Natural numbers are defined as either Zero or Successor of another natural number.
  
Remember the advantages of explicit null handling with `Maybe` in functional programming; it helps maintain a clean, side-effect-free codebase and ensures accurate type assurances and error management mechanisms. Using `Maybe`, recursive types, and appropriate data constructors are key functional programming approaches in Haskell to manage types and values comprehensively.

Summary of chunk 4:
Summary start from 'of a natural. Alright. And so the number one. So I think I think it's defined. No, in no, no. Um goo' 
#### Haskell Natural Numbers
- Define natural numbers using recursive data type.
```haskell
data Nat = Zero | Succ Nat
```
- `Zero` represents 0.
- `Succ` constructor represents the successor of a natural number.
- Example:
  - `Succ Zero` represents 1.
  - `Succ (Succ Zero)` represents 2.

#### Recursive Lists and Parameterization

- Lists in Haskell parameterized by type:
```haskell
data List a = Nil | Cons a (List a)
```
- `a` stands for any type, allowing lists of various types (Int, String, etc.).
- Analogous to Java Generics:
  ```java
  public interface List<E> {
      E head();
      // Other methods
  }
  ```
- In Haskell `map` function type:
```haskell
map :: (a -> b) -> [a] -> [b]
```
- Takes a function from `a` to `b`, a list of `a`, returns a list of `b`.

#### Robust Type Definitions

- Use specific types to eliminate invalid states:
  - Example: Define `Month` and `Day` types to avoid invalid dates.
  - `Month` type restricts month values, avoiding invalid month/day combinations.

#### Preventing Invalid States
- Example of Contact with optional details:
```haskell
data ContactDetails = Address String | Email String | Both String String
data Contact = Contact String ContactDetails
```
- Instead of:
```haskell
data Contact = Contact { name :: String, address :: Maybe String, email :: Maybe String }
```
- Ensures all contacts have at least one method of contact.

#### Partial Functions
- Partial functions defined only for some input values lead to runtime errors.
- Strive to avoid by ensuring functions are defined for all possible input values.
- Example: Avoid `monthDayToString` for invalid dates like 30th February.

#### Summary
- Use type systems to reduce invalid states and manage complexity.
- Recursive data types (like lists and maybe) enhance type safety and correctness.
- Parameterization and generics offer flexibility in type definitions.
- Prefer total functions over partial functions for better program reliability.

Feel free to ask questions to clarify concepts further.

Summary of chunk 5:
Summary start from 'seen I have seen this before? I can't remember where. Um Well, for instance, if I take the is primar' 
### Handling Partially Defined Functions

- **Partially Defined Functions**:
  - Calling a function outside its defined domain throws exceptions.
  - Example:
    - `isPrimary` only defined for passport and birth certificate.
    - Asking `isPrimary` for a credit card results in a "function not defined" error.
  - Common partial functions:
    - `head` of an empty list throws an exception.
    - `tail` of an empty list throws an exception.
    - `!!` (bang bang) for list indexing:
      ```haskell
      [0, 1, 2] !! 2 -- OK, returns 2
      [0, 1, 2] !! 3 -- Throws an exception
      ```

- **Managing Partiality**:
  - **Larger Codomain**: Use types like `Maybe`.
    - Modify `head`:
      ```haskell
      head :: [a] -> Maybe a
      head [] = Nothing
      head (x:xs) = Just x
      ```
  - **Constrain Domain**: Use restrictive types like non-empty lists.
    - Define non-empty list type:
      ```haskell
      data NonEmptyList a = One a | Cons a (NonEmptyList a)
      ```
    - Define `safeHead`:
      ```haskell
      safeHead :: NonEmptyList a -> a
      safeHead (One x) = x
      safeHead (Cons x xs) = x
      ```

### Type Classes

- **Introduction**:
  - Type classes in Haskell are like interfaces in Java or header files in C.
  - If a type belongs to a type class, it must adhere to certain functions defined by that class.

- **`Show` Type Class**:
  - Enables conversion of objects to strings.
  - Default behaviour when using `deriving Show`:
    - For complex types, `Show` applies recursively.
    - Example: If `MonthDay` type has instances `Int` and `Month` which are `Show`, `MonthDay` can also derive `Show`.
  - Usage:
    ```haskell
    data Month = Jan | Feb | Mar deriving Show
    data MonthDay = MonthDay Int Month deriving Show
    ```

- **`EQ` Type Class**:
  - Enables equality and inequality comparisons with `==` and `/=`.
  - Can override using custom equality logic.
  - Example:
    ```haskell
    data CustomType = CustomType Int String deriving Eq
    ```

- **Defining Custom Instances**:
  - Rather than deriving, define specific behaviour.
  - Example for custom `Eq` implementation:
    ```haskell
    instance Eq CustomType where
        (CustomType i1 s1) == (CustomType i2 s2) = i1 == i2 && s1 == s2
    ```

### Practical Examples

- **Handling Lists with Maybe**:
  ```haskell
  safeTail :: [a] -> Maybe [a]
  safeTail [] = Nothing
  safeTail (x:xs) = Just xs
  ```

- **Defining Non-Empty List**:
  ```haskell
  data NonEmptyList a = One a | Cons a (NonEmptyList a)
  ```

- **Custom Show Instance**:
  ```haskell
  data Person = Person String Int
  instance Show Person where
      show (Person name age) = name ++ " is " ++ show age
  ```

### Important Notes
- **Avoid Partial Functions**: Aim for total functions to enhance program reliability.
- **Use Type Systems**: To manage complexity and prevent invalid states.
- **Parameterization and Generics**: For flexible and reusable code.

Summary of chunk 6:
Summary start from 'we How do we implement that? So instead, what we do is we say, um um, we say our data type is an ins' 
### Custom Type Classes and Instances in Haskell

#### **Instance of Show**
- Custom implementation of the `Show` type class for a data type.
- Defining how a data type should be presented as a string:

    ```haskell
    data Bool = False | True
    instance Show Bool where
        show True = "True"
        show False = "False"
    ```

#### **Example with MonthDay**
- Custom `Show` implementation for a `MonthDay` (day and month) data type.

    ```haskell
    data MonthDay = MonthDay Int String
    instance Show MonthDay where
        show (MonthDay day month) = show day ++ "th of " ++ month
    ```

- Example usage: 

    ```haskell
    let today = MonthDay 7 "June"
    print today  -- Output: "7th of June"
    ```

#### **Equality Type Class (Eq)**
- Custom implementation for the equality type class (`==`).

    ```haskell
    instance Eq MonthDay where
        (MonthDay day1 month1) == (MonthDay day2 month2) = (day1 == day2) && (month1 == month2)
    ```

    - `==` operator defined for `MonthDay`.

#### **Functional Type Classes**
- Type class `Show` and function type:

    ```haskell
    class Show a where
        show :: a -> String
    ```

- Automatic derivation for lists using the `Show` instance.

    ```haskell
    let monthDaysList = [MonthDay 7 "June", MonthDay 25 "December"]
    print monthDaysList  -- Calls show for each element automatically
    ```

### Mathematical Concepts in Haskell

#### **Semi-Group**
- **Definition**: A set with an associative binary operation.
    - Example: `(S, • )` where `•` is associative.
    - Example with multiplication of integers: `a • (b • c) = (a • b) • c`.
    
    ```haskell
    instance Semigroup Int where
        (<>) = (*)
    ```

#### **Examples of Associativity**
- **Integers with Addition**: 

    ```haskell
    instance Semigroup Int where
        (<>) = (+)
    ```
    
- **Associativity with Functions**
    - Composition of functions is associative.

    ```haskell
    let f x = x + 1
    let g x = x * 2
    let h x = x - 3
    ```
    
    - `(h . g) . f == h . (g . f)`
    
    ```haskell
    (h . g) . f == \x -> h (g (f x))
    h . (g . f) == \x -> h (g (f x))
    ```

#### **Non-Associative Operations**
- **Subtraction**:

    ```haskell
    5 - (3 - 2) ≠ (5 - 3) - 2
    ```
    
- **Division**:
    
    ```haskell
    5 / (3 / 2) ≠ (5 / 3) / 2
    ```

### Function Composition and Associativity

- **Function Composition**:
    - `(h . g . f)` associates as `(h . (g . f))` or `((h . g) . f)`.

    ```haskell
    f :: Int -> Int
    g :: Int -> Int
    h :: Int -> Int

    -- Chains multiple function applications:
    (h . g . f) x == h (g (f x))
    ```

#### **Applications and Code Examples**:
- **String Concatenation as a Semi-Group**:

    ```haskell
    "abc" ++ ("def" ++ "ghi") == ("abc" ++ "def") ++ "ghi"
    ```

- **Function Composition Visualized**:
    - Mapping transformations through composition.

    ```haskell
    f . g . h == \x -> f (g (h x))
    ```

### Advanced Type Classes
- **Abstract Algebra in Haskell**:
    - Algebraic structures (like semi-groups) mapped into Haskell’s type system.
    
    ```haskell
    class Semigroup a where
        (<>) :: a -> a -> a
    ```

- **Discussion of Associative Functions**:
    - Examples provided for clarity, including shorthands and intuitive use cases.

---

*Feel free to ask any questions during the lecture or revisit these concepts in the provided resources.*

Summary of chunk 7:
Summary start from 'is just something with with an asso associative multiplication. Um and in fact, there's a class in h' 
### Advanced Type Classes

#### **Abstract Algebra in Haskell**

- Algebraic structures like semi-groups are mapped into Haskell’s type system.
- **Semigroup** defined with associative multiplication operation.

```haskell
class Semigroup a where
    (<>) :: a -> a -> a
```

#### **Associative Functions**

- Associative nature discussed through hands-on examples.
- Example: RGB color mixing - defined as a semigroup.
    - Color defined as a tuple of integers (red, green, blue, alpha).
    - Mix operation adds color components and maxes at 255.
    - Mixing operation demonstrates associativity.

```haskell
data Color = Color Int Int Int Int

instance Semigroup Color where
    (<>) (Color r1 g1 b1 a1) (Color r2 g2 b2 a2) =
        Color (min 255 (r1 + r2)) (min 255 (g1 + g2)) (min 255 (b1 + b2)) (min 255 (a1 + a2))
```

- Monads are introduced as special kinds of semigroups with identity.
- Monoid: a semigroup with an identity element.
    - Examples:
        - **Integers with addition**: identity is 0.
        - **Integers with multiplication**: identity is 1.
        - **Set union**: identity is empty set.
        - **Set intersection**: identity is the universal set.
        - **String concatenation**: identity is empty string.
        - **List concatenation**: identity is empty list.
        - **Function composition**: identity is the identity function.

```haskell
class Semigroup a => Monoid a where
    mempty :: a
    
instance Monoid Color where
    mempty = Color 0 0 0 0  -- Identity Color is black
```

### Monads

- Definition: A monad is built upon a monoid within the category of endofunctors.
- Example in Haskell: List monad, Maybe monad.
    - Monad encapsulates a computational strategy.
    - Monad must implement `return` (or `pure`) and `>>=` (bind).

```haskell
class Monad m where
    return :: a -> m a
    (>>=) :: m a -> (a -> m b) -> m b
```

#### **Example of Monad Instances**

- **Maybe Monad**:
    - Models computations which may fail.

```haskell
instance Monad Maybe where
    return = Just
    
    Nothing >>= _ = Nothing
    (Just x) >>= f = f x
```

- **List Monad**:
    - Models nondeterministic computations.

```haskell
instance Monad [] where
    return x = [x]
    xs >>= f = concatMap f xs
```

### Type Classes in Haskell

- Understanding the concept of type classes for creating polymorphic functions.
- Use of `class` and `instance` to structure type-based polymorphism.

- **Basic example of type class `Eq` for equality comparison**:
    ```haskell
    class Eq a where
        (==) :: a -> a -> Bool

    instance Eq Int where
        x == y = x `primIntEq` y
    ```

---

*Feel free to ask any questions during the lecture or revisit these concepts in the provided resources.*

Summary of chunk 8:
Summary start from 'basically, um if I try to do it in one way, it'll say right? Um, yeah. You, You, You you You've alre' 
### Type Classes in Haskell (cont'd)

#### Type Synonyms, Data Types, and New Type Keywords
- **Type Synonyms**: Provides alternative names to existing types.
- **Data Types**: Used to create completely new data structures.
- **New Type**: Acts as a middle ground between type synonyms and data types.
    - A `newtype` can only have one constructor with exactly one argument, acting as a wrapper around an existing type.
    - Useful for creating distinct types from existing ones to prevent mistakes.

```haskell
newtype Score = Score Int
```

- Example using `Score` to create a semi group under addition and a Monoid using zero:
    ```haskell
    instance Semigroup Score where
        Score x <> Score y = Score (x + y)
        
    instance Monoid Score where
        mempty = Score 0
    ```

### The `Ord` Type Class
- For Ordered Data Types (like Java's `Comparable`).
- Requires a comparison function, usually `(<=) :: a -> a -> Bool`.

**Properties of Ordering**:
- **Reflexivity**: `a <= a`
- **Anti-symmetry**: `a <= b` and `b <= a` imply `a == b`
- **Transitivity**: `a <= b` and `b <= c` imply `a <= c`
- **Total Order**: Either `a <= b` or `b <= a` must hold, no incomparable elements.

### Example of Partial Orders

- **Subset Relation**:
    - Reflexive: Any set is a subset of itself.
    - Anti-symmetry: If `A ⊆ B` and `B ⊆ A`, then `A = B`.
    - Transitive: If `A ⊆ B` and `B ⊆ C`, then `A ⊆ C`.
    - Not a total order as some sets can be incomparable.

### Symmetry and Transitivity in `Eq`
- **Reflexivity**: `a == a`
- **Symmetry**: If `a == b`, then `b == a`
- **Transitivity**: If `a == b` and `b == c`, then `a == c`

**Equivalence Relations**:
- Relations satisfying reflexivity, symmetry, and transitivity are known as equivalence relations.

**Substitution Principle**:
- If `x == y`, then for any function `f`, `f x == f y` should hold. Known as substitution or alpha equivalence.

### Practical Examples
- Implementation of `Eq` for `Int`:
    ```haskell
    instance Eq Int where
        (==) x y = x `primIntEq` y
    ```

- Depiction of a total order using `Ord`:
    ```haskell
    instance Ord Int where
        (<=) x y = x `primIntLessEq` y
    ```

### Upcoming Activities
- Quiz 1 due on Tuesday.
- Quiz 2 to be released.
- First exercise to be released soon for weekend work.

Indicating the end of the lecture section and the transition to a break.

**Reminder**: Grab some food and take a break before the next session.

---

*Next activities and resources will be uploaded to the ed platform.*

Summary of chunk 9:
Summary start from 'out. So you've got and you have adequate time. I believe in adequate time allocation. Hi. I was just' 
### Continuation of Haskell Lecture on Recursion and List Functions

#### Implementation of `Eq` for `Int`:
```haskell
instance Eq Int where
    (==) x y = x `primIntEq` y
```

#### Depiction of a Total Order using `Ord`:
```haskell
instance Ord Int where
    (<=) x y = x `primIntLessEq` y
```

#### Upcoming Activities:
- Quiz 1 due on Tuesday.
- Quiz 2 to be released.
- First exercise to be released soon for weekend work.

**Reminder**: Grab some food and take a break before the next session.

---

### Q&A and Lecture Continuation

##### Question 1: What if we define an incorrect instance of `Ord`?
- Inquiry about instances not following expected rules (e.g., non-zero behaving as identity).
- Response: Instances must adhere to class laws; no explicit rules force adherence but non-compliance results in unexpected behavior.

##### Question 2: Recursive Lists in Definitions
- Clarification on non-empty list definitions.
- Response: A recursive case does not end in an empty list; always ensure a base case like a singleton list (e.g., `10`).

**Note: Ongoing technical difficulties with screen mirroring and projector**. 

---

### Practical Problems and Exercises

#### Practice Problems Overview:
- Week 1: Problems on folding and other basic operations.
- Week 2: Problems covering recent concepts.
- Encouragement to use 99 Haskell Problems for extra practice.

#### Example Problem: Sum of Elements in a List

Consider designing a function `mySum` that sums all elements in a list of integers using recursion.

```haskell
mySum :: [Int] -> Int
mySum [] = 0
mySum (n:ns) = n + mySum(ns)
```

- Empty list case: `0`.
- Recursive case: current element plus sum of the rest (`n + mySum ns`).

Testing `mySum` function:
```haskell
mySum [1, 2, 3] -- Result: 6
mySum [1, 2, 3, 3] -- Result: 9
```

#### Exercise: Product of Elements in a List

Define function `myProduct` that calculates the product of all elements in a list of integers.

```haskell
myProduct :: [Int] -> Int
myProduct [] = 1
myProduct (n:ns) = n * myProduct(ns)
```

- Empty list case: `1` (identity element for multiplication).
- Recursive case: current element times product of the rest (`n * myProduct ns`).

Testing `myProduct` function:
```haskell
myProduct [2, 3, 4] -- Result: 24
myProduct [1, 5, 2] -- Result: 10
```

**Note**: The identity values are important in these base cases to ensure expected results when lists are combined using recursive definitions.

Summary of chunk 10:
Summary start from 'that, then you could, um we could do something. Like we could add another case for a singleton list,' 
**Haskell Programming Lecture Notes**

**Defining `myProduct` Function:**
```haskell
myProduct :: [Int] -> Int
myProduct [] = 1
myProduct (n:ns) = n * myProduct ns
```
- **Base Case**: For an empty list, return `1` (identity for multiplication).
- **Recursive Case**: Multiply current element by the product of the rest of the list.

**Testing `myProduct` function:**
```haskell
myProduct [2, 3, 4] -- Result: 24
myProduct [1, 5, 2] -- Result: 10
```

- Identity values are crucial for base cases to ensure expected results in recursive definitions.

**Higher-Order Functions:**

Introduction to `myBinOp`:

- Purpose: Avoid redundancy by creating a general function for binary operations.
- Accepts a function (e.g., `+` or `*`), an identity element `z`, and a list of integers.
- Example definition:
```haskell
myBinOp :: (Int -> Int -> Int) -> Int -> [Int] -> Int
myBinOp _ z [] = z
myBinOp f z (n:ns) = f n (myBinOp f z ns)
```
- **Base Case**: Return `z`.
- **Recursive Case**: Apply the function `f` to the current element and recursively process the rest.

Testing `myBinOp` with `+` and `*`:
```haskell
mySum = myBinOp (+) 0
myProduct = myBinOp (*) 1
mySum [5, 4, 3]     -- Result: 12
myProduct [5, 4, 3] -- Result: 60
```

**Using Fold Functions:**

- **Fold** functions are Haskell's built-in higher-order functions equivalent to `myBinOp`.

**FoldR and FoldL:**

- **FoldR**: Folds from the right.
- **FoldL**: Folds from the left.

**Example: `foldr` and `foldl` with addition:**
```haskell
foldr (+) 0 [1, 2, 5, 4] -- Result: 12
foldl (+) 0 [1, 2, 5, 4] -- Result: 12
```

Rewriting `mySum` and `myProduct` using fold functions:
```haskell
mySumPrime :: [Int] -> Int
mySumPrime = foldr (+) 0

myProductPrime :: [Int] -> Int
myProductPrime = foldr (*) 1
```

**Non-Commutative Example - Exponentiation:**
```haskell
foldl (^) 1 [1, 2, 3] -- Result: 1
foldr (^) 1 [1, 2, 3] -- Result: 8
foldl (^) 2 [1, 2, 3] -- Result: 3
foldr (^) 2 [1, 2, 3] -- Result: 9
```

Associativity Matters:
- Associativity of operations impacts the result.
- Example of concatenating strings:
```haskell
foldl (++) "" ["and", "or", "F", "DJ", "blah"]
-- Result: "andorFDJblah"

foldr (++) "" ["and", "or", "F", "DJ", "blah"]
-- Result: "andorFDJblah"
```

- Thus, it's the bracketing in fold operations that affects the result, rather than the order of elements.

Summary of chunk 11:
Summary start from 'where if you you can define any function that works like stepping through lists, with a fold. So it ' 
### Mapping with Fold
- Folds can emulate other functions that traverse lists.
- Example: Defining `map` using `foldr`.

**Type of `foldr`:**
```haskell
foldr :: (a -> b -> b) -> b -> [a] -> b
```

1. Takes a binary function `(a -> b -> b)`
2. Initial accumulator of type `b`
3. List `[a]`

**Define `map` using `foldr`:**
- Apply function `f` to each element.
- Maintain the structure as a list.

```haskell
map' f = foldr (\x acc -> (f x) : acc) []
```
*Example:*
```haskell
map' (+1) [1, 2, 3] -- Result: [2, 3, 4]
```

### Foldr with Foldl
- Can `foldl` be implemented using `foldr`?

**Fold types:**
```haskell
foldl :: (b -> a -> b) -> b -> [a] -> b
foldr :: (a -> b -> b) -> b -> [a] -> b
```

**Define `foldl` using `foldr`:**
- Reverse input list and apply `foldr`.

```haskell
foldl' f z xs = foldr (\x g a -> g (f a x)) id xs z
```
*Explanation:*
- Helper function accumulates values by applying `f`.
- Starts with an identity function `id`.

*Example:*
```haskell
foldl' (-) 0 [1, 2, 3] -- Result: -6
```

### More on `foldr` and `foldl`
- Using `foldr` to process lists in reverse.

**Handling Base Case:**
- Example of folding an empty list safely.

```haskell
foldr (\x acc -> (x+1) : acc) [] [1, 2, 3] -- Result: [2, 3, 4]
foldr (\x acc -> x + acc) 0 [] -- Result: 0
```

### Handling Errors in Fold Operations
- Code snippet to demonstrate fold behavior and type mismatches.

**Possible Error: Type Mismatch:**
- Example where type mismatch error occurs when using `foldr`.

```haskell
foldr (\x acc -> (x + acc)) 0 ["a", "b"] 
-- Error: Couldn't match expected type `Num a => a` with actual type `[Char]`
```

### Standard Fold Functions in Haskell
- Commonly used fold functions built into Haskell.

**Examples:**
```haskell
foldr (:) [] [1, 2, 3] -- Result: [1, 2, 3]
foldl (++) "" ["aaa", "bbb"] -- Result: "aaabbb"
```

### Key Points and Nuances
- Folds reduce lists by applying functions across elements.
- Behavior depends on the order and type of functions used.
- `foldr` operates from the right end of the list.
- `foldl` operates from the left end of the list.
- Results can vary drastically based on the function used and the associativity.

