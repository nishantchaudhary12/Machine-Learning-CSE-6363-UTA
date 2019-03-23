For this assignment you will perform a hypothesis testing (as described in class) using Weka.

These are the steps that you will follow:

1. Install Weka if you haven't done it yet

2. Open the Experimenter tool from the Weka GUI

3. Click "New" (upper right corner) to create a new experiment

4. Give a name to you results file (i.e. hypotestresults), the ARFF file type is ok

5. Leave the parameters of the "Experiment type" section with their default values, i.e. number of folds for cross validation with the dafault value of "10"

6. Leave the parameters of the "Iteration control" section with their default values

7. Add the following datasets:

    a) contact-lenses.arff

    b) credit-g.arff

    c) diabetes.arff

8. Add the following algorithms:

    a) jRip

    b) j48

    c) Naive Bayes

9. Move to the "Run" phase (click "Run" from the top menu)

10. Click "Start"

11. Move to the "Analyse" phase (click "Analyse" from the top menu)

12. Load your experiment's results file by clicking "File" from the "Source" section and selecting your file

13. Configure your test as follows

    a) Paired T-test (corrected)

    b) Set the j48 algorithm as the test base

    c) Mark the "Show std deviations" option

14. Perform the test to obtain the results of the hypothesis test

15. Answer the questions that follow

Questions:

What is the meaning of an "*" or a "v" in the results?
What is the meaning of the (x/y/z) counters that appear at the bottom
Which algorithm performs significantly better than the base algorithm for the "german-credit" dataset?
Is there an algorithm that performs significantly worse than the base algorithm (J48)?
What can you say about the std deviations shown in the test?