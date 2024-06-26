# autoPG-smar3-plots
Plots for the SMAR3 industrial plant. We will be plotting temperature with its own SP and electrical current, but also 
the level of a conical tank with its control valve and SP.

To run the project, you will need to install `Pipenv`.

```bash
pipenv --python 3.12
```

Then, you will need to install the project dependencies. You can run the following command:

```bash
pipenv install
```

To run one of the project files, use the following command:

```bash
pipenv run python tank2_level_control.py
```