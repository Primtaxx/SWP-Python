package Pizza;

public class RostockPizzeria extends Pizzeria {
    @Override
    public Pizza createPizza(String type) {
        switch (type) {
            case "Salami":
                return new SalamiPizza();
            case "Hawaii":
                return new HawaiiPizza();
            case "Calzone":
                return new RostockCalzonePizza();
            case "QuattroStagioni":
                return new QuattroStagioniPizza();
            default:
                throw new IllegalArgumentException("Unknown pizza type: " + type);
        }
    }
}