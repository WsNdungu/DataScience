def print_all(**kwargs):
    """Prints out key-value pairs in kwargs"""
    
    # Print out key-value pairs
    for key, value in kwargs.items():
        print(key + ": " + value)

print_all(Name = "Samuel Ndungu", Job="Underwritter", Company= "Safetrip Insurance Agency")        