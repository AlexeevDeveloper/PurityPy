<h1 align="center">PurityPy 🧹💻</h1>

<p align="center">Powerful Linter and Formatter for Clean Python Code</p>
<br>
<p align="center">
    <img src="https://img.shields.io/github/languages/top/AlexeevDeveloper/PurityPy?style=for-the-badge">
    <img src="https://img.shields.io/github/languages/count/AlexeevDeveloper/PurityPy?style=for-the-badge">
    <img src="https://img.shields.io/github/stars/AlexeevDeveloper/PurityPy?style=for-the-badge">
    <img src="https://img.shields.io/github/issues/AlexeevDeveloper/PurityPy?style=for-the-badge">
    <img src="https://img.shields.io/github/last-commit/AlexeevDeveloper/PurityPy?style=for-the-badge">
    </br>
</p>

> Your reliable assistant in maintaining cleanliness and order in your Python code!

PurityPy is a powerful tool that will take care of the quality of your code. It combines advanced formatters, linters, and reporters to help you write code that meets the highest standards. Our goal is to make your code cleaner, more beautiful, and more reliable.

> [!CAUTION]
> At the moment, PurityPy is under active development, many things may not work, and this version is not recommended for use (all at your own risk).

## Features 🚀

- Code Formatting: Support for popular formatters like Black and Autopep8 to bring your code to a consistent style.
- Linting: Integration with the best linters, such as Flake8 and Pylint, to identify errors, vulnerabilities, and style violations.
- Flexible Configuration: Customize the tool's behavior through the .puritypy.toml configuration file.
- Custom Checks: Ability to create your own custom checks and linters for specialized requirements.
- Convenient Reports: Generation of reports in the console and HTML format for clear visualization of the results.
- Integration with Rich: Use the Rich library to create a beautiful and interactive terminal interface.
- Emergency Development: The first version of PunityPy was created in just 2-3 days of intersive work, making this tool unique.

## Libraries and Dependencies 📦

To implement PurityPy, we use the following libraries:

- [Rich](https://github.com/Textualize/rich) - for creating a beautiful terminal interface
- [Flake8](https://gitlab.com/pycqa/flake8) - for static code analysis to comply with PEP8 standards
- [Pylint](https://www.pylint.org/) - for advanced code analysis to detect errors, vulnerabilities, and style issues
- [Black](https://github.com/psf/black) - for automatic code formatting
- [Autopep8](https://github.com/hhatto/autopep8) - for automatically fixing formatting errors

All these libraries can be installed using pip:

```bash
pip install rich flake8 pylint black autopep8 rich
```

## Project Structure 📁

The structure of the PurityPy project looks like this:

```
PurityPy/
├── puritypy/
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── data_processor.py
│   │   └── data_analyzer.py
│   ├── formatter/
│   │   ├── __init__.py
│   │   ├── black_formatter.py
│   │   └── autopep8_formatter.py
│   ├── linters/
│   │   ├── __init__.py
│   │   ├── flake8_linter.py
│   │   ├── pylint_linter.py
│   │   └── purefure.py
│   ├── reporters/
│   │   ├── __init__.py
│   │   ├── console_reporter.py
│   │   └── html_reporter.py
│   └── utils/
│       ├── __init__.py
│       ├── file_utils.py
│       └── error_handling.py
├── tests/
│   ├── __init__.py
│   ├── test_formatter.py
│   ├── test_linters.py
│   └── test_reporters.py
├── docs/
│   ├── index.md
│   └── usage.md
├── setup.py
└── README.md
```

## Example .puritypy.toml Configuration 📝

```toml
[puritypy]
root_dir = "."
ignore_dirs = ["venv", "build", "dist", "bin"]
ignore_files = ["__init__.py", "setup.py"]

[formatters]
black = true
autopep8 = true

[linters]
flake8 = true
pylint = true
purefury = true

[reporters]
console = true
html = true
```

## Quick Start 🚀

To start using PurityPy, create a .puritypy.toml file in the root of your project and specify the necessary settings. After that, you can run the analysis of your code:

puritypy analyze path/to/your/code
For more detailed information on using PurityPy, please refer to the [documentation](docs/usage.md).

## Distinctive Features ✨

- Emergency Development: The first version of PurityPy was created in just 2-3 days of intensive work, making this tool unique.
- Flexibility and Extensibility: Thanks to its modular architecture, PurityPy can be easily extended with new formatters, linters, and reporters.
- Asynchronous Support: Ability to use asynchronous I/O to speed up the analysis of large codebases.
- Integration with Rich: Beautiful and interactive terminal interface created using the Rich library.
- Customization: Flexible configuration of the tool through the .puritypy.toml configuration file.

## Contribute 🤝
We welcome any suggestions and contributions to improve PurityPy. Check out the [contributor's guide](CONTRIBUTING.md) to get started.

## Contact and support
If you have questions about using PurityPy, then create an [issue](https://github.com/AlexeevDeveloper/PurityPy/issues/new) in the repository or write to me at alexeev.developer@gmail.com or bro.alexeev@inbox.ru or alexeev.dev@mail.ru.

You can also write to me on Telegram: [@alexeev_dev](https://t.me/alexeev_dev)

PurityPy is an Open Source software, and it only survives due to your feedback and support!

Project releases are available at [this link](https://github.com/AlexeevBronislav/PurityPy/releases).

## License 📄
Copyright © 2024, Alexeev Bronislav

This project is distributed under the [GNU LGPL License](LICENSE).

All rights reversed
