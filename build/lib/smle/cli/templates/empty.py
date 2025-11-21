from smle import SMLEApp

# Instantiate the application object
app = SMLEApp()

# Register the main function
@app.entrypoint
def main(args):
    """
    This is the user's core logic function, which receives the config (args).
    """

    # ========================================
    # TODO: ADD YOUR CODE HERE
    # ========================================


# Run the application
if __name__ == "__main__":
    app.run()