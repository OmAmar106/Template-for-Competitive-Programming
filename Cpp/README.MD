# C++ Snippets

This folder contains the VS Code C++ snippets and their generated code files.

- **`cpp.jsonc`**: Contains the C++ snippets exactly as they are stored in VS Code, without any modifications.
- **`cpp_snippet_files/`**: Contains the individual code files generated from `cpp.jsonc` using GitHub Actions.

Whenever `cpp.jsonc` is updated, GitHub Actions automatically regenerates the corresponding files in `cpp_snippet_files/`.