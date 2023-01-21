# Cypher

## Fundamentals

* Source: [What are graph databases?](https://memgraph.com/docs/cypher-manual/what-are-graph-databases)

### Nodes

* A pair of parentheses is used to represent nodes:

  ```cypher
  ()
  (node)
  ```

* The variable (node) stores node values so they can be processed or returned in a query later on.
* If you do not need to do anything with the node, skip the use of the variable, and hence you are creating an anonymous node.

### Relationships

* Relationships are the lines that connect nodes and represent a defined connection between them.
* Every relationship has a source node and a target node that represent the direction of the relationship.
  * If this direction is important, the relationship is considered directed, otherwise, it’s undirected.

### Labels

* Labels shape the domain by grouping nodes into sets or categories.
* Nodes with the same label belong to the same set.
* Nodes can also have multiple labels.

  ```cypher
  (:Person)
  (:City:Location)
  ```

### Properties

* Properties are key-value pairs of data stored on nodes or on relationships.

## Styling

* Source: [The Cypher Query Language - Best Practices](https://memgraph.com/blog/cypher-best-practices)
* Cypher is case-sensitive.
* Nodes:
  * Use `PascalCase` for node labels:
  
  ```cypher
  (:Country)
  (:City)
  (:CapitalCity)
  ```

* Relationships:
  * Use upper-case and underscore to separate multiple words:
  
  ```cypher
  [:LIVES_IN]
  (:BORDERS_WITH)
  ```

* Properties, variables, parameters, aliases, and functions:
  * Use `camelCase`:
  
  ```cypher
  dateOfBirth // Property key
  largestCountry // Variable
  size() // Function
  countryOne // Alias
  ```

* Clauses:
  * Preferably defined with capital letters, even if they consist of two or more words.
    * Although clauses are not case sensitive.
  * Each new clause should be placed at the beginning of a new line to ensure complete readability.
  
  ```cypher
  MATCH (c:Country)
  WHERE c.name = 'UK'
  RETURN c;
  
  WITH "2021-01-01" as currentDate
  MATCH (p:Person)
  WHERE p.birthdate > currentDate
  RETURN p.name;
  ```

* Keywords:
  * Preferably defined with capital letters.
    * Although keywords are not case sensitive.
  * These include DISTINCT, IN, STARTS WITH, CONTAINS, NOT, AND, OR and AS.
  
  ```cypher
  MATCH (c:Country)
  WHERE c.name CONTAINS 'United' AND c.population > 9000000
  RETURN c AS Country;
  ```

* Indentations and line breaks:
  * Not obligatory; used to improve readability.
  * Indentation is done using 2 spaces.
  * If there are multiple subqueries, they can be further grouped by using curly brackets.
  
  ```cypher
  //Indent 2 spaces on lines with ON CREATE or ON MATCH subqueries
  MATCH (p:Person {name: 'Helga'})
  MERGE (c:Country {name: 'UK'})
  MERGE (p)-[l:LIVES_IN]->(c)
    ON CREATE SET l.movedIn = date({year: 2020})
    ON MATCH SET l.modified = date()
  RETURN p, l, c;
  
  //Indent 2 spaces with braces for subqueries
  MATCH (p:Person)
  WHERE EXISTS {
    MATCH (p)-->(c:Country)
    WHERE c.name = 'UK'
  }
  RETURN p;
  ```

  * Exception:
    * One-liner subqueries, e.g.:

  ```cypher
  MATCH (p:Person)
  WHERE EXISTS { MATCH (p)-->(c:Country {name: 'UK'}) }
  RETURN p;
  ```

* Quotes:
  * Favour single quotes.
  * But use whichever provides the fewest escaped characters in the string.
  
  ```cypher
  // Bad syntax
  RETURN 'Memgraph\'s mission is: ', "A very famous quote is: \"Astra inclinant, sed non obligant.\"";
  
  // Recommended syntax
  RETURN "Memgraph's mission is: ", 'A very famous quote is: "Astra inclinant, sed non obligant."';
  ```

* Semicolons:
  * Place a semicolon at the end of a query when you have a script/block with multiple separate queries that should be executed independently.
  * Other than that, semicolons are not required at the end of a query.
  
  ```cypher
  MATCH (c:Country {name: 'UK'})
  RETURN c;
  
  MATCH (c:Country {name: 'Germany'})
  RETURN c;
  ```

* Null and Boolean Values:
  * Should always be lower case:
  
  ```cypher
  // Bad syntax
  MATCH (c:Country)
  WHERE c.island = NULL
    SET islandCountry = True
  RETURN c;
  
  // Recommended syntax
  MATCH (c:Country)
  WHERE c.island = null
   SET islandCountry = true
  RETURN c;
  ```

* Pattern styling:
  * When you have a pattern that is too long for one line, break after an arrow, not before it:
  
  ```cypher
  // Bad syntax
  MATCH (:Country)-->(:Person)-->(:Person)
      <--(c:Country)
  RETURN c.name;
  
  // Recommended syntax
  MATCH (:Country)-->(:Person)-->(:Person)<--
      (c:Country)
  RETURN c.name;
  ```

  * If you don’t plan on using a variable in the query, it’s better to use anonymous nodes and relationships instead.

  ```cypher
  // Bad syntax
  MATCH (c:Country {name: 'UK'})<-[l:LIVES_IN]-(p:Person)
  RETURN p.name;
  
  // Recommended syntax
  MATCH (:Country {name: 'UK'})<-[:LIVES_IN]-(p:Person)
  RETURN p.name;
  ```

  * Nodes with assigned variables should come before anonymous nodes and relationships if possible.
    * The same goes for nodes that are starting points or the central focus of the query.

  ```cypher
  // Bad syntax
  MATCH (:Person)-[:LIVES_IN]->(c:Country {name: 'UK'})
  RETURN c;
  
  // Recommended syntax
  MATCH (c:Country {name: 'UK'})<-[:LIVES_IN]-(:Person)
  RETURN c;
  ```

  * Patterns should be ordered so that left-to-right relationships (arrows) come at the beginning of the query.

  ```cypher
    // Bad syntax
  MATCH (c:Country)<-[:BORDERS_WITH]-(:Country)<-[:LIVES_IN]-(:Person)
  RETURN c;
  
  // Recommended syntax
  MATCH (:Person)-[:LIVES_IN]->(:Country)-[:BORDERS_WITH]->(c:Country)
  RETURN c;
  ```

* Spacing:
  * There should be one space between property predicates and label/type predicates.

  ```cypher
  // Bad syntax
  MATCH (:Country   {name: 'UK'})<-[:LIVES_IN{since: 2010}]-(p:Person)
  RETURN p.name;
  
  // Recommended syntax
  MATCH (:Country {name: 'UK'})<-[:LIVES_IN {since: 2010}]-(p:Person)
  RETURN p.name;
  ```

  * There should be no spaces in label predicates.

  ```cypher
  // Bad syntax
  MATCH (c: Country:  City)
  RETURN c.name;
  
  // Recommended syntax
  MATCH (c:Country:City)
  RETURN c.name;
  ```

  * There should be no spaces in patterns.

  ```cypher
  // Bad syntax
  MATCH (c:Country) --> (:City) 
  RETURN c.name;
  
  // Recommended syntax
  MATCH (c:Country)-->(:City) 
  RETURN c.name;
  ```

  * There should be one space on both sides of an operator.
  
  ```cypher
  // Bad syntax
  MATCH (c:Country)
  WHERE population>100000
  RETURN c.name;
  
  // Recommended syntax
  MATCH (c:Country)
  WHERE population > 100000
  RETURN c.name;
  ```

  * There should be one space between elements in a list (after each comma).

  ```cypher
  // Bad syntax
  WITH ['UK','US','Germany'] as list
  MATCH (c:Country)
  WHERE c.name IN list
  RETURN c.name;
  
  // Recommended syntax
  WITH ['UK', 'US', 'Germany'] as list
  MATCH (c:Country)
  WHERE c.name IN list
  RETURN c.name;
  ```

  * Function call parentheses should only have one space after each comma.
  
  ```cypher
  // Bad syntax
  RETURN split( 'A', 'B' , 'C' );
  
  // Recommended syntax
  RETURN split('A', 'B', 'C');
  ```

  * Map literals should only have one space after each comma and one space separating a colon and a value.

  ```cypher
  // Bad syntax
  WITH { name :'UK' ,population  :  70000000 } AS country
  RETURN country;
  
  // Recommended syntax
  WITH {name: 'UK', population: 70000000} AS country
  RETURN country;
  ```
