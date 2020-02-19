# Simple Insurer - Test Project

This is a project for the hiring purposes. It serves both parties - we can access your level of competence and 
you can get a feeling of the everyday problems we face.

## Prolog
Nowadays, big insurance companies have trouble modernising their internal IT systems. Main reasons are the complexity of such systems and the 
way those systems were implemented tens years ago. A consequence of such an obsolence is the fact many tasks are still done manually by 
employees of these insurance companies. An example of such a manual task would be the processing of claims made by customers.
Typically, when a claim occurs, the beneficiary (i.e. the insured customer) is required to pay out of the pocket and then claim it back 
from the insurance company. 

This test project (in a very simplistic way) shows how Paysure works and how it tackles the issue presented above.

## Environment setup
All you'll need is Python 3.6 (or higher) and some Python packages:

- `django==3.0.2`: as ORM
- `behave_django==1.3.0`: for testing 
- any REST API framework: `djangorestframework`, `flask`, `pyramid`, etc. or use plain `django`

## Goal

The aim of this assignment is to create an application that would allow customers to use their payment cards to pay for 
their claims based on their insurance policies.

You **do NOT need** to implement it COMPLETELY. It would be great if you spend approx. 1 hour on this task and see what you manage to implement.

If we like your solution, we will schedule a call with you and we will briefly discuss it with you - that should help to avoid any cheating :).

## Instructions

### Policy

It has following attributes:

- `external_user_id`: Unique indetifier of the customer
- `benefit`: Esentially covers of the policy (e.g. dentist, optician, gynecologist etc.)
- `currency`: Currency of the policy
- `total_max_amount`: Total amount in the `currency` that could be used by the beneficiary to pay for their claims

### Payment

When a customer pays with a card for medical expenses, authorization message is received as a json POST HTTP request at 
`http://localhost:8000/payment`. It contains these fields:

- `external_user_id`: Matches the `external_user_id` of policy
- `benefit`: Matches the `benefit` of policy
- `currency`: Matches the `currency` of policy
- `amount`: Authorization `amount` to be paid for the given `benefit`
- `timestamp`: Time of the transaction in ISO 8601 format

Example payment:

```
{ 
    "external_user_id": "user1",
    "benefit": "dentist",
    "currency": "GBP",
    "amount": 42,
    "timestamp": "2019-01-08T22:51:13+00:00"
}
```

If the policy for given `external_user_id`, `benefit` and `currency` exists, and the `amount` of 
this authorization + all authorized payments for this policy does not exceed the policy's `total_max_amount`, the 
authorization should be authorized by

```
-> http 200, json
{"authorized": true, "reason": null}
```

Otherwise the API should returns

```
-> http 200, json
{"authorized": false, "reason": <reason>}
```

`<reason>` could be:

- `POLICY_NOT_FOUND`: If no policy for given `external_user_id`, `benefit` and `currency` exists
- `POLICY_AMOUNT_EXCEEDED`: If the total `amount` of this and all others accepted authorizations for the matched policy 
exceed the `total_max_amount` of the policy

Note: Declined payments should not be reflected in the total sum called `total_max_amount`.

### Uploading policies
Policies should be uploaded through `http://localhost:8000/policy` as a json POST request such as:

```
{
    "external_user_id": "jabba_the_hutt",
    "benefit": "dentist",
    "total_max_amount": 1000,
    "currency": "gbp"
}
```

If successfully uploaded, API should return status code `201`. In order to keep things simple, we will not support 
creating more policies with the same combination `external_user_id`, `benefit` and `currency`. It is not necessary to 
support retrieving and delete.

## Tests

See `features/` folder for the implemented bdd tests. They should be helpful with both understanding of the task and 
development. Run the tests by `python manage.py behave` from the `src/` folder.

## Implementation

Project was pre-initialized from django app template for faster development.

- Allow sending policy data to `http://localhost:8000/policy`
- Allow sending payment messages to `http://localhost:8000/payment` and return appropriate response 
(see above)
- Store all incoming authorizations
- Persist the state of the policies (restart of the app should not break anything)

## Bonus task
Support payments in xml format such as:

```
<?xml version="1.0" encoding="UTF-8"?>
<root>
   <Bill_Amt>42</Bill_Amt>
   <MCC_Desc>dentist</MCC_Desc>
   <Txn_Ctry>GBP</Txn_Ctry>
   <Token>user1</Token>
   <TXN_Time_DE>20190108225113</TXN_Time_DE>
</root>
```

Mapping to payment request above is as follows:

- `Bill_Amt` = `amount`
- `MCC_Desc` = `benefit`
- `Txn_Ctry` = `currency`
- `Token` = `user_external_id`
- `TXN_Time_DE` is UTC time in format YYYYMMDDHHMMSS

Task: Allow receiving payments in this format at the API. The implementation is up to you.
