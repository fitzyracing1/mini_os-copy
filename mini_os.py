#!/usr/bin/env python3
"""
Mini text-menu "OS" with DuckDuckGo search and expression evaluator.
"""
import os
import sys
from duckduckgo_search import DDGS

def safe_int(val, default=10, low=1, high=100):
    try:
        return max(low, min(high, int(val)))
    except Exception:
        return default

def do_search():
    query = input("Enter search query: ").strip()
    if not query:
        print("Query cannot be empty.\n")
        return
    max_results = safe_int(input("Max results [default 10]: ") or 10)
    print(f"\nSearching DuckDuckGo for '{query}' (max {max_results})...\n")
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(
                keywords=query,
                region="wt-wt",
                safesearch="moderate",
                backend="api",
                max_results=max_results
            ) or [])
        if not results:
            print("No results found.\n")
            return
        for i, r in enumerate(results, 1):
            print(f"{i}. {r.get('title','No title')}")
            print(f"   URL: {r.get('href')}")
            print(f"   Snippet: {r.get('body','No snippet')}\n")
    except Exception as e:
        print(f"Error during search: {e}\nTip: Try again later or reduce max_results.\n")

def do_expression():
    expr = input("Enter expression (e.g., x1*c*c*z*1): ").strip()
    if not expr:
        print("Expression cannot be empty.\n")
        return
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*_ ")
    if any(ch not in allowed for ch in expr):
        print("Only *, letters, numbers, and underscores are allowed.\n")
        return
    try:
        scope = {"x1": 2.0, "c": 3.0, "z": 4.0}
        result = eval(expr, {"__builtins__": {}}, scope)
        print(f"Using scope {scope}, {expr} = {result}\n")
    except Exception as e:
        print(f"Could not evaluate expression: {e}\n")

def main():
    while True:
        print("=== Mini OS ===")
        print("1) DuckDuckGo search")
        print("2) Evaluate expression")
        print("q) Quit")
        choice = input("Select: ").strip().lower()
        if choice == "1":
            do_search()
        elif choice == "2":
            do_expression()
        elif choice == "q":
            print("Goodbye.")
            return
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    # Allow forced non-interactive runs (e.g., when piping test input) via env var.
    force = bool(os.environ.get("MINI_OS_FORCE_RUN"))
    if sys.stdin.isatty() or force:
        main()
    else:
        print("Run this script in a terminal for the interactive menu or set MINI_OS_FORCE_RUN=1 for piped input.")
