# Prior Authorization Checker

A production of project [ClassifyMyMeds](https://github.com/domagal9/classifymymeds) by Team Ruby at The Erdős Institute 2021 Boot Camp. The project is for the CoverMyMdes challenge, addressing the following problems:

1. Predict whether a prior authorization will get approved.
2. Forecast the monthly volume of prior authorizations.
3. Discover the formulary for each payer.
4. Predict the limitation of fills for certain drugs.

For full details, please go to the project repository: [ClassifyMyMeds](https://github.com/domagal9/classifymymeds).

This repository lists codes and data for the web app at [https://pachecker.herokuapp.com](https://pachecker.herokuapp.com), answering the first and the third problems above. Users enter information on `payer`, `drug`, some diagnosis such as `correct diagnosis`, `tried and failed` and `contraindication`, then the app responses with results including whether a prior authorization is needed, and the chance of being accepted if a prior authorization is needed.

## Information (Features) Details

- payer: a string identifying patients' insurance company.
- drug: the drug for the pharmacy claim or prior authorization if needed.
- correct diagnosis: the patient has the correct diagnosis for the associated drug.
- tried and failed: the patient has tried and failed the relevant generic alternatives.
- contraindication: the patient has an associated contraindication for the medication requested.

## Formulary

The formulary is stored in **models/formulary.json**. It associates each pair of (payer, drug) a code.

- code 70: the drug is not covered by the plan and is not on formulary, and typically implies that another course of therapy should be pursued. 
- code 75: the drug is on the formulary but does not have preferred status and requires a prior authorization (PA).
- code 76: the drug is covered, but that the plan limitations have been exceeded, which means that the limitations on the number of fills for that medication has been met.

## Model

The current model is the random forest, stored in **models/pa_clf_rf.json**. It assigns each tuple of (payer, drug, correct_diagnosis, tried_and_failed, contraindication) a number between 0 and 1, the probability of a PA get approved with information given by the tuple.