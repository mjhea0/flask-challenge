Attached, you’ll find a zipped JSON file containing a Journey Dataset from one of our demo environments. This is a standard output format for our main product. Each of the 10k sampled records represents a single phone call. The object model represents our session object, each one described with a few core attributes, an extensible list of session attributes, a list of events (with their own attributes), and a list of filters and "paths=" (an event sequence defined by the user) satisfied by the session. You’ll note that the phone calls all occur within a single calendar day and that one customer may have made multiple calls in the day.

For this exercise, we’re looking for a Python REST service with two key features:

1. Feature 1: We need an endpoint that will allow a user to upload a data file; i.e. the attached file.
1. Feature 2: We need an endpoint that allows the user to request an aggregate of one field in that file; i.e. "event_duration=" or "cti.num_agents=".
