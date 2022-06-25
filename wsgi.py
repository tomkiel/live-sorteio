from app.falafel import app
import os
os.environ["PWD"] = os.getcwd()

if __name__ == "__main__":
    app.run()