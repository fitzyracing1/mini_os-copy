# Mini OS

A minimal text-based "operating system" with DuckDuckGo search and expression evaluation.

## Features
- **DuckDuckGo Search**: Web search with configurable max results
- **Expression Evaluator**: Compute mathematical expressions (e.g., `x1*c*c*z*1`)

## Setup
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install duckduckgo-search

# Run
python mini_os.py
```

## Usage
Interactive menu:
1. DuckDuckGo search - enter query and max results
2. Evaluate expression - enter math expression using variables x1, c, z

## Non-interactive mode
```bash
MINI_OS_FORCE_RUN=1 python mini_os.py <<'EOF'
2
x1*c*c*z*1
q
EOF
```
