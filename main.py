
from Controller.estoque_controller import EstoqueController
from Model.estoque_model import EstoqueModel
from View.estoque_view import EstoqueView

if __name__ == "__main__":
    model = EstoqueModel('Data/estoque_kanemoto.csv')
    view = EstoqueView()
    controller = EstoqueController(model, view)
    controller.run()
