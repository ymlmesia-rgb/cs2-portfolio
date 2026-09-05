# Student Score Checker
Name: Yuan Marcus L. Mesia
Section: 8 - Dahlia

--------------------------

## Activity Overview

In this activity, I improved a Student Score Checker program by applying proper coding standards and selection structures.
The program accepts a student score from 0 to 100 and determines the appropriate classification.

The classifications are:

| Score | Classification |  

| 90–100 | Outstanding | 

| 80-89 | Very Satisfactory | 

| 75-79 | Satisfactory | 

| 0-74 | Needs Improvement | 

Scores below 0 and scores above 100 are invalid.

# Part 1: Analyze the Logic

## Input
What information does the program need?
> The program needs a single integer representing a student's numerical score ('score')

## Valid Range
**Minimum valid score:** 0

**Maximum valid score:** 100

## Possible Outputs
1. 'Invalid score. Please enter a score between 0 and 100.'
2. 'The grade for the score {90-100} is Outstanding'
3. 'The grade for the score {80-89} is Very Satisfactory'
4. 'The grade for the score {75-79} is Staisfactory'
5. 'The grade for the score {0-74} is Needs Improvement'

## Boundary Condition
What condition will you use to determine whether the score is valid? 
> ('score') < 0 or ('score') > 100

## Multiple Decision Paths 
Explain how the program decides which classification should be displayed. 
> The program uses chained 'elif' statements evaluated sequentially:
> 1. First, it check if the score is out of bounds ('< 0' or '> 100').
> 2. If valid, it checks if the score is '>= 90' for **Outstanding**.
> 3. If false, it check if it is '>= 80' for **Very Satisfactory**.
> 4. If false, it check if it is '>= 75' for **Satisfactory**.
> 5. If none of these conditions are met, if falls back to the 'else' block for **Needs Improvement**.

# Part 2: Flowchart

<img width="1099" height="700" alt="image" src="https://github.com/user-attachments/assets/471201c6-1309-4bd5-841b-d37675760e97" />

***Made with LucidChart.co*** 

# Part 3: Pseudocode
START

  INPUT score

  IF score <0 or >100 THEN
  
    DISPLAY "Invalid score."
    
  ELSE IF score >= 90 THEN
  
    DISPLAY "Outstanding"
    
  ELSE IF score >= 80 THEN
  
    DISPLAY "Very Satisfactory"
    
  ELSE IF score >= 75 THEN
  
    DISPLAY "Satisfactory"
    
  ELSE 
  
    DISPLAY "Needs Improvement"
    
  END IF
  
END

# Part 4: Clean Code Implementatiom

## Source Code

See [score_checker.py](score_checker.py) for the executable file.

# Part 5: Testing

| Test | Input | Purpose | Expected Output | Actual Output | Result | 

| 1 | -1 | Below minimum |Invalid score. Please enter a score between 0 and 100. |Invalid score. Please enter a score between 0 and 100. |PASS| 

| 2 | 0 | Minimum boundary |The grade for the score 0 is Needs Improvement. |The grade for the score 0 is Needs Improvement. |PASS| 

| 3 | 74 | Below Satisfactory boundary |The grade for the score 74 is Needs Improvement. | The grade for the score 74 is Needs Improvement.|PASS| 

| 4 | 75 | Satisfactory boundary |The grade for the score 75 is Satisfactory. |The grade for the score 75 is Satisfactory. |PASS| 

| 5 | 80 | Very Satisfactory boundary |The grade for the score 80 is Very Satisfactory. |The grade for the score 80 is Very Satisfactory. |PASS| 

| 6 | 90 | Outstanding boundary |The grade for the score 90 is Outstanding. |The grade for the score 90 is Outstanding. |PASS| 

| 7 | 100 | Maximum boundary |The grade for the score 100 is Outstanding. |The grade for the score 100 is Outstanding. |PASS| 

| 8 | 101 | Above maximum |Invalid score. Please enter a score between 0 and 100. |Invalid score. Please enter a score between 0 and 100. |PASS| 

## Testing Reflection

1. Why is it important to test the values 0 and 100? 
> They represent the exact minimum and maximum valid limits of the acceptable range.

2. Why did you also test -1 and 101?
> These are off-by-one values just outside the boundary limits. These test values confirm that inputs outside the allowed limits are properly flagged as invalid.

3. Which test helped you understand boundary conditions the most? 
> Tests 3 and 4. Testing 74 and 75 revealed the exact cutoff score where performance upgrades from "Needs Improvement" to "Satisfactory."

4.  Did any of your tests initially fail? If yes, what did you change in your program?
> No. No tests failed because range checking ran before grade evaluation.

## Reflection

1. How did selection structures make the program more useful? 
> Selection structures let programs react to user input by running specific code instead of executing line-by-line.

2. How did proper comments and readable formatting improve your program? 
> Clear variable names, consistent indentation, and targeted comments make the code self-explanatory, helping team members understand it without reading raw logic.

3. Why is it useful to plan the program using a flowchart and pseudocode before writing the code? 
> Planning beforehand maps out all decision branches early, catching logic imperfections before you write syntax.








