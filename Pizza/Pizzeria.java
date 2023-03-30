package Pizza;


public abstract class Pizzeria {
   
    public abstract Pizza createPizza(String type);

    public void orderPizza(String type) {
        Pizza pizza = createPizza(type);
        pizza.bake();
        pizza.cut();
        pizza.box();
    }

}


