## Brute Force

I took a brute force approach to solve the challenge. You can find the steps I took below. I included notes on the refactor as well, but since you said to only spend 8 to 10 hours on it, I didn't have time to do any of the steps outlined.

To run the code, follow the instructions in the "README.md" file from the repo. Make sure to run the seed. Once the app is running, there are four endpoints. The POST endpoint, works different than what was outlined in the challenge. Essentially, the provided dataset needed to be wrapped in an array for it to be valid JSON. To get around that, the POST endpoint only handles a single JSON object (wrapped in an array), not a number of objects. I was going to refactor this, but ran out of time. You can find the rest of my assumptions in the same "steps.md" file. You'll also notice that I am not storing any of the data in a DB. Again, this is intentional. I was going to refactor it by adding Mongo, but again ran out of time. Finally, to prevent having to reinvent the wheel, I started with a boilerplate. I am the author of the boilerplate so I can detail everything happening with it.  

### Steps

1. Upgrade [Flask Skeleton](https://github.com/realpython/flask-skeleton) to Python 3.6
1. Remove client-side code
1. Remove `user` and `main` blueprints
1. Remove unnecessary dependencies and extensions
1. Add `api` blueprint
1. Update tests
1. Add endpoint for POST request
1. Validate JSON payload
1. Add tests
1. Save data to file
1. Update tests
1. Create aggregation file via pandas
1. Add tests
1. Add endpoint for aggregations
1. Add tests
1. Update endpoint for POST request to calculate aggregations
1. Add tests

## Refactor

1. Add mongo to better handle data aggregations
1. Add more aggregations
1. Add more tests - right now payload can only handle a single JSON object, not an array like the sample
1. Add more `try/except`s, better error handling
1. Increase code coverage
1. Add task queue - so users can upload large files without having to wait, results are emailed
1. Benchmark handling some of the data relationally
