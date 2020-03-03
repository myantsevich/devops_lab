Summary
=======
Here is a simple, separate python app which monitors your system

It monitors the following options:

● Overall CPU load

● Overall memory usage

● Overall virtual memory usage

● IO information

● Network information


How to work with
=======
The app makes shapshot of systems parameters every 5 minutes(default). This data are written into txt file (default). Every snapshot has index number and time tag.

Users can change default parameters (time and file's type) or leave them as is.

IMPORTANT: The app should be stopped by user. The app do not have to stop by time out because of continuous monitoring (hypothetically)


To start
=======

- git fetch / git checkout
- pip install devops_lab
- snapshot ('json|txt', 'int')

