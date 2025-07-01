# Contributing to BlazeBuster

Thank you for your interest in contributing to BlazeBuster! We welcome contributions from the community and are pleased to have you here.

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contribution Guidelines](#contribution-guidelines)
- [Code Style](#code-style)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Reporting Issues](#reporting-issues)

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git
- Basic knowledge of Flask and machine learning concepts

### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/your-username/BlazeBuster---Fire-Weather-Index-Forecaster.git
   cd BlazeBuster---Fire-Weather-Index-Forecaster
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python application.py
   ```

## 🤝 Contribution Guidelines

### Types of Contributions

We welcome several types of contributions:

- **Bug fixes** - Fix issues in the codebase
- **Feature enhancements** - Add new functionality
- **Documentation improvements** - Enhance README, comments, or docs
- **Performance optimizations** - Improve application speed or efficiency
- **UI/UX improvements** - Enhance user interface and experience
- **Test coverage** - Add or improve tests

### Before You Start

1. Check the [Issues](https://github.com/krishnakamalbaishnab/BlazeBuster---Fire-Weather-Index-Forecaster/issues) page to see if your feature/bug is already being worked on
2. For major changes, please open an issue first to discuss what you would like to change
3. Make sure your development environment is set up correctly

## 📝 Code Style

### Python Code

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions small and focused on a single task

### HTML/CSS

- Use semantic HTML5 elements
- Follow consistent indentation (2 spaces)
- Use meaningful class names
- Keep CSS organized and commented

### Example Python Function

```python
def calculate_fire_risk(fwi_value):
    """
    Calculate fire risk level based on FWI value.
    
    Args:
        fwi_value (float): Fire Weather Index value
        
    Returns:
        str: Risk level ('low', 'moderate', 'high', 'extreme')
    """
    if fwi_value < 5:
        return 'low'
    elif fwi_value < 15:
        return 'moderate'
    elif fwi_value < 25:
        return 'high'
    else:
        return 'extreme'
```

## 🧪 Testing

### Running Tests

Currently, the project doesn't have comprehensive tests, but we welcome contributions to add them!

```bash
# When tests are implemented
python -m pytest tests/
```

### Adding Tests

- Write unit tests for new functions
- Test edge cases and error conditions
- Ensure tests pass before submitting PR

## 📤 Submitting Changes

### Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clear, concise commit messages
   - Include comments for complex logic
   - Update documentation if necessary

3. **Test your changes**
   - Verify the application runs without errors
   - Test your new feature thoroughly
   - Check for any breaking changes

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Use a clear, descriptive title
   - Provide a detailed description of changes
   - Reference any related issues
   - Add screenshots for UI changes

### Commit Message Format

Use the following format for commit messages:

```
type: brief description

Detailed explanation of the change (if necessary)

- List any breaking changes
- Reference issues: Fixes #123
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting (no logic changes)
- `refactor`: Code restructuring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

## 🐛 Reporting Issues

### Bug Reports

When reporting bugs, please include:

1. **Clear title** describing the issue
2. **Steps to reproduce** the bug
3. **Expected behavior** vs **actual behavior**
4. **Environment details** (OS, Python version, browser)
5. **Screenshots** if applicable
6. **Error messages** or logs

### Feature Requests

For feature requests, please include:

1. **Clear description** of the proposed feature
2. **Use case** - why is this feature needed?
3. **Possible implementation** ideas (if any)
4. **Examples** or mockups (if applicable)

## 📞 Getting Help

If you need help or have questions:

1. Check existing [Issues](https://github.com/krishnakamalbaishnab/BlazeBuster---Fire-Weather-Index-Forecaster/issues)
2. Create a new issue with the "question" label
3. Be specific about what you're trying to achieve

## 🏷️ Labels

We use the following labels to organize issues and PRs:

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested

## 🎉 Recognition

Contributors will be acknowledged in:

- README.md file
- Release notes for major contributions
- Special mentions for significant improvements

Thank you for contributing to BlazeBuster! Your efforts help make fire weather prediction more accessible and accurate. 🔥🌟 