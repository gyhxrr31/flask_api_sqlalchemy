from flask import render_template
import connexion

# создаем экземпляр приложения с помощью connexion, а не flask
# Flask все еще используется, но уже с дополнительными функциями по типу swagger

app = connexion.App(__name__, specification_dir="./") 
app.add_api("swagger.yml")


@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)