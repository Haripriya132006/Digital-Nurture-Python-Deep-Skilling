from flask import Flask,jsonify
from config import Config
from courses.routes import courses_bp
def create_app():
          app=Flask(__name__)
          app.config.from_object(Config)
          app.register_blueprint(courses_bp)
          
          @app.errorhandler(404)
          def handle_not_found_error(error):
                    return jsonify({
                              "status":"error",
                              "message":"The requested url not found in this server."
                              }),404
          @app.errorhandler(500)
          def handle_internal_server_error(error):
                    return jsonify({
                              "status":"error",
                              "message":"Internal server error has occured. try again later."
                    }),500
                    
          return app
if __name__=='__main__':
          app=create_app()
          app.run()