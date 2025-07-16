# Contribution Guidelines

Contributions are welcome, and are greatly appreciated! Even small contributions are helpful, and credit will always be given!

## Types of Contributions

### Report Bugs

To report a bug, first make sure there isn't already an open [GitHub Issue](https://github.com/KuantumBS/grikod/issues)
about it. If not, you can submit a new issue, making sure to include:

* Your OS name and version.
* Any details about your local setup (_e.g._, your Python environment setup) that might be helpful in troubleshooting.
* The Solar Data Tools version you are using.
* Detailed steps to reproduce the bug.
* A tag, if appropriate (_e.g._, "bug" or "enhancement").

### Fix Open Issues

Look through the [GitHub Issues](https://github.com/KuantumBS/grikod/issues) for any
reported bugs. Anything tagged with "bug" and "help wanted" is open to contributions.

### Implement Features

Look through the [GitHub Issues](https://github.com/KuantumBS/grikod/issues) for any
feature requests. Anything tagged with "enhancement" and "help  wanted" is open to contributions.

### Write Documentation

You can never have enough documentation! Please feel free to contribute to any
part of the documentation, such as the getting started guides or the docstrings/API reference.

## Get Started!

Ready to contribute? Here's how to set up Solar Data Tools for local development.

1. You will need to have `git` installed on your local machine, and you will need some way to create and manage
Python virtual environments. We recommend using `conda`.
2. Create your own fork of the Solar Data Tools [repository](https://github.com/KuantumBS/grikod).
3. Clone your repository, for example by typing in your terminal:
`git clone https://github.com/<your_username>/kececifractals.git`.
4. Install `solardatatools` as editable in your new environment:

    ```console
    $ pip install -e .
    ```
   If you would like to install optional dependencies, such as MOSEK or docs-specific dependencies, you can do so by:
    ```console
    $ pip install -e ".[docs]"
    ```
5. Create a branch for local development and make your changes:

    ```console
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

6. If you have made changes to the documentation, you can build the docs locally by running:

    ```console
    $ cd docs
    $ make html
    ```

   This will create a local copy of the documentation in `_build/html/index.html`.

7. When you're done making changes, check that your changes conform to any code formatting requirements and pass any tests. One of the automated checks for each PR is linting with ruff and pre-commit hooks and will fail otherwise. You can install pre-commit with `pip install pre-commit` and then run `pre-commit install` in the root of the repository. When you commit your changes, the pre-commit hooks will run automatically.

8. Commit and push your changes to your fork, and open a pull request.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include additional tests if appropriate.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for all currently supported operating systems and versions of Python.

## Code of Conduct

Please note that the Solar Data Tools project is released with a
[Code of Conduct](getting_started/CODE_OF_CONDUCT.md). By contributing to this project you agree to abide by its terms.
