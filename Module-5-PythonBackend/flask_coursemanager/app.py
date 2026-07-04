from flask import Flask,jsonify

from config import Config
from extensions import db,migrate

def create_app():
          app=Flask(__name__)
          app.config.from_object(Config)
          
          db.init_app(app)
          migrate.init_app(app,db)
          from courses import models
          from courses.routes import courses_bp

          app.register_blueprint(courses_bp)
          with app.app_context():
                    db.create_all()
                    
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