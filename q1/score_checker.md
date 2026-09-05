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







