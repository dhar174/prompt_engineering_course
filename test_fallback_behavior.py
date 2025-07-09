#!/usr/bin/env python3
"""
Test script to verify the get_embeddings fallback behavior works correctly.

This test addresses issue #64 to ensure that the get_embeddings function
properly returns a fallback OpenAIEmbeddings instance when HuggingFace
embeddings fail to load, rather than returning None.
"""
import os
import sys

def test_get_embeddings_fallback():
    """
    Test that get_embeddings properly handles fallback case and never returns None.
    
    This test specifically validates the fix for the issue:
    "After printing the fallback message, the function does not return a 
    fallback embedding instance, causing it to return None."
    """
    # Set a dummy API key to avoid validation errors during testing
    os.environ['OPENAI_API_KEY'] = 'test_key_for_validation'
    
    # Import the function under test
    sys.path.insert(0, 'gradio_app')
    try:
        from faiss_helper import get_embeddings
    except ImportError as e:
        print(f"❌ Failed to import get_embeddings: {e}")
        return False
    
    print("Testing get_embeddings fallback behavior...")
    
    # Test case 1: Normal OpenAI path
    print("\n1. Testing use_openai=True (normal path):")
    try:
        embeddings_openai = get_embeddings(use_openai=True)
        assert embeddings_openai is not None, "OpenAI embeddings should not be None"
        assert 'OpenAIEmbeddings' in str(type(embeddings_openai)), "Should return OpenAIEmbeddings"
        print("   ✅ OpenAI path works correctly")
    except Exception as e:
        print(f"   ❌ OpenAI path failed: {e}")
        return False
    
    # Test case 2: HuggingFace fallback path (the critical test case)
    print("\n2. Testing use_openai=False (fallback path):")
    try:
        embeddings_fallback = get_embeddings(use_openai=False)
        
        # This is the critical assertion - the function should NEVER return None
        assert embeddings_fallback is not None, "Fallback embeddings should NEVER be None"
        
        # It should fall back to OpenAI embeddings
        assert 'OpenAIEmbeddings' in str(type(embeddings_fallback)), "Should fallback to OpenAIEmbeddings"
        
        print("   ✅ Fallback path works correctly - returns valid embedding instance")
        print(f"   ✅ Returned type: {type(embeddings_fallback)}")
        
    except Exception as e:
        print(f"   ❌ Fallback path failed: {e}")
        return False
    
    print("\n✅ All tests passed! The get_embeddings function properly handles fallback.")
    print("✅ Issue #64 fix confirmed: Function never returns None in fallback case.")
    
    return True

if __name__ == "__main__":
    success = test_get_embeddings_fallback()
    if not success:
        print("\n❌ Tests failed!")
        sys.exit(1)
    else:
        print("\n🎉 All tests passed!")
        sys.exit(0)