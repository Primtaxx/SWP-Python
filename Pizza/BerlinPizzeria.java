package Pizza;

public class BerlinPizzeria extends Pizzeria {
    @Override
    public Pizza createPizza(String type) {
        switch (type) {
            case "Salami":
                return new BerlinSalamiPizza();
            case "Hawaii":
                return new HawaiiPizza();
            case "Calzone":
                return new CalzonePizza();
            case "QuattroStagioni":
                return new QuattroStagioniPizza();
            default:
                throw new IllegalArgumentException("Unknown pizza type: " + type);
        }
}
}