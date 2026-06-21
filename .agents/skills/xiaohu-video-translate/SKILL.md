```markdown
# xiaohu-video-translate Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches you the development conventions and workflows used in the `xiaohu-video-translate` Python codebase. You'll learn about file organization, import/export styles, commit message patterns, and how to write and run tests. This guide is ideal for contributors looking to maintain consistency or onboard quickly.

## Coding Conventions

### File Naming
- Use **snake_case** for all file names.
  - Example: `video_processor.py`, `audio_utils.py`

### Import Style
- Use **relative imports** within the package.
  - Example:
    ```python
    from .audio_utils import extract_audio
    ```

### Export Style
- Use **named exports**; explicitly define what is exported from each module.
  - Example:
    ```python
    def translate_video(...):
        ...

    __all__ = ['translate_video']
    ```

### Commit Messages
- Freeform style, no strict prefixes.
- Average commit message length: ~34 characters.
  - Example: `fix bug in audio extraction logic`

## Workflows

### Adding a New Feature
**Trigger:** When you want to introduce a new capability to the codebase  
**Command:** `/add-feature`

1. Create a new Python file using snake_case if needed.
2. Implement the feature using relative imports for dependencies.
3. Export new functions or classes using named exports.
4. Write or update tests in a corresponding `*.test.*` file.
5. Commit your changes with a clear, concise message.

### Fixing a Bug
**Trigger:** When you need to resolve a defect  
**Command:** `/fix-bug`

1. Locate the relevant module and identify the issue.
2. Apply the fix, maintaining coding conventions.
3. Update or add tests to cover the bug scenario.
4. Commit with a descriptive message about the fix.

### Running Tests
**Trigger:** To verify code correctness after changes  
**Command:** `/run-tests`

1. Identify test files matching the `*.test.*` pattern.
2. Use the project's preferred test runner (framework unspecified; check for documentation or use `pytest` as a default).
3. Run all tests and ensure they pass before merging changes.

## Testing Patterns

- Test files follow the `*.test.*` naming pattern.
  - Example: `video_processor.test.py`
- The specific testing framework is unknown; check for documentation or use `pytest` as a default.
- Place tests alongside or near the modules they test.
- Write tests for new features and bug fixes.

## Commands
| Command        | Purpose                                   |
|----------------|-------------------------------------------|
| /add-feature   | Start the workflow for adding a new feature|
| /fix-bug       | Begin the bug fixing workflow              |
| /run-tests     | Run all tests in the codebase              |
```
