from app import app
import os
app.debug = True

if  __name__ == "__main__":
    app.run(
        host=os.getenv('LISTEN','0.0.0.0'),
        port=int(os.getenv('PORT', '8080'))
    )