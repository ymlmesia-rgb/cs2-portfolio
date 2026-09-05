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
