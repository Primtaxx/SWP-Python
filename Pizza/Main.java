package Pizza;

public class Main {
    public static void main(String[] args) {
        Pizzeria berlinPizzeria = new BerlinPizzeria();
        berlinPizzeria.orderPizza("Salami");

        Pizzeria hamburgPizzeria = new HamburgPizzeria();
        hamburgPizzeria.orderPizza("Hawaii");

        Pizzeria rostockPizzeria = new RostockPizzeria();
        rostockPizzeria.orderPizza("Calzone");
    }
}
