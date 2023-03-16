# Shiny

## Good Resources

* [Mastering Shiny, by Hadley Wickham](https://mastering-shiny.org/index.html)
* [Difference between `reactive`, `eventReactive`, `observe`, `observeEvent`](https://stackoverflow.com/a/53016939/7133282)
* [`reactiveValues` vs `reactive`, by Dean Attali](https://stackoverflow.com/a/39440482/7133282)

## Concepts

## R

* `reactive`: Create a variable that can be changed over time by user inputs, evaluates "lazy" meaning only when called.
* `observe`: Continually monitor reactive events and variables, whenever ANY reactive variable is changed in the environment (the observed environment), the code is evaluated.
  * Can change values of previously defined reactive variables, cannot create/return variables.
  * Every `output` has an underlying `observe` function.
* `observeEvent`: Continually monitor **ONE** defined reactive variable/event (the trigger) and run the code when the the trigger is activated by change/input of that trigger. Can change values of previously defined reactive variables, cannot create/return variables.
* `eventReactive` Create a variable, with a defined trigger similar to observeEvent. Use this when you want a reactive variable that evaluates due to a trigger instead of when it is called.
* `reactiveValues`: Good for:
  * Whenever you have a variable that you think of as having some sort of state (rather than just reacting to a different value being updated).
  * When a variable can be updated in multiple places (e.g. different input variables can affect the reactive variable).
* `isolate`: Access the current value of a reactive value or expression without taking a dependency on it:

## Python

* `@output` decorator creates a `reactive.Effect`.

## r->Python Mappings

* `shiny::observe()` -> `reactive.Effect`
* `shiny::reactive()` -> `reactive.Calc`
