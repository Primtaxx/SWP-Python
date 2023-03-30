package Pizza;

public class HamburgPizzeria extends Pizzeria {
    @Override
    public Pizza createPizza(String type) {
        switch (type) {
            case "Salami":
                return new SalamiPizza();
            case "Hawaii":
                return new HamburgHawaiiPizza();
            case "Calzone":
                return new CalzonePizza();
            case "QuattroStagioni":
                return new QuattroStagioniPizza();
            default:
                throw new IllegalArgumentException("Unknown pizza type: " + type);
        }
}
}