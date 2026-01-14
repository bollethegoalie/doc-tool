"""
Tests for the main module. 

Tests make sure your code works correctly! 
"""
from doc_tool.main import main  # ← Changed from my_awesome_app to doc_tool! 

def test_main():
    """
    Test that the main function runs without errors.
    """
    # Call the main function
    # If it crashes, this test fails
    # If it completes, this test passes
    main()

def test_main_returns_none():
    """
    Test that main() doesn't return anything.
    """
    result = main()
    assert result is None  # Should return None (nothing)
