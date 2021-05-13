# shibaofwisdom

Final freestyle project for OPIM 244 (Spring 2021)


## Setup

Create and activate a new virtual environment from the command line (e.g. GitBash):

```sh
conda create -n shiba-env python=3.8
```

You only have to create the environment the first time you run the program. To activate the environment for the first time and any time after running the program, enter this from the command line:

```sh
conda activate shiba-env
```

Install the programs needed to run the Shiba of Wisdom program from the command line using:

```sh
pip install -r requirements.txt
```

## Running the Shiba of Wisdom program

Navigate to the root directory of the program in the command line and enter this code to receive advice from the Shiba of Wisdom program:

```sh
python -m app.shiba
```

Below is a guide to the acceptable user-given inputs in the program:
| Prompt | Acceptable Inputs |
| ----------- | ----------- |
| Do you wish to ask the Shiba of Wisdom about something or receive fated, random advice? [ask/random]: | ask, random |
| What do you wish to ask the Shiba of Wisdom for advice on?: | any string search term ex: avocado, love, fail |


## Testing

To run the tests for the Shiba of Wisdom program, enter the below code in the command line:

```sh
pytest
```
